from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('job/', views.job, name='jobs'),
    path('create/', views.create_job_and_company, name='create_job'),
    path('apply/<int:job_id>/', views.apply, name='apply'),
    path('dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('worker/<int:id>/', views.worker_profile, name='worker_profile'),
    path('edit_resume/', views.edit_resume, name='edit_resume'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'), name='password_reset_complete'),
    path('chat/<int:worker_id>/', views.chat_with_worker, name='chat_with_worker'),
    path('worker/chats/', views.worker_chats, name='worker_chats'),
    path('worker/chat/<int:employer_id>/', views.chat_with_employer, name='chat_with_employer'),
    path('employer_profile', views.employer_profile, name='employer_profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('get_new_messages/', views.get_new_messages, name='get_new_messages'),
]
