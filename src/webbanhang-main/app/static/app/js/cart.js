function handleCartAction(event, targetType) {
    // Kiểm tra nếu người dùng chưa đăng nhập
    if (user === "AnonymousUser") {
        var result = confirm("Bạn cần đăng nhập để thực hiện hành động này! Bạn muốn chuyển đến trang đăng nhập/đăng kí không?");
    
        if (result) {
            // Nếu người dùng nhấn OK, chuyển hướng đến trang login
            window.location.href = '/login/';
        } else {
            // Nếu người dùng nhấn Cancel, không làm gì
            event.preventDefault();  // Hủy hành động hiện tại (nếu có)
        }
        return;
    }

     // Nếu là nút "Thêm vào giỏ hàng", gọi hàm xử lý thêm sản phẩm vào giỏ
    if (targetType === 'addToCart') {
        //  kiểm tra trạng thái hết hàng
        const isOutOfStock = event.target.getAttribute('data-out-of-stock')==="true";
        if(isOutOfStock){
            alert("Sản phẩm đã hết hàng. Không thể thêm vào giỏ.");
            event.preventDefault();
            return;
        }

        // Nếu còn hàng, gọi hàm xử lý thêm sản phẩm vào giỏ
        var productId = event.target.getAttribute('data-product');
        var action = event.target.getAttribute('data-action');
        updateUserOrder(productId, action);
    } else if (targetType === 'cartIcon') {
        // Nếu là icon giỏ hàng, chuyển hướng đến trang giỏ hàng
        window.location.href = '/cart/';
    }
}

// Lắng nghe sự kiện cho các nút "Thêm vào giỏ hàng" và icon giỏ hàng
document.addEventListener('click', function(event) {
    // Kiểm tra nếu phần tử được nhấn là nút thêm vào giỏ hàng
    if (event.target.classList.contains('update-cart')) {
        handleCartAction(event, 'addToCart');  // Gọi hàm với targetType là 'add-to-cart'
    }
    // Kiểm tra nếu phần tử được nhấn là icon giỏ hàng
    else if (event.target.closest('.cart-icon')) {
        event.preventDefault(); // Ngăn chặn chuyển hướng của thẻ a
        handleCartAction(event, 'cartIcon');  // Gọi hàm với targetType là 'cart-icon'
    }
});


//lấy action và id sản phẩm gửi tới server (view.py) thông qua fetch request
function updateUserOrder(product_Id, action) {
    console.log("Bạn đã đăng nhập thành công!"); // In ra console thông báo rằng người dùng đã đăng nhập thành công.
    
    var url = '/update_item/' // Đặt URL đến endpoint '/update_item/' để xử lý yêu cầu cập nhật.

    fetch(url, { // Gọi hàm fetch để gửi yêu cầu đến server.
        method: 'POST', // Xác định phương thức HTTP là POST để gửi dữ liệu.
        headers: { // Cài đặt các headers cho yêu cầu.
            'Content-Type': 'application/json', // Đặt loại nội dung là JSON.
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({'productId': product_Id, 'action': action}) // Chuyển đổi đối tượng JavaScript thành chuỗi JSON để gửi trong body của yêu cầu, bao gồm `productId` và `action`.
    })
    .then((response) => { // Khi nhận được phản hồi từ server...
        return response.json() // Phân tích cú pháp phản hồi JSON.
    })
    .then((data) => { // Khi phân tích cú pháp thành công...
        console.log('data', data); // In ra dữ liệu nhận được từ server để kiểm tra kết quả.
        location.reload()
    })

    .catch((error) => {
        console.error('Error:', error);
    });
}


// var myCarousel = document.querySelector('#carouselExampleDark');
// var carousel = new bootstrap.Carousel(myCarousel, {
//   interval: 1000  // Thời gian chuyển slide là 1 giây (1000 mili giây)
// });
