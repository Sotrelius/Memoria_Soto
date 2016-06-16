clear all 
set(0, 'DefaultAxesFontName', 'Bookman')
set(0, 'DefaultAxesFontSize', 20)

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
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
z5 = load('resulconf5');
Sd5 = z5(:,1);
k25 = z5(:,3);
n5 = z5(:,4);
d105=z5(:,6);
d205=z5(:,7);
d855=z5(:,8);
D5 = r*2;
U5=d855./d105;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
z50 = load('resulconf50');
Sd50 = z50(:,1);
k250 = z50(:,3);
n50 = z50(:,4);
d1050=z50(:,6);
d2050=z50(:,7);
d8550=z50(:,8);
D50 = r*2;
U50=d8550./d1050;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
z100 = load('resulconf100');
Sd100 = z100(:,1);
k2100 = z100(:,3);
n100 = z100(:,4);
d10100=z100(:,6);
d20100=z100(:,7);
d85100=z100(:,8);
D100 = r*2;
U100=d85100./d10100;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
z500 = load('resulconf500');
Sd500 = z500(:,1);
k2500 = z500(:,3);
n500 = z500(:,4);
d10500=z500(:,6);
d20500=z500(:,7);
d85500=z500(:,8);
D500 = r*2;
U500=d85500./d10500;
Sds=[0, 0.17, 0.34, 0.51, 0.68];

scatter(Sd,d20, 110, 'o', 'DisplayName', ' 27 [Pa]');
%boxplot(n,Sd);
hold on
scatter(Sd5,d205, 210, 's',  'DisplayName', '274 [Pa]');
%boxplot(n5,Sd5);
scatter(Sd50,d2050, 110, 'o', 'DisplayName', '2743 [Pa]');
scatter(Sd100,d20100, 110, 'o', 'DisplayName', '5486 [Pa]');
scatter(Sd500,d20500, 110, 'o',  'DisplayName', '27430 [Pa]');
hold on
hold off
xlabel(['Variaci$\acute{o}$n tama$\tilde{n}$o de grano Sd [-]'], 'interpreter','latex');
ylabel('D_{20} [m]');
xlim([-0.05 0.7]);
%ylim([4.8e-3 6.2e-3]);
%title('Porosidad vs Sd a distintos confinamientos', 'FontSize',28, 'FontName', 'Bookman');
legend({},'FontSize', 28, 'FontName', 'Bookman');
legend('Location', 'northoutside','Orientation', 'horizontal');
legend('Show');
legend('boxoff');
