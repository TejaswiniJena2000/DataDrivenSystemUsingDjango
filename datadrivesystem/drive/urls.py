from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/edit_profile/', views.edit_profile, name='edit_profile'),
    path('create_folder/', views.create_folder, name='create_folder'),
    path('view_folder/<int:folder_id>/', views.view_folder, name='view_folder'),
    path('edit_folder/<int:folder_id>/', views.edit_folder, name='edit_folder'),
    path('delete_folder/<int:folder_id>/', views.delete_folder, name='delete_folder'),

    # ...
]
