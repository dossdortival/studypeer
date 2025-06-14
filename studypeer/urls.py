from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # Study Group URLs
    path('groups/', views.group_list, name='group_list'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('create/', views.create_group, name='create_group'),
    path('groups/<int:group_id>/edit/', views.update_group, name='update_group'),
    path('groups/<int:group_id>/delete/', views.delete_group, name='delete_group'), 

    # Membership URLs
    path('groups/<int:group_id>/join/', views.join_group, name='join_group'),
    path('groups/<int:group_id>/leave/', views.leave_group, name='leave_group'),

    # Dashboard URL    
    path('dashboard/', views.dashboard, name='dashboard'),

    # Profile URLs
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]