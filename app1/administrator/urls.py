from django.urls import path

from administrator import views

urlpatterns = [
    path('application/', views.Application_A, name='application'),
    path('application/approve_application/<int:id_application>/', views.Approve_application, name='approve_application'),
    path('application/reject_application/<int:id_application>/', views.Reject_application, name='reject_application'),

    path('statistics/', views.Statistics_A, name='statistics'),
    path('reports/', views.Reports_A, name='reports'),
]
