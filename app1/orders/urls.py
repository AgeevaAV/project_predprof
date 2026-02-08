from django.urls import path
from . import views

urlpatterns = [
    path('cart/add/<int:product_id>/<str:product_breakfast_or_lunch>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),

    path('increase/<int:item_id>/', views.increase_item, name='increase_item'),
    path('decrease/<int:item_id>/', views.decrease_item, name='decrease_item'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_quantity, name='update_quantity'),
    path('remove/<int:item_id>/', views.remove_item, name='remove_item'),
    path('order/', views.add_to_order, name='create_order'),
]