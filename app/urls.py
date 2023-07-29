from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name="signin"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('log_out/', views.log_out, name="log_out"),
    path('delet/<str:name>/', views.deletTask, name="delet"),
    path('complet/<str:name>/', views.completTask, name="complet")
]
