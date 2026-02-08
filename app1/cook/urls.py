from django.urls import path

from cook import views

urlpatterns = [
    path('application/', views.Application_C, name='application_c'),
    path('ordeapplicationr/create_application/', views.Create_application, name='create_application'),
    path('remaining/', views.Remaining_C, name='remaining'),
    path('remaining/food_change/', views.Food_change, name='food_change'),
    path('control/', views.Control_C, name='control'),
    path('control/ready_change/<int:id_order>/', views.Ready_change, name='ready_change'),
    path('accounting/', views.Accounting_C, name='accounting'),
]
