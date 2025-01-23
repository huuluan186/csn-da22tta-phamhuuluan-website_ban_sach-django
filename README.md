# csn-da22tta-phamhuuluan-book_selling_web-django
# Django ebook-store
Ứng dụng web bán sách được xây dựng bằng Django 5, MySQL và Bootstrap 5.

Ứng dụng này cũng sử dụng một số gói bổ sung như:

django-crispy-forms

django-filter

pillow

easy-thumbnails

dj-database-url

Trong ứng dụng này, quản trị viên có thể quản lý sản phẩm và đơn hàng, trong khi khách hàng có thể đăng ký tài khoản, thêm sản phẩm vào giỏ hàng,...


# 🚀 Cách chạy chương trình

1️⃣ Cài đặt môi trường

Yêu cầu Python >=3.8.

2️⃣ Clone repository về máy


git clone https://github.com/huuluan186/csn-da22tta-phamhuuluan-website_ban_sach-django/tree/main/src/webbanhang-main

3️⃣ Cài đặt các thư viện cần thiết

Chạy lệnh sau trong terminal:

pip install -r requirements.txt  

Mở tệp settings.py của dự án Django và sửa phần DATABASES:


DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'ten_csdl',  # Tên cơ sở dữ liệu

        'USER': 'ten_user',  # Tên user MySQL

        'PASSWORD': 'mat_khau',  # Mật khẩu của user

        'HOST': 'localhost',  # Máy chủ (local)

        'PORT': '3306',  # Cổng mặc định của MySQL

    }

}

4️⃣ Tạo tài khoản quản trị (superuser)

Chạy lệnh:


python manage.py createsuperuser  
Sau đó nhập tên đăng nhập, email và mật khẩu của bạn.

5️⃣ Thực hiện di chuyển dữ liệu (migrate)

Chạy lệnh:


python manage.py migrate  
6️⃣ Khởi động server

Chạy lệnh:


python manage.py runserver  
7️⃣ Truy cập ứng dụng

Ứng dụng chính: Truy cập http://localhost:8000/
Module quản trị: Truy cập http://localhost:8000/admin và đăng nhập bằng tài khoản quản trị vừa tạo.



# 📞 Liên hệ

👤 Phạm Hữu Luân

📧 Email: luanphamhuu2004@example.com
  
📞 Số diện thoại: 0386291762
📚 Trường Đại học Trà Vinh


