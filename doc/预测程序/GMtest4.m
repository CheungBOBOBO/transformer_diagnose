function [x,delta]=GMtest4()
Shuju1=xlsread('data2.xlsx','E2:E12');%CO2原始数据
n=11;
Shuju2=zeros(n,1);
Y=zeros(n,1);%12应该设置为数据样本的数量值
Z=zeros(n-1,1);
B=zeros(n-1,2);
C=ones(n-1,1);
D=zeros(n-1,2);
A=zeros(2,1);
X=zeros(n-1,1);
Shuju2(1,1)=Shuju1(1,1);
a=0.00002;
for i=2:n
    Shuju2(i,1)=a*Shuju1(i,1)+(1-a)*Shuju2(i-1,1);%修改系数可以使预测误差变小，误差可达0.03%
end
Y(1,1)=Shuju2(1,1);%平滑处理
for i=2:n
    Y(i,1)=Shuju2(i,1)+Y(i-1,1);
end
for i=1:n-1
    Z(i,1)=0.5*Y(i,1)+0.5*Y(i+1,1);
end
for i=1:n-1
    X(i,1)=Shuju2(i+1,1);
end
B(:,1)=Z;
B(:,2)=-C;
D=-B;
A=inv(D'*D)*D'*X;
a=A(1,1);
b=A(2,1);
m=Y(1,1);
y=(1-exp(a))*(m-b/a)*exp(-a*(n+1));
x=(y-0.99*X(n-1,1))/0.01;

xlswrite('data2.xlsx',x,'sheet1','E15:E15');

end







