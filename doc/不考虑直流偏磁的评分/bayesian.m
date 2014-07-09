function [R5,I,H]=bayesian() %��Ҷ˹���緽����֮ǰ������״̬�����ۺ�����
%��������Ƶı�ʾ��ʽ��������������ʷ״̬H1Ϊ0����ǰ״̬H2Ϊ1��Ԥ��״̬H3Ϊ2�����������Ϊ012
Input_data1=xlsread('resultwithoutbias.xlsx','H2:H4');%������ģ�͸�������ʷ״̬����ǰ״̬��Ԥ��״̬�����ֵȼ�
H1=Input_data1(1);%��ʷ״̬
H2=Input_data1(2);%��ǰ״̬
H3=Input_data1(3);%Ԥ��״̬
m=125-(25*H1+5*H2+H3);%�������תΪʮ����
Input_data2=xlsread('sample.xlsx','E3:I127');%ѵ����������
M=zeros(125,5);
for i=1:125
    for j=1:5
        M(i,j)=Input_data2(i,j);
    end
end
%H��ȡֵ��Χ��0~124����Ӧ��125�����
Sa=(1+M(m,1))/(1+M(m,1)+1+M(m,2)+1+M(m,3)+1+M(m,4)+1+M(m,5));
Sa
Sb=(1+M(m,2))/(1+M(m,1)+1+M(m,2)+1+M(m,3)+1+M(m,4)+1+M(m,5));
Sb
Sc=(1+M(m,3))/(1+M(m,1)+1+M(m,2)+1+M(m,3)+1+M(m,4)+1+M(m,5));
Sc
Sd=(1+M(m,4))/(1+M(m,1)+1+M(m,2)+1+M(m,3)+1+M(m,4)+1+M(m,5));
Sd
Se=(1+M(m,5))/(1+M(m,1)+1+M(m,2)+1+M(m,3)+1+M(m,4)+1+M(m,5));
Se
A=[Sa Sb Sc Sd Se];
G=[93;73;50.5;30.5;10];
T_score=A*G;
T_max=max(A);%ѡȡ������ֵ��Ϊ���Ƽ�ֱ��ƫ�ŵı�ѹ��״̬�������
a=Sa;
b=Sb;
c=Sc;
d=Sd;
e=Se;
%�޸�ѵ����������
if a==T_max
    M(m,1)=M(m,1)+1;
else if b==T_max
        M(m,2)=M(m,2)+1;
    else if c==T_max
            M(m,3)=M(m,3)+1;
        else if d==T_max
                M(m,4)=M(m,4)+1;
            else M(m,5)=M(m,5)+1;
            end
        end
    end
end
if T_score<21
    T_Status=0;
else if T_score<41
        T_Status=1;
    else if T_score<61
            T_Status=2;
        else if T_score<86
                T_Status=3;
            else T_Status=4;
            end
        end
    end
end
Input_data2=M;
xlswrite('resultwithoutbias.xlsx',Sa,'sheet1','B5:B5');
xlswrite('resultwithoutbias.xlsx',Sb,'sheet1','C5:C5');
xlswrite('resultwithoutbias.xlsx',Sc,'sheet1','D5:D5');
xlswrite('resultwithoutbias.xlsx',Sd,'sheet1','E5:E5');
xlswrite('resultwithoutbias.xlsx',Se,'sheet1','F5:F5');
xlswrite('resultwithoutbias.xlsx',T_score,'sheet1','G5:G5');
xlswrite('resultwithoutbias.xlsx',T_Status,'sheet1','H5:H5');
xlswrite('sample.xlsx',Input_data2,'sheet1','E3:I127');

end
        
        