from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ask/', views.post_question, name='post_question'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),

]
