from django.urls import path
from . import views

urlpatterns = [
    path('register_student/', views.register_student, name='register_student'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('student_details/', views.student_details, name='student_details'),
    path('update_student/<int:pk>/', views.update_student, name='update_student'),

]