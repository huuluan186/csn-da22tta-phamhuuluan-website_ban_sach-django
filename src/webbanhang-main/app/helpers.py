from io import BytesIO
import textwrap
import matplotlib.pyplot as plt
from .models import *
import base64
from django.db.models import Sum, Count
import json
from django.http import JsonResponse


def updateItem(request):
    data = json.loads(request.body)  # Đọc dữ liệu JSON từ body của yêu cầu
    productId = data['productId']  # Lấy ID của sản phẩm từ dữ liệu đã phân tích
    action = data['action']  # Lấy hành động ('add' hoặc 'remove') từ dữ liệu đã phân tích
    customer = request.user  # Lấy đối tượng customer liên kết với người dùng hiện tại
    product = Product.objects.get(id=productId)  # Lấy đối tượng sản phẩm theo ID
    order, created = Order.objects.get_or_create(customer=customer)  # Tìm hoặc tạo một đơn hàng chưa hoàn thành cho khách hàng
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)  # Tìm hoặc tạo một mục đơn hàng cho sản phẩm trong đơn hàng

    if action == 'add':
        if product.quantity > 0:  # Kiểm tra còn hàng
            orderItem.quantity += 1
            product.quantity -= 1  # Giảm số lượng trong kho
            product.save()
        else:
            return JsonResponse({"error": "Hết hàng!"}, status=400)

    if action == 'remove':
        if orderItem.quantity > 0:
            orderItem.quantity -= 1
            product.quantity += 1  # Tăng số lượng trong kho khi xóa khỏi giỏ hàng
            product.save()

    orderItem.save()

    if orderItem.quantity <= 0:  # Nếu số lượng OrderItem <= 0 thì xóa
        orderItem.delete()

    # Cập nhật lại giỏ hàng sau khi thay đổi
    return JsonResponse("added", safe=False)



# Hàm dùng chung để lấy thông tin giỏ hàng
def get_cart_data(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer)
        if not created:
            order.save()  # Cập nhật đơn hàng nếu cần
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items  # Lấy số lượng sản phẩm trong giỏ hàng
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_value': 0}
        cartItems = order['get_cart_items']
    
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return context


def product_availability(quantity):
    if quantity > 0:
        return f"Còn lại: {quantity}"
    else:
        return "<strong>Hết hàng</strong>"
    

# xử lý danh mục và sản phẩm
def get_categories_and_products():
     # Lấy tất cả các danh mục cấp 1 (không phải danh mục con)
    categories = Category.objects.filter(is_sub=False)
    # Tạo một dictionary để lưu các sản phẩm theo từng danh mục
    products_by_category = {}
    product_availability_dict = {}
    # Lặp qua tất cả các danh mục
    for category in categories:
        # Lọc ra các sản phẩm của từng danh mục và lấy tối đa 4 sản phẩm
        products = Product.objects.filter(category=category)[:3]
        
        # Lưu tên danh mục và danh sách sản phẩm vào từ điển theo slug của danh mục
        products_by_category[category.slug] = {
            'name': category.name,  # Tên danh mục
            'products': products    # Các sản phẩm trong danh mục
        }

        # Lưu tình trạng hàng hóa cho từng sản phẩm vào dictionary
        for product in products:
            product_availability_dict[product.id] = product_availability(product.quantity)

    # Đưa dữ liệu vào context để truyền vào template
    # Kết hợp dữ liệu giỏ hàng (cart_data) và các dữ liệu cần thiết khác
    context = {'categories': categories, 'products_by_category': products_by_category, 'product_availability_dict': product_availability_dict} # Dữ liệu giỏ hàng
    return (context)


def tong_doanh_thu():
    orders = Order.objects.all()
    return sum([order.get_cart_value for order in orders])


def top_san_pham_ban_chay(limit=10):
    top_selling_products = OrderItem.objects.values('product')\
        .annotate(total_quantity=Sum('quantity'))\
        .order_by('-total_quantity')[:limit]
    
    product_names = []
    quantities = []
    for item in top_selling_products:
        product = Product.objects.get(id=item['product'])
        product_names.append(product.name)
        quantities.append(item['total_quantity'])
    
    return product_names, quantities

def top_san_pham_ton_kho(limit=10):
     # Lọc các sản phẩm có số lượng tồn kho lớn hơn 10, sắp xếp giảm dần theo số lượng tồn kho
    products = Product.objects.filter(quantity__gt=10).order_by('-quantity')[:10]
    
    # Tạo danh sách tên sản phẩm và số lượng tồn kho

    product_names = [product.name for product in products]
    quantities = [product.quantity for product in products]
    return product_names, quantities

def tong_ton_kho_tat_ca_sp():
    """
    Tính tổng số lượng tồn kho của tất cả các sản phẩm.
    """
    # Lấy tất cả các sản phẩm
    products = Product.objects.all()

    # Tính tổng tồn kho
    total_stock = sum([product.quantity for product in products])

    return total_stock


def ve_bieu_do_cot(product_names, quantities, title, x_label, y_label):
    """
    Hàm vẽ biểu đồ cột cho top sản phẩm.

    :param product_names: Danh sách tên sản phẩm
    :param quantities: Danh sách số lượng
    :param title: Tiêu đề biểu đồ
    :param x_label: Nhãn trục X
    :param y_label: Nhãn trục Y
    :return: Chuỗi base64 của ảnh biểu đồ
    """
    product_names_shortened = [textwrap.shorten(name, width=50, placeholder="...") for name in product_names]
    plt.figure(figsize=(10, 7))
    plt.bar(product_names_shortened, quantities, color='orange')
    for i, value in enumerate(quantities):
        plt.text(i,value+0.15,value,ha='center')
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    max_quantity = max(quantities)
    plt.ylim(0, max_quantity * 1.2)
    plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Lưu biểu đồ vào bộ nhớ tạm
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Mã hóa ảnh thành base64 để gửi vào template
    return base64.b64encode(image_png).decode('utf-8')

