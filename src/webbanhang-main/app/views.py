from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import  HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from app.helpers import *

# Create your views here.

def home(request):
    cart_data = get_cart_data(request)
    categories_data = get_categories_and_products()
    featured_products = Product.objects.filter(featured=True)[:3]
    is_home_page = True  # Xác định đây là trang chủ
    context = {**cart_data, **categories_data,
               'featured_products': featured_products,
               'is_home_page':is_home_page
               } 
    return render(request, 'app/home.html', context)

def featured_products(request):
    # Lấy các sản phẩm nổi bật
    featured_products= Product.objects.filter(featured=True)
    context = {
        'featured_products': featured_products,
    }
    return render(request, 'app/featured_products.html', context)

def category(request):
    categories = Category.objects.filter(is_sub=False)
     # Lấy slug của danh mục hiện tại từ tham số URL
    active_category = request.GET.get('category', '')
   
    if active_category:
        # Lấy sản phẩm theo slug danh mục
        products = Product.objects.filter(category__slug=active_category)
         # Lấy tên danh mục dựa vào slug
        active_category_name = Category.objects.get(slug=active_category).name
    else:
        products = []    
        active_category_name = "Tất cả sản phẩm"  # Giá trị mặc định
    cart_data=get_cart_data(request)    
    context = {'categories':categories,'products':products,'active_category_name':active_category_name,**cart_data}
    
    return render(request,'app/category.html',context)

def search(request):
    # Kiểm tra xem yêu cầu là POST hay không
    if request.method == "POST":
        # Lấy từ khóa tìm kiếm người dùng nhập vào từ form (thường là input có name="searched")
        searched = request.POST["searched"].strip()
        # Tìm kiếm các sản phẩm có tên chứa từ khóa nhập vào (phần 'name__contains' là lọc theo tên sản phẩm)
        if search:
            keys = Product.objects.filter(name__iregex=rf"\b{searched}\b") 
    cart_data=get_cart_data(request)
    categories = Category.objects.filter(is_sub=False)  
    products = Product.objects.all()
    context = {"searched": searched,"keys": keys,'products': products,'categories':categories,**cart_data}
    # Render kết quả tìm kiếm và truyền vào template các biến 'searched' và 'keys'
    return render(request, 'app/search.html', context)


# Hàm xử lý đăng ký người dùng
def register(request):
    # Tạo một instance của form CreateUserForm
    form = CreateUserForm()

    # Kiểm tra xem request có phải là phương thức POST không
    if request.method == "POST":
        # Nếu là POST, lấy dữ liệu từ request.POST và gán vào form
        form = CreateUserForm(request.POST)
        
        # Kiểm tra tính hợp lệ của form
        if form.is_valid():
            # Nếu form hợp lệ, lưu người dùng vào cơ sở dữ liệu
            form.save()
            messages.success(request, 'Đăng ký thành công! Bạn có thể đăng nhập ngay.')
            # return redirect('login')
        else:
            for error in form.errors.values():
                messages.info(request, error)
    

    # Truyền form vào context để render ra template
    cart_data=get_cart_data(request)     
    categories = Category.objects.filter(is_sub=False)     
    context = {'form': form,'categories':categories,**cart_data}

    # Trả về response với template 'register.html' và truyền context vào
    return render(request, 'app/register.html', context)


def log_in(request):
    # Lấy thông tin từ form
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin:index')
        return redirect('home')
    # Xác thực người dùng
    if request.method == "POST":
        user_name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request,username=user_name,password= pwd)
        if user is not None:  # Nếu người dùng tồn tại và thông tin hợp lệ
            login(request, user)  # Đăng nhập người dùng
            if user.is_superuser:
                return redirect('admin:index')
            return redirect('home')  # Chuyển hướng người dùng đến trang chủ hoặc trang khác
        else: 
            messages.info(request,'Tên đăng nhập hoặc mật khẩu không đúng!')
    cart_data=get_cart_data(request)   
    categories = Category.objects.filter(is_sub=False)          
    context={**cart_data,'categories':categories}
    return render(request,'app/login.html',context)



def log_out(request):
    logout(request)
    return redirect('login')

def about(request):
    cart_data=get_cart_data(request)
    categories = Category.objects.filter(is_sub=False)  
    context = {**cart_data,'categories':categories}  
    return render(request,'app/about.html',context)

def cart(request):
    cart_data=get_cart_data(request)
    categories = Category.objects.filter(is_sub=False)
    context = {**cart_data,'categories':categories }  # Tạo một từ điển `context` chứa các mục và đơn hàng
    return render(request, 'app/cart.html', context)  # Trả về trang 'cart.html' với `context` đã tạo


def checkout(request):
    cart_data=get_cart_data(request)
    categories = Category.objects.filter(is_sub=False)  
    context = {**cart_data,'categories':categories}  
    return render(request,'app/checkout.html',context)



def statistics_view(request):
    cart_data=get_cart_data(request)
    categories = Category.objects.filter(is_sub=False)   
     # Kiểm tra nếu người dùng là admin (superuser)
    if not request.user.is_superuser:
        return HttpResponseForbidden("Bạn không có quyền truy cập vào trang này!<br><a href='/login/'>Quay lại trang đăng nhập</a>")
    
    total_revenue = tong_doanh_thu()

    total_stock= tong_ton_kho_tat_ca_sp()

    # Tính sản phẩm bán chạy nhất (được đặt nhiều nhất)
    top_product_names, top_quantities = top_san_pham_ban_chay()
    
    # Tính top sản phẩm tồn kho nhiều nhất
    stock_product_names, stock_quantities = top_san_pham_ton_kho()

  
 
 # Sử dụng hàm ve_bieu_do để tạo biểu đồ cho top sản phẩm bán chạy
    bieu_do_cot_ban_chay =ve_bieu_do_cot(
        top_product_names, top_quantities, 
        'Top Sản Phẩm Bán Chạy Nhất', 'Sản Phẩm', 'Số Lượng Bán'
    )

    # Sử dụng hàm ve_bieu_do để tạo biểu đồ cho top sản phẩm tồn kho
    bieu_do_cot_ton_kho = ve_bieu_do_cot(
        stock_product_names, stock_quantities, 
        'Top Sản Phẩm Tồn Kho Nhiều Nhất', 'Sản Phẩm', 'Số Lượng Tồn Kho'
    )

    context = {
        'total_revenue': total_revenue,
        'total_stock':total_stock,
        'top_product_names': top_product_names,
        'top_quantities': top_quantities,
        'stock_product_names': stock_product_names,
        'stock_quantities': stock_quantities,
        'top_bar_chart': bieu_do_cot_ban_chay,  # Biểu đồ top bán chạy
        'stock_bar_chart': bieu_do_cot_ton_kho,  # Biểu đồ top tồn kho
        'categories':categories,
        **cart_data,
    }
    return render(request, 'app/statistics.html', context)



