from django.shortcuts import render, redirect, get_object_or_404
from .models import Income
from .forms import IncomeForm  # Form untuk model Income
from django.http import JsonResponse
from django.contrib import messages

# Menampilkan daftar data
def index(request):
    incomes = Income.objects.all()  # Mengambil semua data pendapatan
    return render(request, 'index.html', {'incomes': incomes})

def pemasukan(request):
    incomes = Income.objects.all()  # Mengambil semua data pendapatan
    form = IncomeForm()  # Form untuk menambahkan pendapatan
    return render(request, 'pemasukan.html', {'incomes': incomes, 'form': form})

def pengeluaran(request):
    form = IncomeForm()  # Form untuk menambahkan pendapatan
    return render(request, 'pengeluaran.html', {'form': form})

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data ke database
            messages.success(request, "Berhasil tambah data!")  # Pesan untuk SweetAlert
            return redirect('pemasukan')  # Kembali ke halaman pemasukan
    return redirect('pemasukan')  # Jika tidak valid, kembali ke halaman pemasukan

def update_income(request, id):
    income = get_object_or_404(Income, id=id)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()  # Simpan perubahan ke database
            messages.success(request, "Berhasil update data!")  # Pesan untuk SweetAlert
            return redirect('pemasukan')  # Kembali ke halaman pemasukan
    return redirect('pemasukan')  # Redirect jika bukan POST

def delete_income(request, id):
    income = get_object_or_404(Income, id=id)
    income.delete()  # Hapus objek
    messages.success(request, "Berhasil hapus data!")  # Pesan untuk SweetAlert
    return redirect('pemasukan')  # Kembali ke halaman pemasukan setelah berhasil dihapus
