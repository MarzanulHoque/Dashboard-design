from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


def index(request):
    products = None
    categories = Category.get_all_categories()

    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':

        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        # validations
        error_message = None
        if not first_name:
            error_message = "First name required"

        elif len(first_name) < 4:
            error_message = "first name Must be 4 Character Long"

        elif not last_name:
            error_message = "Last name Required"
        elif len(last_name) < 4:
            error_message = "last name must be 4 character"
        elif not phone:
            error_message = "Phone Number Required"
        elif len(phone) < 10:
            error_message = "Phone number must be 10 Character"
        elif not email:
            error_message = "Email Required"
        elif not password:
            error_message = "password required"
        elif len(password) < 6:
            error_message = "password Must  be 6 Character Long"

        if not error_message:

            customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)

            customer.register()
            return redirect("homepage")
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
