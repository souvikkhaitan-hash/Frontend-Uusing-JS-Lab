from django.urls import path
from . import views

urlpatterns = [
    path("", views.base_layout_demo, name="layout_demo"),
]