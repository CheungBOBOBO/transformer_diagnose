function [x,delta]=GMtest1()
Shuju1=xlsread('data2.xlsx','B2:B12');%读取H2原始数据
n=11;%数据样本的数量（这里的样本只有11条数据）
Shuju2=zeros(n,1);%初始化矩阵（设置为零矩阵）
Y=zeros(n,1);%初始化矩阵（设置为零矩阵）
Z=zeros(n-1,1);%初始化矩阵（设置为零矩阵）
B=zeros(n-1,2);%初始化矩阵（设置为零矩阵）
C=ones(n-1,1);%初始化矩阵（设置为壹矩阵，既每个元素均为1）
D=zeros(n-1,2);%初始化矩阵（设置为零矩阵）
A=zeros(2,1);%初始化矩阵（设置为零矩阵）
X=zeros(n-1,1);%初始化矩阵（设置为零矩阵）
Shuju2(1,1)=Shuju1(1,1);
a=0.005609;
for i=2:n
    Shuju2(i,1)=a*Shuju1(i,1)+(1-a)*Shuju2(i-1,1);%对Shuju2矩阵中的每个元素进行处理
end
Y(1,1)=Shuju2(1,1);%平滑处理
for i=2:n
    Y(i,1)=Shuju2(i,1)+Y(i-1,1);%对Y矩阵中的每个元素进行处理
end
%以下为灰色理论的方法
for i=1:n-1
    Z(i,1)=0.5*Y(i,1)+0.5*Y(i+1,1);%对Z矩阵中的每个元素进行处理
end
for i=1:n-1
    X(i,1)=Shuju2(i+1,1);
end
B(:,1)=Z;%将Z矩阵放入B矩阵的第一列
B(:,2)=-C;%将B矩阵的第二列全部设置为“-1”
D=-B;
A=inv(D'*D)*D'*X;%D'表示对D矩阵求转置，inv（D'*D）表示对D'*D矩阵求逆
a=A(1,1);
b=A(2,1);
m=Y(1,1);
y=(1-exp(a))*(m-b/a)*exp(-a*(n+1));
x=(y-0.99*X(n-1,1))/0.01;
xlswrite('data2.xlsx',x,'sheet1','B15:B15');%输出预测结果
end







