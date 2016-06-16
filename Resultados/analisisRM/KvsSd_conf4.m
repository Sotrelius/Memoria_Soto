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
khaz = rho*g/mu*6e-4*(1+10*(n-0.26)).*(d10*100).^2;  %'Hazen:wq

ksl = rho*g/mu*1e-2*n.^3.287.*(d10*100).^2; %'Slichter
kter = rho*g/mu*10.7e-3*(n-0.13./(1-n).^(1/3)).^2.*(d10*100).^2; %'Terzaghi (Grano liso)
kkc= rho*g/mu*3.75e-5*tau*(n.^3./(1-n).^2).*(d10*100).^2; %vocovic and soro
kbey= rho*g/mu*5.2e-4*log10(500./U).*(d10*100).^2; % 'Beyer'


subplot(3,1,1);
scatter(Sd,k2, 'DisplayName', 'Acople DEM-PFV');
hold on
%scatter(Sd,kh,'filled','DisplayName','Harleman et al, tamano uniforme');
scatter(Sd,kru,'filled','DisplayName','Russel, esferas de vidrio');
scatter(Sd,khaz,'filled','DisplayName','Hazen');
scatter(Sd,ksl,'filled','DisplayName','Slichter');
scatter(Sd,kter,'filled','DisplayName','Terzaghi (Grano liso)');
scatter(Sd,kbey,'filled','DisplayName','Beyer');
%scatter(Sd,kkc,'filled','DisplayName','Vocovic y Soro');
hold off
%ylabel('Conductividad Hidráulica [cm/s]');
title('K vs variacion respecto al radio promedio. Tension normal 27 [Pa]');
%legend({},'FontSize',20,'FontWeight', 'bold', 'FontName', 'Bookman');
%legend('Location','northeast');
%legend('Show');
%legend('boxoff');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
z5 = load('resulconf50');
Sd5 = z5(:,1);
k25 = z5(:,3);
n5 = z5(:,4);
d105=z5(:,6);
d205=z5(:,7);
d855=z5(:,8);
D5 = r*2;
U5=d855./d105;

kh5 = 128996*(d105*100*3.28084).^2.05*5.263157894736842e-8/0.092903*100;   %'Harleman et al, tamano uniforme
kru5 = 300000*(d105*100*3.28084).^2*5.263157894736842e-8/0.092903*100;  %Russel, esferas de vidrio
khaz5 = rho*g/mu*6e-4*(1+10*(n5-0.26)).*(d105*100).^2;  %'Hazen
ksl5 = rho*g/mu*1e-2*n5.^3.287.*(d105*100).^2; %'Slichter
kter5 = rho*g/mu*10.7e-3*(n5-0.13./(1-n5).^(1/3)).^2.*(d105*100).^2; %'Terzaghi (Grano liso)
kkc5= rho*g/mu*3.75e-5*tau*(n5.^3./(1-n5).^2).*(d105*100).^2; %vocovic and soro
kbey5= rho*g/mu*5.2e-4*log10(500./U5).*(d105*100).^2; % 'Beyer'

subplot(3,1,2);
scatter(Sd5,k25, 50, 'DisplayName', 'Acople DEM-PFV');
hold on
%scatter(Sd,kh,'filled','DisplayName','Harleman et al, tamano uniforme');
scatter(Sd5,kru5, 50,'filled','DisplayName','Russel, esferas de vidrio');
scatter(Sd5,khaz5, 50, 'filled','DisplayName','Hazen');
scatter(Sd5,ksl5, 50,'filled','DisplayName','Slichter');
scatter(Sd5,kter5, 50, 'filled','DisplayName','Terzaghi (Grano liso)');
scatter(Sd5,kbey5, 50, 'filled','DisplayName','Beyer');
%scatter(Sd,kkc,'filled','DisplayName','Vocovic y Soro');
hold off
ylabel('Conductividad Hidraulica [cm/s]');
title('K vs variacion respecto al radio promedio. Tension normal 2743 [Pa]');
legend({},'FontSize', 34,'FontWeight', 'bold', 'FontName', 'Bookman');
legend('Location','northwest');
legend('Show');
legend('boxoff');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
z50 = load('resulconf500');
Sd50 = z50(:,1);
k250 = z50(:,3);
n50 = z50(:,4);
d1050=z50(:,6);
d2050=z50(:,7);
d8550=z50(:,8);
D50 = r*2;
U50=d8550./d1050;

kh50 = 128996*(d1050*100*3.28084).^2.05*5.263157894736842e-8/0.092903*100;   %'Harleman et al, tamano uniforme
kru50 = 300000*(d1050*100*3.28084).^2*5.263157894736842e-8/0.092903*100;  %Russel, esferas de vidrio
khaz50 = rho*g/mu*6e-4*(1+10*(n50-0.26)).*(d1050*100).^2;  %'Hazen
ksl50 = rho*g/mu*1e-2*n50.^3.287.*(d1050*100).^2; %'Slichter
kter50 = rho*g/mu*10.7e-3*(n50-0.13./(1-n50).^(1/3)).^2.*(d1050*100).^2; %'Terzaghi (Grano liso)
kkc50= rho*g/mu*3.75e-5*tau*(n50.^3./(1-n50).^2).*(d1050*100).^2; %vocovic and soro
kbey50= rho*g/mu*5.2e-4*log10(500./U50).*(d1050*100).^2; % 'Beyer'

subplot(3,1,3);
scatter(Sd50,k250, 'DisplayName', 'Acople DEM-PFV');
hold on
%scatter(Sd,kh,'filled','DisplayName','Harleman et al, tamano uniforme');
scatter(Sd50,kru50,'filled','DisplayName','Russel, esferas de vidrio');
scatter(Sd50,khaz50,'filled','DisplayName','Hazen');
scatter(Sd50,ksl50,'filled','DisplayName','Slichter');
scatter(Sd50,kter50,'filled','DisplayName','Terzaghi (Grano liso)');
scatter(Sd50,kbey50,'filled','DisplayName','Beyer');
%scatter(Sd50,kkc50,'filled','DisplayName','Vocovic y Soro');
hold off
xlabel('Variacion tamano de grano Sd [-]');
%ylabel('Conductividad Hidráulica [cm/s]');
title('K vs variacion respecto al radio promedio. Tension normal 27430 [Pa]');
%legend({},'FontSize',20,'FontWeight', 'bold', 'FontName', 'Bookman');
%legend('Location','northeast');
%legend('Show');
%legend('boxoff');
