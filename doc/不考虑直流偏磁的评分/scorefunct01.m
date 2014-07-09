function [R5,I,H]=scorefunct01() %历史状态评分
Input_data=xlsread('datawithoutbias.xlsx','B2:B20');%读取原始数据，数据顺序对应参数需求表,220kV
lower_data=zeros(13);%隶属度函数下限值存储矩阵
upper_data=zeros(13);%隶属度函数上限值存储矩阵
lower_data=xlsread('datawithoutbias.xlsx','E2:E14');%状态量的下限值
upper_data=xlsread('datawithoutbias.xlsx','F2:F14');%状态量的上限值
%---------最底层评分
s(1)=0;%H2（单位：10^-6）的评分
a1=Input_data(1);%H2对应的数值
al1=lower_data(1);%H2对应的隶属度函数下限值
au1=upper_data(1);%H2对应的隶属度函数上限值
if a1<al1 
    s(1)=1; 
else if a1<au1
        s(1)=(au1-a1)/(au1-al1);
    else s(1)=0;
    end
end
s(2)=0;%C2H2（单位：10^-6）的评分
a2=Input_data(2);%C2H2对应的数值
al2=lower_data(2);%C2H2对应的隶属度函数下限值
au2=upper_data(2);%C2H2对应的隶属度函数上限值
if a2<au2 
    s(2)=(au2-a2)/(au2-al2); 
else s(2)=0;    
end
s(3)=0;%CO（单位：10^-6）的评分
a3=Input_data(3);
al3=lower_data(3);
au3=upper_data(3);
if a3<au3 
    s(3)=(au3-a3)/(au3-al3); 
else s(3)=0;    
end
s(4)=0;%CO2（单位：10^-6）的评分
a4=Input_data(4);
al4=lower_data(4);
au4=upper_data(4);
if a4<au4 
    s(4)=(au4-a4)/(au4-al4); 
else s(4)=0;    
end
s(5)=0;%总烃（单位：10^-6）的评分
a5=Input_data(5);
al5=lower_data(5);
au5=upper_data(5);
if a5<al5 
    s(5)=1; 
else if a5<au5
        s(5)=(au5-a5)/(au5-al5);
    else s(5)=0;
    end
end
s(6)=0;%绝缘吸收比的评分
a6=Input_data(6);
al6=lower_data(6);
au6=upper_data(6);
if a6<al6 
    s(6)=0; 
else if a6<au6
        s(6)=(a6-al6)/(au6-al6);
    else s(6)=1;
    end
end
s(7)=0;%绕组介质损耗因数（单位：%）的评分
a7=Input_data(7);
al7=lower_data(7);
au7=upper_data(7);
if a7<al7 
    s(7)=1; 
else if a7<au7
        s(7)=(au7-a7)/(au7-al7);
    else s(7)=0;
    end
end
s(8)=0;%油介质损耗因数（单位：%）的评分
a8=Input_data(8);
al8=lower_data(8);
au8=upper_data(8);
if a8<au8 
    s(8)=(au8-a8)/(au8-al8); 
else s(8)=0;    
end
s(9)=0;%绕组直流电阻相间差（单位：%）的评分
a9=Input_data(9);
al9=lower_data(9);
au9=upper_data(9);
if a9<al9 
    s(9)=1; 
else if a9<au9
        s(9)=(au9-a9)/(au9-al9);
    else s(9)=0;
    end
end
s(10)=0;%油击穿电压（单位：kV）的评分
a10=Input_data(10);
al10=lower_data(10);
au10=upper_data(10);
if a10<au10
    s(10)=a10/au10; 
else s(10)=1;    
end
s(11)=0;%油中微水含量（单位：mg/L）的评分
a11=Input_data(11);
al11=lower_data(11);
au11=upper_data(11);
if a11<au11 
    s(11)=(au11-a11)/au11;
else s(11)=0;
end
s(12)=0;%套管主屏绝缘电阻（单位：MΩ）的评分
a12=Input_data(12);
al12=lower_data(12);
au12=upper_data(12);
if a12<al12 
    s(12)=0; 
else if a12<au12
        s(12)=(a12-al12)/(au12-al12);
    else s(12)=1;
    end
end
s(13)=0;%铁芯接地电流（单位：A）的评分
a13=Input_data(13);
al13=lower_data(13);
au13=upper_data(13);
if a13<al13 
    s(13)=1; 
else if a13<au13
        s(13)=(au13-a13)/(au13-al13);
    else s(13)=0;
    end
