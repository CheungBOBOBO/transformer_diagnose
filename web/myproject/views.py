# coding: utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from graphos.renderers.flot import LineChart
from graphos.sources.simple import SimpleDataSource
# Create your views here.

def home(request):
    return render_to_response('hello_ext.html',{})

def oildata(request):
    data =  [
        ['Year', '销量', 'Expenses'],
        [2004, 1000, 400],
        [2005, 1170, 460],
        [2006, 660, 1120],
        [2007, 1030, 540]
    ]
    chart = LineChart(SimpleDataSource(data=data), html_id="line_chart")    
    return render_to_response('oildata.html',{'chart':chart,})
