from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin_here/', views.admin_here, name='admin_here'),
    # path('logout/', views.logout_user, name='logout'),

]