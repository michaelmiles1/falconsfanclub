from django.urls import path
from . import views

urlpatterns = [
    path("", views.roster_index, name="roster_index")
]
