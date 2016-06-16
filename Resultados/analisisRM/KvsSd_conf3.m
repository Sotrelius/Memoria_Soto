clear all 
close all

r=0.003;
z = load('resulconf05');
Sd = z(:,1);
k2 = z(:,3);
n = z(:,4);
d10=z(:,6);
d20=z(:,7);
d85=z(:,8);
D = r*2;
di=D-D*Sd;
df=D+D*Sd;
rho = 1. ;   %1000kg/m3 to g/cm3 => 1000/100^3 => 10^6/10^6 
g = 981 ;     %cm/s
mu = 0.01 ;   %0.001kg/m/s to g/cm/s => 1000/100 =>10^-3*10
%d10 =di+ (df-di)/10;
%d60 =di+ (df-di)/10*6 ;
U=d85./d10;
T=20;
tau=1.093e-4*T^2+2.102e-2*T+0.5889;

kh = 128996*(d10*100*3.28084).^2.05*5.263157894736842e-8/0.092903*100;   %'Harleman et al, tamano uniforme
kru = 300000*(d10*100*3.28084).^2*5.263157894736842e-8/0.092903*100;  %Russel, esferas de vidrio
khaz = rho*g/mu*6e-4*(1+10*(n-0.26)).*(d10*100).^2;  %'Hazen
ksl = rho*g/mu*1e-2*n.^3.287.*(d10*100).^2; %'Slichter
kter = rho*g/mu*10.7e-3*(n-0.13./(1-n).^(1/3)).^2.*(d10*100).^2; %'Terzaghi (Grano liso)
kkc= rho*g/mu*3.75e-5*tau*(n.^3./(1-n).^2).*(d10*100).^2; %vocovic and soro
kbey= rho*g/mu*5.2e-4*log10(500./U).*(d10*100).^2; % 'Beyer'


subplot(3,1,1);
scatter(Sd,k2, 'DisplayName', 'Acople DEM-PFV');
hold on
%scatter(Sd,kh,'filled','DisplayName','Harleman et al, tamano uniforme');
scatter(Sd,kru ,'DisplayName','Russel, esferas de vidrio');
scatter(Sd,khaz,'DisplayName','Hazen');
scatter(Sd,ksl,'DisplayName','Slichter');
scatter(Sd,kter,'DisplayName','Terzaghi (Grano liso)');
scatter(Sd,kbey,'DisplayName','Beyer');
%:scatter(Sd,kkc,'filled','DisplayName','Vocovic y Soro');
hold off
ylabel('Conductividad Hidraulica [cm/s]');
title('K vs variacion respecto al radio promedio');
legend({},'FontSize',20,'FontWeight', 'bold', 'FontName', 'Bookman');
legend('Location','northeast');
legend('Show');
legend('boxoff');

subplot(3,1,2);
scatter(Sd,d10);
title('Porosidad vs variacion respecto al radio promedio');
xlabel('Variacion tamano de grano Sd [-]');
ylabel('Diametro d10 [m]');
%legend({},'FontSize',20,'FontWeight', 'bold', 'FontName', 'Bookman');
%legend('Location','northeast');
%legend('Show');
%legend('boxoff');

subplot(3,1,3);
scatter(Sd,n);
title('Porosidad vs variacion respecto al radio promedio');
xlabel('Variacion tamano de grano Sd [-]');
ylabel('Porosidad [-]');

