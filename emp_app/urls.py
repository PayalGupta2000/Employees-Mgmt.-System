from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("view_all",views.view_all),
    path("add_emp",views.add_emp),
]