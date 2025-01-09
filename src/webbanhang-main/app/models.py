from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum

# Create your models here.

# tạo class createuserform kế thừa từ class có sẵn trong django là usercreationform
class CreateUserForm(UserCreationForm):
    class Meta: # Meta class để xác định thông tin về model và các trường cần hiển thị trong form
        model=User
        fields = ['username', 'email', 'password1', 'password2']
    # đặt lại placeholder và độ dài cho các trường trên
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = {
            'username': "tên người dùng",
            'email': "địa chỉ email",
            'password1': "mật khẩu",
            'password2': "lại mật khẩu",
        }
        for field_name, label in field_names.items():
            # Đặt nhãn (label) cho các trường
            self.fields[field_name].label = label
            # Thiết lập placeholder cho từng trường
            self.fields[field_name].widget.attrs['placeholder'] = f"Nhập {label}"
            # Thiết lập thuộc tính style cho tất cả các trường
            self.fields[field_name].widget.attrs['style'] = 'width: 100%; max-width: 240px;'

class Category(models.Model):
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE,related_name='sub_categories',null=True,blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200,null=True)
    slug = models.SlugField(max_length=200,unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    # digital = models.BooleanField(default=False,null=True,blank=False)
    image = models.ImageField(null=True,blank=True) #làm xong cài pip install pillow
    category = models.ManyToManyField(Category,related_name='products')
    quantity = models.IntegerField(default=20, null=True, blank=True)  # Số lượng trong kho
    featured = models.BooleanField(default=False)
   

    class Meta:
        ordering = ['name']  # Sắp xếp theo tên sản phẩm
        
    def __str__(self):
        return self.name
    
    
    # điều chỉnh thuộc tính url của image
    @property
    def ImageURL(self):
        try:
            url =self.image.url
        except:
            url=''
        return url    


class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.id)
    
    #đếm số lượng sản phẩm mua trong giỏ hàng
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()# Lấy tất cả các OrderItem liên kết với Order hiện tại
        total = sum([item.quantity for item in orderitems]) # Tính tổng số lượng của từng sản phẩm
        return total
    
    # tính tổng giá trị của giỏ hàng
    @property
    def get_cart_value(self):
        orderitems = self.orderitem_set.all()
        value = sum([item.get_item_value for item in orderitems])  # Tính tổng giá trị của từng sản phẩm
        return value


# class này để xem khách hàng order sách gì ở class product
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    @property
    def get_item_value(self): #tính tổng giá trị của 1 sản phẩm trong giỏ hàng
        total_price = self.product.price * self.quantity
        return total_price

