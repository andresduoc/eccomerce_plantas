from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarIndex),
    path('AgregarProducto',views.AgregarProducto,name='AgregarProducto'),
    path('SubirAgregarProducto',views.SubirAgregarProducto,name='SubirAgregarProducto'),
    path('cargarEditarProducto/<id>',views.cargarEditarProducto),
    path('editarProducto',views.editarProducto),
    path('QuitarProducto/<id>',views.QuitarProducto,name='QuitarProducto')
]