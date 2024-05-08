from django.shortcuts import render, redirect, get_object_or_404
from .models import Income
from .forms import IncomeForm  # Form untuk model Income
from django.http import JsonResponse

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

# Menambahkan data pendapatan
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data ke database
            return redirect('pemasukan')  # Kembali ke halaman pemasukan setelah berhasil menambah
    return redirect('pemasukan')  # Jika tidak valid, kembali ke halaman pemasukan

# Mengupdate data pendapatan
def update_income(request, id):
    income = get_object_or_404(Income, id=id)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('pemasukan')  # Kembali ke halaman pemasukan setelah berhasil update
    return redirect('pemasukan')  # Redirect jika tidak valid atau bukan POST

# Menghapus data pendapatan
def delete_income(request, id):
    income = get_object_or_404(Income, id=id)  # Dapatkan objek berdasarkan ID
    income.delete()  # Hapus objek dari database
    return redirect('pemasukan')  # Arahkan kembali ke halaman pemasukan setelah menghapus
