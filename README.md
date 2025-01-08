<<<<<<< HEAD
csn-da22tta-phamhuuluan-book_selling_web-django
Django ebook-store
Ứng dụng web bán sách được xây dựng bằng Django 5, MySQL và Bootstrap 5.
Ứng dụng này cũng sử dụng một số gói bổ sung như:

django-crispy-forms
django-filter
pillow
easy-thumbnails
dj-database-url
Trong ứng dụng này, quản trị viên có thể quản lý sản phẩm và đơn hàng, trong khi khách hàng có thể đăng ký tài khoản, thêm sản phẩm vào giỏ hàng,...

Hướng dẫn chạy ứng dụng trên máy tính cá nhân
Cài đặt các thư viện cần thiết:
Chạy lệnh sau trong terminal:

bash
Sao chép mã
pip install -r requirements.txt  
Tạo tài khoản quản trị (superuser):
Chạy lệnh:

bash
Sao chép mã
python manage.py createsuperuser  
Sau đó nhập tên đăng nhập, email và mật khẩu của bạn.

Thực hiện di chuyển dữ liệu (migrate):
bash
Sao chép mã
python manage.py migrate  
Khởi động server:
bash
Sao chép mã
python manage.py runserver  
Truy cập ứng dụng:
Sau khi khởi động server, mở trình duyệt và truy cập http://localhost:8000/ để vào ứng dụng chính.
Để truy cập module quản trị, truy cập http://localhost:8000/admin và đăng nhập bằng tài khoản quản trị vừa tạo.
=======
# 📚 CSN-DA22TTA-PhamHuuLuan-BookSellingWeb
# Django Ebook Store

Ứng dụng web bán sách được xây dựng bằng Django 5, MySQL và Bootstrap 5.

Ứng dụng này cũng sử dụng một số gói bổ sung như:

django-crispy-forms

django-filter

pillow

easy-thumbnails

dj-database-url

Trong ứng dụng này, quản trị viên có thể quản lý sản phẩm và đơn hàng, trong khi khách hàng có thể đăng ký tài khoản, thêm sản phẩm vào giỏ hàng, và nhiều chức năng khác.

# 🚀 Cách chạy chương trình

1️⃣ Cài đặt môi trường

Yêu cầu Python >=3.8.

2️⃣ Clone repository về máy


git clone https://github.com/nguyenthanhhieu/csn-da22tta-nguyenthanhhieu-loctrungbinh.git  
cd csn-da22tta-nguyenthanhhieu-loctrungbinh  
3️⃣ Cài đặt các thư viện cần thiết

Chạy lệnh sau trong terminal:


pip install -r requirements.txt  
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

# 📂 Cấu trúc thư mục

👤 csn-da22tta-nguyenthanhhieu-loctrungbinh

 ├── 📂 setup               # Cài đặt chương trình, dữ liệu thử nghiệm
 ├── 📂 src                 # Chứa mã nguồn xử lý ảnh
 ├── 📂 progress-report     # Báo cáo tiến độ hàng tuần
 ├── 📂 thesis              # Tài liệu đồ án
 │   ├── 📂 doc            # Tài liệu Word
 │   ├── 📂 pdf            # Tài liệu PDF
 │   ├── 📂 abs            # Slide báo cáo (.ppt), video
 │   ├── 📂 refs           # Tài liệu tham khảo
 ├── README.md              # Mô tả tổng quan về đồ án
 ├── .gitignore             # File bỏ qua khi push lên GitHub


# 📞 Liên hệ

👤 Phạm Hữu Luân

📧 Email: luanphamhuu2004@example.com

📚 Trường Đại học Trà Vinh


>>>>>>> e56b6260210fbb20dded7704e576ec781cff2e7d
