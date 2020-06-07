from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum
from .models import ShoppingCart, Category, Regular_pizza, Sicilian_pizza, Topping, Sub, Pasta, Salad, Dinner_platter, User_order, Order, Order_count


def signin_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if not password == password2:
            return render(request, "signin.html", {"message": "Passwords don't match."})
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return render(request, "login.html", {"message": "Registered. You can log in now."})
    return render(request, "signin.html")


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse("admin_area"))
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {"msg": "Invalid credentials"})


def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"msg":None})
    context = {
        "user":request.user,
        "Categories": Category.objects.all()
    }
    return render(request, "index.html", context)


def admin_area(request):
    customer_orders = ShoppingCart.objects.filter(admin_comment="Initiated")
    if customer_orders:
        context = {
            "user": request.user,
            "customer_orders": customer_orders,
            "Categories": Category.objects.all()
        }
        return render(request, "admin_dashboard.html", context)


def manage_orders(request):
    customer_orders = ShoppingCart.objects.filter(admin_comment="Initiated")
    if customer_orders:
        context = {
            "user": request.user,
            "customer_orders": customer_orders,
            "Categories": Category.objects.all()
        }
        return render(request, "admin_dashboard.html", context)


def approve_order(request, order_id):
    ShoppingCart.objects.filter(id=order_id).update(admin_comment="Completed")
    return HttpResponseRedirect(reverse("admin_area"))


def menu(request, category):
    if category == 2:
        context = {
            "regularp": Regular_pizza.objects.all()
        }
        return render(request, "regular_pizza.html", context)
    elif category == 3:
        context = {
            "sicilianp": Sicilian_pizza.objects.all()
        }
        return render(request, "Sicilian_pizza.html", context)
    elif category == 4:
        context = {
            "toppings": Topping.objects.all()
        }
        return render(request, "topping.html", context)
    elif category == 5:
        context = {
            "subs": Sub.objects.all()
        }
        return render(request, "Sub.html", context)
    elif category == 6:
        context = {
            "pastas": Pasta.objects.all()
        }
        return render(request, "pasta.html", context)
    elif category == 7:
        context = {
            "salads": Salad.objects.all()
        }
        return render(request, "salad.html", context)
    elif category == 8:
        context = {
            "dinner_platters": Dinner_platter.objects.all()
        }
        return render(request, "dinner_platters.html", context)
    else:
        return "order should be made here in the index page"


def addtocart(request, name, price):
    current_user = request.user
    data = ShoppingCart()
    data.user_id = current_user.id
    data.is_ordered = "In cart"
    data.prod_name = name
    data.prod_qty = 1
    data.prod_price = price
    data.save()
    return HttpResponseRedirect(reverse("shoppingcart"))


def shoppingcart(request):
    current_user = request.user
    cartitems= ShoppingCart.objects.filter(user_id=current_user.id, is_ordered="In cart")
    if cartitems:
        # total = cartitems.aggregate(sum(prod_price))
        total = 0
        for dollars in cartitems:
            total += dollars.prod_price
            total = round(total, 2)
        context = {
            "cartitems":cartitems,
            "total":total
        }
        return render(request, "shopping_cart.html", context)
    else:
        return render(request, "empty_cart.html")


def removefromcart(request, item_id):
    ShoppingCart.objects.filter(id=item_id).delete()
    return HttpResponseRedirect(reverse("index"))


def place_order(request):
    current_user = request.user
    cartitems = ShoppingCart.objects.filter(user_id=current_user.id, is_ordered="In cart")
    if cartitems:
        # total = cartitems.aggregate(sum(prod_price))
        total = 0
        for dollars in cartitems:
            total += dollars.prod_price
            total = round(total, 2)
        # return HttpResponse(total)
        context = {
            "cartitems": cartitems,
            "total": total
        }
        return render(request, "confirm_order.html", context)
    else:
        return render(request, "empty_cart.html")


def order(request):
    current_user = request.user
    ShoppingCart.objects.filter(user_id=current_user.id).update(is_ordered="Pending", admin_comment="Initiated")
    return HttpResponseRedirect(reverse("index"))


def my_orders(request):
    current_user = request.user
    orders = ShoppingCart.objects.filter(user_id=current_user.id).filter(is_ordered="Pending")
    context = {
        "orders": orders
    }
    return render(request, "my_orders.html", context)


def logout_view(request):
    logout(request)
    return render(request, "login.html", {"msg": "logged out"})
