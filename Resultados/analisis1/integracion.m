clear all 
close all

a = 1.4e6;
b = 5.9e2;
c = -0.67;
d = 3e-3;
Ss = 0.34;

integral = inline('a/3*x^3 + b/2*x^2 + c*x', 'a', 'b', 'c', 'x');

d1 = d-d*Ss;
d2 = d+d*Ss;
valorIntegral = (integral(a,b,c,d2) - integral(a,b,c,d1))/(d2-d1);

z = load('resultadosPoly');
Sd = z(:,1);
k2 = z(:,3);
n = z(:,4);
%kbr=(n/0.117).^7*100/86400;
kkc= 1000*9.81/0.001*(n.^3./(1-n).^2)*0.003^2/180*86400/100;

z2 = load('resultadosPoly02');
Sd2 = z2(:,1);
k22 = z2(:,3);
n2 = z2(:,4);
kkc2= 1000*9.81/0.001*(n2.^3./(1-n2).^2)*0.003^2/180*86400/100;

z1 = load('resultadosPoly01');
Sd1 = z1(:,1);
k21 = z1(:,3);
n1 = z1(:,4);

z05 = load('resultadosPoly005');
Sd05 = z05(:,1);
k205 = z05(:,3);
n05 = z05(:,4);

z6 = load('resultadosPoly06');
Sd6 = z6(:,1);
k26 = z6(:,3);
n6 = z6(:,4);

aux=0;
N=length(Sd);

for i=1:N
	if Sd(i)==Ss
		aux=aux+1;
		So(i)=k2(i)/valorIntegral;
	end
end

Sd
aux

subplot(2,2,1);
scatter(Sd,k2);
hold on
plot(Sd,kkc,'+r');
scatter(Sd2,k22);
plot(Sd2,kkc2,'+r');
scatter(Sd1,k21);
scatter(Sd05,k205);
scatter(Sd6,k26);
hold off
xlabel('Variacion tamaño de grano Sd [-]');
ylabel('Permeabilidad [cm/s]');
title('Permeabilidad vs variacion respecto al radio promedio');

subplot(2,2,2);
scatter(Sd,n);
hold on
%plot(Sd,nbr);
scatter(Sd1,n1);
scatter(Sd2,n2);
scatter(Sd05,n05);
scatter(Sd6,n6);
hold off
xlabel('Variacion tamaño de grano Sd [-]');
ylabel('Porosidad [-]');
title('Porosidad vs variacion respecto al radio promedio');

%subplot(2,2,3);
%boxplot(k2, Sd);
%xlabel('Variacion tamaño de grano Sd [-]');
%ylabel('Permeabilidad [cm/s]');
%title('Permeabilidad vs variacion respecto al radio promedio');

%subplot(2,2,4);
%boxplot(n, Sd);
%xlabel('Variacion tamaño de grano Sd [-]');
%ylabel('Porosidad [-]');
%title('Porosidad vs variacion respecto al radio promedio');




%find

%49.33/13.8214
%55.76/14.7924
%70.60/16.7345

%14.7924
