# -*- coding: UTF-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from graphos.renderers.flot import LineChart
from graphos.sources.simple import SimpleDataSource
#from smop.runtime import zeros_,ones_ 
from myproject.predictor import GMtest
from myproject.scorefunction import scorefunction
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import UploadFileForm
from .models import Document
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os
from transformer_diagnose.settings import MEDIA_ROOT
from lxml import etree
import re
import time

# Create your views here.

import logging
logger = logging.getLogger(__name__)

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

def get_gas_data_xml_root():
    doc=Document.objects.first()
    gas_data_xml_path = os.path.join(MEDIA_ROOT ,doc.docfile.name)
    logger.info('gas_data_xml_path = %s'% gas_data_xml_path)
    xml_data= open(gas_data_xml_path, 'rb').read()
    return etree.XML(xml_data)
    

def get_tend_data(gas):
    root = get_gas_data_xml_root()
    date_list = root.xpath('/Response/ResultValue/DataTable/Rows/Row/ACQUISITIONTIME/text()')
    gas_data_list = root.xpath('/Response/ResultValue/DataTable/Rows/Row/'+gas+'/text()')
    
    return [[ long( time.strftime("%s" , time.strptime( re.sub(r'\.\d+$',r'',date_list[i]) ,'%Y-%m-%dT%H:%M:%S')) )*1000 ,value] for i,value in enumerate(gas_data_list) ]

def get_predict_data(gas):
    root = get_gas_data_xml_root()
    gas_data_list = root.xpath('/Response/ResultValue/DataTable/Rows/Row/'+gas+'/text()')
    logger.info('gas_data_list = %s'% gas_data_list)
    return [float(gas_data) for gas_data in gas_data_list]


def initial_score(request):
    a_list={
        "H2":0.005609,
        "C2H2":0.00001,
        "CO":0.00359,
        "CO2":0.00002,
        "TOTALHYDROCARBON":0.00492,
    }

    #data=get_data()
    data={}
    data["H2"]=[20.6, 1.71, 1.9, 3.1, 4.99, 5.36, 25.01, 4.87, 6.76, 8.91, 5.98 ]
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

@csrf_protect
def trans_gasdata(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['oil_xml_file'])
            #return HttpResponse('<script>alert("success")</script>')
            return HttpResponseRedirect(reverse('trans_gasdata'))
        else:
            return HttpResponse('invalid form')
    else:
        form=UploadFileForm()
    documents = Document.objects.all()
    logger.info('documents :%s'%documents)
    return render_to_response("chen/trans_gasdata.html",{'documents':documents},RequestContext(request))

def trans_para(request):
    return render_to_response("chen/trans_para.html",{})


def trans_record(request):
    return render_to_response("chen/trans_record.html",{})

def handle_uploaded_file(file):
    Document.objects.all().delete()
    xml_file=Document(docfile =file)
    xml_file.name=file.name
    xml_file.save()


def get_predict(quest):
    a_list={
        "H2":0.005609,
        "C2H2":0.00001,
        "CO":0.00359,
        "CO2":0.00002,
        "TOTALHYDROCARBON":0.00492,
    }

    class Predict(object):pass
    data=Predict()
    
    for key,value in a_list.items():
       data.__dict__['predict_'+key] =GMtest(get_predict_data(key),value)
    
    return render_to_response("predict.html",{'data':data})   

def get_tend(quest):
    data= [[u'时间',quest.POST["gas"] + u'含量']]
    data= data + get_tend_data(quest.POST["gas"])
    chart = LineChart(SimpleDataSource(data=data), html_id="line_chart")
    return render_to_response("tend.html",{'chart':chart}) 
