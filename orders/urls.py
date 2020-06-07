from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("signin", views.signin_view, name="signin"),
    path("menu/<int:category>", views.menu, name="menu"),
    path("addtocart/<str:name>/<str:price>", views.addtocart, name="addtocart"),
    path("shoppingcart", views.shoppingcart, name="shoppingcart"),
    path("removefromcart/<int:item_id>", views.removefromcart, name="removefromcart"),
    path("place_order", views.place_order, name="place_order"),
    path("my_orders", views.my_orders, name="my_orders"),
    path("admin_area", views.admin_area, name="admin_area"),
    path("manage_orders", views.manage_orders, name="manage_orders"),
    path("order", views.order, name="order"),
    path("approve_order/<int:order_id>", views.approve_order, name="approve_order"),
    path("logout", views.logout_view, name="logout")
]