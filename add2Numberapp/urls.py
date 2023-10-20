from django.urls import path
from . import views

urlpatterns = [
   path('', views.sum, name="sum"),
   path('findsum', views.findsum, name="findsum"),

]