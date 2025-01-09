# Django ebook-store

An website bookstore app made using django 5, mysql and bootstrap 5.
This app also uses several other packages like -

- django-crispy-forms
- django-filter
- pillow
- easy-thumbnails
- dj-database-url

In this app admin can manage products and orders and a customer can simply register, add items to cart...

To run this app on your local machine you can simply follow the instructions given below.

To install dependencies you can run
```
pip install -r requirements.txt
```

To create superuser run this command:

```
python manage.py createsuperuser
```

and then enter your username, email and password.

To make migrations :

```
python manage.py migrate
```

To run server :

```
python manage.py runserver
```

After starting server go to your web browser and visit http://localhost:8000/ and for admin module visit http://localhost:8000/admin and login using superuser credentials.
