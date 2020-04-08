from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("add", views.add, name="add"),
    path("order", views.order, name="order"),
    path("cart", views.cart, name="cart"),
    path("purchase", views.purchase, name="purchase")
]
