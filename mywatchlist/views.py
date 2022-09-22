from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_mywatchlist(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
        'list_watch': data_watchlist,
        'nama': 'Alyssa Larasati',
        'student_id': 2106656125,
    }
    return render(request, "mywatchlist.html",context)

def show_xml(request):
    data_xml = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_xml), content_type="application/xml")

def show_json(request):
    data_Json = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_Json), content_type="application/json")

def show_json_by_id(request):
    data_req_id = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_req_id), content_type="application/json")

def show_xml_by_id(request):
    data_req_id = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_req_id), content_type="application/xml")


