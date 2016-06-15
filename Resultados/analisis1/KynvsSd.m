clear all 
close all

z = load('resultadosPoly');
Sd = z(:,1);
k2 = z(:,3);
n = z(:,4);
%kkh= 128996*(D*100*3.28084).^2.05*5.263157894736842e-8/0.092903*100;

z2 = load('resultadosPoly02');
Sd2 = z2(:,1);
k22 = z2(:,3);
n2 = z2(:,4);
%kkh2= 128996*(D*100*3.28084).^2.05*5.263157894736842e-8/0.092903*100;

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

subplot(2,1,1);
scatter(Sd,k2);
hold on
scatter(Sd2,k22);
scatter(Sd1,k21);
scatter(Sd05,k205);
scatter(Sd6,k26);
hold off
xlabel('Variacion tamaño de grano Sd [-]');
ylabel('Permeabilidad [cm/s]');
title('Permeabilidad vs variacion respecto al radio promedio');

subplot(2,1,2);
scatter(Sd,n);
hold on
scatter(Sd1,n1);
scatter(Sd2,n2);
scatter(Sd05,n05);
scatter(Sd6,n6);
hold off
xlabel('Variacion tamaño de grano Sd [-]');
ylabel('Porosidad [-]');
title('Porosidad vs variacion respecto al radio promedio');

