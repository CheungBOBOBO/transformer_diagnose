# coding: utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from graphos.renderers.flot import LineChart
from graphos.sources.simple import SimpleDataSource
#from smop.runtime import zeros_,ones_ 
from myproject.predictor import GMtest
from myproject.scorefunction import scorefunction
# Create your views here.

import logging
logger = logging.getLogger(__name__)

logger.debug("scorefunction ???????")
def home(request):
    #return render_to_response('hello_ext.html',{})
    return render_to_response('index.html',{}) 

def oildata(request):
    data =  [
        ['Year', '销量', 'Expenses'],
        [2004, 1000, 400],
        [2005, 1170, 460],
        [2006, 660, 1120],
        [2007, 1030, 540]
    ]
    chart = LineChart(SimpleDataSource(data=data), html_id="line_chart")    
    #return HttpResponse("11");
    return render_to_response('oildata.html',{'chart':chart,})

def get_data():
    data={}
    data["H2"]=[20.6, 1.71, 1.9, 3.1, 4.99, 5.36, 25.01, 4.87, 6.76, 8.91, 5.98 ]
    return data

def initial_score(request):
    a_list={
        "H2":0.005609,
        "C2H2":0.00001,
        "CO":0.00359,
        "CO2":0.00002,
        "TOTAL_HYDROCARBON":0.00492,
    }

    data=get_data()
    predict_data={(key,GMtest(value,a_list[key])) for key,value in data.items() }

    input_data=[4.,0.,590.,1125.,12.,2.,0.445,0.1,1.344,42.,12.,21000.,0.0113,95.,95.]
    R5,I,H=scorefunction(input_data)
    #result=R5.tolist()[0]+I.tolist()[0]+[H]
    result=R5.tolist()[0]
    tmp=[["2014."+str(id)]+result for id in range(10) ]
    logger.info(result)
    title=["时间","1","2",'3','4','5']
    tmp=[title]+tmp
    
    chart = LineChart(SimpleDataSource(data=tmp), html_id="line_chart")
    return render_to_response('oildata.html',{'chart':chart,})
def threshold(request):
    return render_to_response("chen/threshold.html",{})
def trans_dc_para(request):
    return render_to_response("chen/trans_dc_para.html",{})
def trans_estimate(request):
    return render_to_response("chen/trans_estimate.html",{})
def trans_gasdata(request):
    return render_to_response("chen/trans_gasdata.html",{})
def trans_para(request):
    return render_to_response("chen/trans_para.html",{})
def trans_record(request):
    return render_to_response("chen/trans_record.html",{})

