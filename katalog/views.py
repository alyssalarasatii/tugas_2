from django.shortcuts import render
from katalog.models import CatalogItem
from tugas_2.katalog.models import CatalogItem

# TODO: Create your views here.
def s_katalog(request):
    barang_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': barang_katalog,
        'nama': 'Alyssa Larasati',
        'student_id': '2106656125'
    }
    return render(request, "katalog.html",context)