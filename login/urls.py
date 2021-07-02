from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("new_usr/", views.create_new, name="create_new"),
    path("forgot_usr/", views.forgot_pass, name="forgot_pass"),

]