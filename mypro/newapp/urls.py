from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Halaman utama
    path('pemasukan/', views.pemasukan, name='pemasukan'), 
    path('pengeluaran/', views.pengeluaran, name='pengeluaran'), 
    path('add/', views.add_income, name='add'),  # Menambah data ke database
    path('update/<int:id>/', views.update_income, name='update'),  # Mengupdate data
    path('delete/<int:id>/', views.delete_income, name='delete'),  # Menghapus data
]
