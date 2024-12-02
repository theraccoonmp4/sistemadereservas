from sistemadereservas import views
from django.urls import path

urlpatterns = [
    path('sobre/', views.sobre, name="sobre"),
    path('minhainfo/', views.minhainfo, name="minhainfo"),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
]