from django.urls import path
from . import views

urlpatterns = [
    path(
        "fruits-students/",
        views.fruit_student_view,
        name="fruits_students"
    ),
]