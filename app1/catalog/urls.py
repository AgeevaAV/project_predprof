from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.Menu, name='menu'),
    path('detail/<int:id_card>/', views.Detail, name='detail'),
    path('box/', views.Box_, name='box'),
    path('box/<int:id_box>/', views.buybox, name='buybox'),
]
