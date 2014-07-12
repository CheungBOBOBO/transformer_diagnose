#!/usr/bin/python
# Autogenerated with SMOP version 0.25
# /usr/local/bin/smop -o GMtest.py GMtest.m
from __future__ import division
import numpy as np
from smop.runtime import *
from lxml import etree
from  numpy.linalg.linalg import inv as inv_
from math import exp as exp_

def GMtest(data,a,nargout=1,):
    #Shuju1=xlsread_('data2.xlsx','B2:B12')
    n=len(data)
    Shuju1=np.ndarray(shape=(n , 1),
        buffer=np.array( [ float(value)   for value in data]),
        dtype=float,)

    Shuju2=zeros_(n,1)
    Y=zeros_(n,1)
    Z=zeros_(n - 1,1)
    B=zeros_(n - 1,2)
    #C=ones_(n - 1,1)
    C_temp=ones_(n - 1,1)
    C=zeros_(n - 1,1)
    C=-C_temp

    D=zeros_(n - 1,2)
    A=zeros_(2,1)
    X=zeros_(n - 1,1)
    Shuju2[0,0]=Shuju1[0,0]
    #a=0.005609
    for i in range(1,n):
        Shuju2[i,0]=a * Shuju1[i,0] + (1 - a) * Shuju2[i - 1,0]
    Y[0,0]=Shuju2[0,0]
    for i in range(1,n):
        Y[i,0]=Shuju2[i,0] + Y[i - 1,0]
    for i in range(0,n - 1):
        Z[i,0]=0.5 * Y[i,0] + 0.5 * Y[i + 1,0]
    for i in range(0,n - 1):
        X[i,0]=Shuju2[i + 1,0]
    B[:,0]=Z.T
    B[:,1]=C.T
    D=- B
    print "D:",D
    print    "1.",D.T.dot( D )
    A=inv_(D.T.dot( D)).dot( D.T).dot( X)
    a=A[0,0]
    b=A[1,0]
    m=Y[0,0]
    y=(1 - exp_(a)) * (m - b / a) * exp_(- a * (n + 1))
    x=(y - 0.99 * X[n - 2,0]) / 0.01
    #xlswrite_('data2.xlsx',x,'sheet1','B15:B15')
    #return x,delta_()
    return x

def handle_transformer_air_data(xml_data):
    atrribute_list={
        'H2':0.005609,
        'C2H2':0.00001,
        'CO':0.00359,
        "CO2":0.00002,
        'TOTALHYDROCARBON':0.00492,
        }
    root=etree.XML(xml_data) 
    return [ GMtest(root.xpath('/Response/ResultValue/DataTable/Rows/Row[position()<12]/'+key+'/text()'),value) 
        for key,value  in atrribute_list.items() ]

if __name__ =='__main__' :

    data=[20.6, 1.71, 1.9, 3.1, 4.99, 5.36, 25.01, 4.87, 6.76, 8.91, 5.98 ]
    predict_data1=GMtest(data,0.005609)
    print "GMtest H2 : ",predict_data1

    filename='../../test_data/oildata.xml'
    xml_data= open(filename, 'rb').read()
    predict_datas = handle_transformer_air_data(xml_data)
    print 'predict_data : \n',predict_datas