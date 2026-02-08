from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('recovery/', views.recovery, name='recovery'),
    path('register/', views.register, name='register'),
    path('profile/', views.Profile, name='profile'),
    path('your_orders/', views.Your_orders, name='your_orders'),
    path('your_orders/<int:id_ord>', views.Get_order, name='get_order'),
    path('your_orders/add_to_comment/<int:id_ord>/', views.Add_to_comment2, name='add_to_comment2'),
    path('your_orders/add_to_comment/<int:id_ord>', views.Add_to_comment, name='add_to_comment'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/comment', views.Comment, name='comment'),
    path('profile/comment/<int:id_comment>/', views.Delete_comment , name='delete_comment'),
    path('profile/personal_data', views.Personal_data, name='personal_data'),
    path('profile/allergens', views.Allergens, name='allergens'),
    path('profile/allergens/change_allergens', views.Change_allergens, name='change_allergens'),

]
