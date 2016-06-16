clear all 
set(0, 'DefaultAxesFontName', 'Bookman')
set(0, 'DefaultAxesFontSize', 19)

r=0.003;
z = load('resulconfBL');
Sd = z(:,1);
conf = z(:,11)/1000;
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



Sds=[0, 0.17, 0.34, 0.51, 0.68];

scatter(conf,n, 150, 'd','MarkerFaceColor', [0.5 0.5 0.5], 'MarkerEdgeColor', [0 0 0], 'DisplayName', 'DEM-PFV');
%boxplot(n,Sd);
xlabel(['Presi$\acute{o}$n de confinamiento [KPa]'], 'interpreter','latex');
ylabel('Porosidad [-]');
%ylim([0.32 0.42]);
%xlim([-0.05 0.9]);
%title('Porosidad vs Sd a distintos confinamientos', 'FontSize',28, 'FontName', 'Bookman');
legend({},'FontSize', 28, 'FontName', 'Bookman');
legend('Location', 'northoutside','Orientation', 'horizontal');
legend('Show');
legend('boxoff');