end
s(14)=Input_data(14)/100;s(15)=Input_data(15)/100;
%运行工况s14、家族缺陷s15由于没有定量化的规程规定，并且基本信息占的权重较小，因此采取专家打分的方式确定得分，直接输入专家评分（百分制，但为了后续处理方便，需要进行归一化）
%——————各个参量的隶属度函数
for i=1:15
    if s(i)<0.2 
        t1(i)=0;t2(i)=0;t3(i)=0;t4(i)=0;t5(i)=1;
    else if s(i)<0.4
            t1(i)=0;t2(i)=0;t3(i)=0;t4(i)=5*s(i)-1;t5(i)=-5*s(i)+2;
        else if s(i)<0.6
                t1(i)=0;t2(i)=0;t3(i)=5*s(i)-2;t4(i)=-5*s(i)+3;t5(i)=0;
            else if s(i)<0.85
                    t1(i)=0;t2(i)=4*s(i)-2.4;t3(i)=-4*s(i)+3.4;t4(i)=0;t5(i)=0;
                else if s(i)<1
                       t1(i)=(20*s(i)-17)/3;t2(i)=(20-20*s(i))/3;t3(i)=0;t4(i)=0;t5(i)=0; 
                    else  t1(i)=1;t2(i)=0;t3(i)=0;t4(i)=0;t5(i)=0;
                    end
                end
            end
        end
    end
end
S1=[t1(1) t2(1) t3(1) t4(1) t5(1);t1(2) t2(2) t3(2) t4(2) t5(2);t1(3) t2(3) t3(3) t4(3) t5(3);t1(4) t2(4) t3(4) t4(4) t5(4);t1(5) t2(5) t3(5) t4(5) t5(5)];%在线监测量的隶属矩阵
S2=[t1(6) t2(6) t3(6) t4(6) t5(6);t1(7) t2(7) t3(7) t4(7) t5(7);t1(8) t2(8) t3(8) t4(8) t5(8);t1(9) t2(9) t3(9) t4(9) t5(9);t1(10) t2(10) t3(10) t4(10) t5(10);t1(11) t2(11) t3(11) t4(11) t5(11);t1(12) t2(12) t3(12) t4(12) t5(12);t1(13) t2(13) t3(13) t4(13) t5(13)];%电气试验信息量的隶属矩阵
S3=[t1(14) t2(14) t3(14) t4(14) t5(14);t1(15) t2(15) t3(15) t4(15) t5(15)];%基本信息的隶属矩阵
%%———————评估系统结构权重系数
%——————在线监测量权重系数矩阵
a1=0.165;a2=0.24;a3=0.19;a4=0.165;a5=0.24;
A=[a1 a2 a3 a4 a5];

%——————电气试验信息量权重系数矩阵
b1=0.1036;b2=0.1321;b3=0.1321;b4=0.1464;b5=0.1321;b6=0.1321;b7=0.1179;b8=0.1036;
B=[b1 b2 b3 b4 b5 b6 b7 b8];

%——————基本信息量权重系数矩阵
c1=0.55;c2=0.45;
C=[c1 c2];

%——————第二层权重系数矩阵(在线监测量、电气试验信息量、基本信息量)
e1=0.4;e2=0.35;e3=0.25;
E=[e1 e2 e3];

%%——————第二层隶属矩阵
R1=A*S1;%在线监测量的隶属矩阵，为一个1*5的行向量
R2=B*S2;%电气试验信息量的隶属矩阵，为一个1*5的行向量
R3=C*S3;%基本信息量的隶属矩阵，为一个1*5的行向量
S5=[R1;R2;R3];%第二层的隶属矩阵
S5
%——————历史状态、当前状态、预测状态得分
R5=E*S5;%状态隶属矩阵（历史状态、当前状态、预测状态分别进行计算）
R5
G=[93;73;50.5;30.5;10];%将5级评分方案中得到的5个评分区间取中间值形成该矩阵
I=R5*G;%得到（历史、当前、预测）状态的得分
if I<21
    H=0;
else if I<41
        H=1;
    else if I<61
            H=2;
        else if I<86
                H=3;
            else H=4;
            end
        end
    end
end
xlswrite('resultwithoutbias.xlsx',R5,'sheet1','B2:F2');
xlswrite('resultwithoutbias.xlsx',I,'sheet1','G2:G2');
xlswrite('resultwithoutbias.xlsx',H,'sheet1','H2:H2');
end
