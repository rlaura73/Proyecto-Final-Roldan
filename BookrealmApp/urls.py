from django.urls import path
from BookrealmApp import views

urlpatterns = [
    path('', views.pag_inicio, name="PagInicio"),
    path('about/', views.pag_about, name="PagAbout")
]