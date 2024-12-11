from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home),
    # id used string type
    path("<int:id>/",views.post)
]