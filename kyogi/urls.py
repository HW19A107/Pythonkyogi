from django.urls import path

from . import views

urlpatterns = [
    path('login',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register', views.AccountRegistration.as_view(), name='register'),
    path("home",views.home,name="home"),
    path("check",views.totals),
    path('graph',views.graph.as_view(),name='graph')
]