from django.db import models

class Income(models.Model):
    tanggal = models.DateField()
    jumlah = models.DecimalField(max_digits=100, decimal_places=0)
    deskripsi = models.CharField(max_length=255)
    # sumber = models.CharField(max_length=100)