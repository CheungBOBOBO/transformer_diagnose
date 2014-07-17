# Autogenerated with SMOP version 0.25
# /usr/local/bin/smop -o ../../web/myproject/socrefunction.py scorefunct02.m
from __future__ import division
import numpy as np
from  numpy.linalg.linalg import inv as inv_
from math import exp as exp_
from math import log as log_
from smop.runtime import *

lower_data=np.ndarray(  shape=(13,1),
                        buffer=np.array([10,0,0,0,20,1,0.5,0,1,0,0,10000,0.1]),
                        dtype=float,)

upper_data=np.ndarray(  shape=(13,1),
                        buffer=np.array([150,5,400,4500,150,1.3,0.8,4,2,35,25,20000,0.3]),
                        dtype=float,)

def scorefunction(Input_data,nargout=1):
    #Input_data=xlsread_('datawithoutbias.xlsx','C2:C20')
    #lower_data=zeros_(13)
    #upper_data=zeros_(13)
    #lower_data=xlsread_('datawithoutbias.xlsx','E2:E14')
    #upper_data=xlsread_('datawithoutbias.xlsx','F2:F14')
    s=[0]*15
    a1=Input_data[0]
    al1=lower_data[0]
    au1=upper_data[0]
    if a1 < al1:
        s[0]=1
    else:
        if a1 < au1:
            s[0]=(au1 - a1) / (au1 - al1)
        else:
            s[0]=0
    a2=Input_data[1]
    al2=lower_data[1]
    au2=upper_data[1]
    if a2 < au2:
        s[1]=(au2 - a2) / (au2 - al2)
    else:
        s[1]=0
    a3=Input_data[2]
    al3=lower_data[2]
    au3=upper_data[2]
    if a3 < au3:
        s[2]=(au3 - a3) / (au3 - al3)
    else:
        s[2]=0
    a4=Input_data[3]
    al4=lower_data[3]
    au4=upper_data[3]
    if a4 < au4:
        s[3]=(au4 - a4) / (au4 - al4)
    else:
        s[3]=0
    a5=Input_data[4]
    al5=lower_data[4]
    au5=upper_data[4]
    if a5 < al5:
        s[4]=1
    else:
        if a5 < au5:
            s[4]=(au5 - a5) / (au5 - al5)
        else:
            s[4]=0
    a6=Input_data[5]
    al6=lower_data[5]
    au6=upper_data[5]
    if a6 < al6:
        s[5]=0
    else:
        if a6 < au6:
            s[5]=(a6 - al6) / (au6 - al6)
        else:
            s[5]=1
    a7=Input_data[6]
    al7=lower_data[6]
    au7=upper_data[6]
    if a7 < al7:
        s[6]=1
    else:
        if a7 < au7:
            s[6]=(au7 - a7) / (au7 - al7)
        else:
            s[6]=0
    a8=Input_data[7]
    al8=lower_data[7]
    au8=upper_data[7]
    if a8 < au8:
        s[7]=(au8 - a8) / (au8 - al8)
    else:
        s[7]=0
    a9=Input_data[8]
    al9=lower_data[8]
    au9=upper_data[8]
    if a9 < al9:
        s[8]=1
    else:
        if a9 < au9:
            s[8]=(au9 - a9) / (au9 - al9)
        else:
            s[8]=0
    a10=Input_data[9]
    al10=lower_data[9]
    au10=upper_data[9]
    if a10 < au10:
        s[9]=a10 / au10
    else:
        s[9]=1
    a11=Input_data[10]
    al11=lower_data[10]
    au11=upper_data[10]
    if a11 < au11:
        s[10]=(au11 - a11) / au11
    else:
        s[10]=0
    a12=Input_data[11]
    al12=lower_data[11]
    au12=upper_data[11]
    if a12 < al12:
        s[11]=0
    else:
        if a12 < au12:
            s[11]=(a12 - al12) / (au12 - al12)
        else:
            s[11]=1
    a13=Input_data[12]
    al13=lower_data[12]
    au13=upper_data[12]
    if a13 < al13:
        s[12]=1
    else:
        if a13 < au13:
            s[12]=(au13 - a13) / (au13 - al13)
        else:
            s[12]=0
    s[13]=Input_data[13] / 100
    s[14]=Input_data[14] / 100
    t1=[None]*15
    t2=[None]*15
    t3=[None]*15
    t4=[None]*15
    t5=[None]*15
    for i in range(0,15):
        if s[i] < 0.2:
            t1[i]=0
            t2[i]=0
            t3[i]=0
            t4[i]=0
            t5[i]=1
        else:
            if s[i] < 0.4:
                t1[i]=0
                t2[i]=0
                t3[i]=0
                t4[i]=5 * s[i] - 1
                t5[i]=- 5 * s[i] + 2
            else:
                if s[i] < 0.6:
                    t1[i]=0
                    t2[i]=0
                    t3[i]=5 * s[i] - 2
                    t4[i]=- 5 * s[i] + 3
                    t5[i]=0
                else:
                    if s[i] < 0.85:
                        t1[i]=0
                        t2[i]=4 * s[i] - 2.4
                        t3[i]=- 4 * s[i] + 3.4
                        t4[i]=0
                        t5[i]=0
                    else:
                        if s[i] < 1:
                            t1[i]=(20 * s[i] - 17) / 3
                            t2[i]=(20 - 20 * s[i]) / 3
                            t3[i]=0
                            t4[i]=0
                            t5[i]=0
                        else:
                            t1[i]=1
                            t2[i]=0
                            t3[i]=0
                            t4[i]=0
                            t5[i]=0
    #S1=matlabarray([t1[1],t2[1],t3[1],t4[1],t5[1],t1[2],t2[2],t3[2],t4[2],t5[2],t1[3],t2[3],t3[3],t4[3],t5[3],t1[4],t2[4],t3[4],t4[4],t5[4],t1[5],t2[5],t3[5],t4[5],t5[5]])
    #S2=matlabarray([t1[6],t2[6],t3[6],t4[6],t5[6],t1[7],t2[7],t3[7],t4[7],t5[7],t1[8],t2[8],t3[8],t4[8],t5[8],t1[9],t2[9],t3[9],t4[9],t5[9],t1[10],t2[10],t3[10],t4[10],t5[10],t1[11],t2[11],t3[11],t4[11],t5[11],t1[12],t2[12],t3[12],t4[12],t5[12],t1[13],t2[13],t3[13],t4[13],t5[13]])
    #S3=matlabarray([t1[14],t2[14],t3[14],t4[14],t5[14],t1[15],t2[15],t3[15],t4[15],t5[15]])
    t_list = [t1,t2,t3,t4,t5]
    '''S1=np.matrix([[item[0] for item in t_list ] , 
        [item[1] for item in t_list ],
        [item[2] for item in t_list ],
        [item[3] for item in t_list ],
        [item[4] for item in t_list ]] )
    '''
    S1=np.matrix([[item[x] for item in t_list ] for x in range(0,5)]) 
    S2=np.matrix([[item[x] for item in t_list ] for x in range(5,13)]) 
    S3=np.matrix([[item[x] for item in t_list ] for x in range(13,15)]) 
    
    a1=0.165
    a2=0.24
    a3=0.19
    a4=0.165
    a5=0.24
    A=np.matrix([a1,a2,a3,a4,a5])
    b1=0.1036
    b2=0.1321
    b3=0.1321
    b4=0.1464
    b5=0.1321
    b6=0.1321
    b7=0.1179
    b8=0.1036
    B=np.matrix([b1,b2,b3,b4,b5,b6,b7,b8])
    c1=0.55
    c2=0.45
    C=np.matrix([c1,c2])
    e1=0.4
    e2=0.35
    e3=0.25
    E=np.matrix([e1,e2,e3])
    R1=A * S1
    R2=B * S2
    R3=C * S3
    S5=np.matrix([R1.tolist()[0],R2.tolist()[0],R3.tolist()[0]])
    R5=E * S5
    print 'R5=',R5
    G=np.matrix([93.,73.,50.5,30.5,10.])
    I=R5 * G.T
    if I < 21:
        H=0
    else:
        if I < 41:
            H=1
        else:
            if I < 61:
                H=2
            else:
                if I < 86:
                    H=3
                else:
                    H=4
    #xlswrite_('resultwithoutbias.xlsx',R5,'sheet1','B3:F3')
    #xlswrite_('resultwithoutbias.xlsx',I,'sheet1','G3:G3')
    #xlswrite_('resultwithoutbias.xlsx',H,'sheet1','H3:H3')
    print 'R5=',R5,"I=",I,'H=',H
    return R5,I,H

if __name__ == '__main__':
    print  'caculate without bias' 
    input_data=[4.,0.,590.,1125.,12.,2.,0.445,0.1,1.344,42.,12.,21000.,0.0113,95.,95.]
    scorefunction(input_data)

