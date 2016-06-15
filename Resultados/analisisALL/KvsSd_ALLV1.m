clear all
z = load('resultALL');
Sd = z(:,1);
k2 = z(:,3);
n = z(:,4);
d10=z(:,6);
d20=z(:,7);
d85=z(:,8);
r=0.0003;
D = r*2;
rho = 1. ;   %1000kg/m3 to g/cm3 => 1000/100^3 => 10^6/10^6 
g = 981 ;     %cm/s
mu = 0.01 ;   %0.001kg/m/s to g/cm/s => 1000/100 =>10^-3*10
U=d85./d10;
T=20;
tau=1.093e-4*T^2+2.102e-2*T+0.5889;

kh = 128996*(d10*1000).^2.05*5.263157894736842e-8/0.092903*100;   %'Harleman et al, tamano uniforme
kru = 300000*(d10*1000).^2*5.263157894736842e-8/0.092903*100;  %Russel, esferas de vidrio
khaz = rho*g/mu*6e-4*(1+10*(n-0.26)).*(d10*100).^2;  %'Hazen
ksl = rho*g/mu*1e-2*n.^3.287.*(d10*100).^2; %'Slichter
kter = rho*g/mu*10.7e-3*(n-0.13./(1-n).^(1/3)).^2.*(d10*100).^2; %'Terzaghi (Grano liso)
kkc= rho*g/mu*3.75e-5*tau*(n.^3./(1-n).^2).*(d10*100).^2; %vocovic and soro
kbey= rho*g/mu*5.2e-4*log10(500./U).*(d10*100).^2; % 'Beyer'
ksoto= rho*g/mu*4553*n.^4.67.*d20.^2.22;
%set(0, 'DefaultAxesFontSize', 19)
%set(0, 'DefaultAxesFontName', 'Bookman')


%scatter(Sd,k2, 70, 'DisplayName', 'Acople DEM-PFV');
%hold on
%%scatter(Sd,kru, 70,'filled', 'd', 'DisplayName','Russel, esferas de vidrio');
%scatter(Sd,ksoto, 70, 'filled', 'd','DisplayName','Soto');
%plot(Sd,rho*g/mu*(0.41)^4.67*4553*d20.^2.22, 'b--');
%%scatter(Sd,khaz, 70, 'filled', 'd','DisplayName','Hazen');
%%scatter(Sd,ksl, 70,'filled', 'd','DisplayName','Slichter');
%%scatter(Sd,kter, 70, 'filled', 'd','DisplayName','Terzaghi (Grano liso)');
%%scatter(Sd,kbey, 70, 'filled', 'd', 'DisplayName','Beyer');
%hold off
%ylabel(['Conductividad Hidr$\acute{a}$ulica [cm/s]'], 'interpreter','latex');
%xlabel(['Variaci$\acute{o}$n tama$\tilde{n}$o grano Sd [-]'],'interpreter','latex')
%%xlabel('Variacion tama\tilde{n}o grano Sd [-]');
%title(['K vs Sd. Tensi$\acute{o}$n normal 2743 [Pa]'], 'interpreter','latex');
%legend({},'FontSize', 42,'FontWeight', 'bold', 'FontName', 'Bookman');
%legend('Location','eastoutside');
%legend('Show');
%legend('boxoff');


figure(2)
alpha = rho*g/mu*474; 
beta = 3.57;
gamma = 1.98;


Sdplot = linspace(min(Sd),max(Sd),100);
d20plot = 0.006*Sdplot.*Sdplot-0.003*Sdplot+0.006;
%Sdplot = linspace(min(d10),max(d10),100)*100;  %d10*100
nplot = linspace(0.2,0.4,5);
funcSoto = inline('alpha*n^(beta)*d20.^(gamma)', 'alpha', 'beta', 'gamma', 'n', 'd20');

alp = rho*g/mu*1e-2;
bet = 3.287;
gam = 2;
d10plot = (0.0067*Sdplot.*Sdplot-0.0051*Sdplot+0.006)*100;
%d10plot = linspace(min(d20),max(d20),100)*100; %do20plot
funcSlichter = inline('alp*n^bet*(d10).^gam', 'alp', 'bet', 'gam', 'n','d10' );

plot(Sdplot, funcSoto(alpha, beta, gamma, nplot(1), d20plot),'r', 'LineWidth', 0.6);
hold on
plot(Sdplot, funcSoto(alpha, beta, gamma, nplot(2), d20plot), 'k', 'LineWidth', 0.8);
plot(Sdplot, funcSoto(alpha, beta, gamma, nplot(3), d20plot),'Color', [0.8 0.8 0.8], 'LineWidth', 0.8);
plot(Sdplot, funcSoto(alpha, beta, gamma, nplot(4), d20plot), 'b', 'LineWidth', 0.6);
plot(Sdplot, funcSoto(alpha, beta, gamma, nplot(5), d20plot), 'g', 'LineWidth', 0.6);

plot(Sdplot, funcSlichter(alp, bet, gam, nplot(1), d10plot), '--r', 'LineWidth', 1.3);
plot(Sdplot, funcSlichter(alp, bet, gam, nplot(2), d10plot), '--k', 'LineWidth', 1.3);
plot(Sdplot, funcSlichter(alp, bet, gam, nplot(3), d10plot),'--' ,'Color', [0.8 0.8 0.8] , 'LineWidth', 1.9);
plot(Sdplot, funcSlichter(alp, bet, gam, nplot(4), d10plot), '--b', 'LineWidth', 1.3);
plot(Sdplot, funcSlichter(alp, bet, gam, nplot(5), d10plot), '--g', 'LineWidth', 1.3);
scatter(Sd,k2, 70, 'd', 'MarkerEdgeColor', [0 0 0], 'LineWidth', 0.2, 'DisplayName', 'Acople DEM-PFV');

hold off
ylabel(['Conductividad Hidr$\acute{a}$ulica [cm/s]'], 'interpreter','latex');
xlabel(['Variaci$\acute{o}$n tama$\tilde{n}$o grano Sd [-]'],'interpreter','latex')
title(['K vs Sd. Para distintos valores de Tensi$\acute{o}$n '], 'interpreter','latex');
legend({},'FontSize', 42,'FontWeight', 'bold', 'FontName', 'Bookman');
legend('Location','eastoutside');
legend('Show');
legend('boxoff');



