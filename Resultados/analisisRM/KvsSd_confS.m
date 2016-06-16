z5 = load('resulconf50');
Sd5 = z5(:,1);
k25 = z5(:,3);
n5 = z5(:,4);
d105=z5(:,6);
d205=z5(:,7);
d855=z5(:,8);
r=0.0003;
D5 = r*2;
U5=d855./d105;

set(0, 'DefaultAxesFontSize', 19)
set(0, 'DefaultAxesFontName', 'Bookman')
%plot(ttrey5/adi,chispesa3(1:length(ttrey5)),'-ko','MarkerFaceColor',[120/255 120/255 120/255],'MarkerSize',7)

kh5 = 128996*(d105*100*3.28084).^2.05*5.263157894736842e-8/0.092903*100;   %'Harleman et al, tamano uniforme
kru5 = 300000*(d105*100*3.28084).^2*5.263157894736842e-8/0.092903*100;  %Russel, esferas de vidrio
khaz5 = rho*g/mu*6e-4*(1+10*(n5-0.26)).*(d105*100).^2;  %'Hazen
ksl5 = rho*g/mu*1e-2*n5.^3.287.*(d105*100).^2; %'Slichter
kter5 = rho*g/mu*10.7e-3*(n5-0.13./(1-n5).^(1/3)).^2.*(d105*100).^2; %'Terzaghi (Grano liso)
kkc5= rho*g/mu*3.75e-5*tau*(n5.^3./(1-n5).^2).*(d105*100).^2; %vocovic and soro
kbey5= rho*g/mu*5.2e-4*log10(500./U5).*(d105*100).^2; % 'Beyer'


scatter(Sd5,k25, 70, 'DisplayName', 'Acople DEM-PFV');
hold on
%scatter(Sd,kh,'filled','DisplayName','Harleman et al, tamano uniforme');
scatter(Sd5,kru5, 70,'filled', 'd', 'DisplayName','Russel, esferas de vidrio');
scatter(Sd5,khaz5, 70, 'filled', 'd','DisplayName','Hazen');
scatter(Sd5,ksl5, 70,'filled', 'd','DisplayName','Slichter');
scatter(Sd5,kter5, 70, 'filled', 'd','DisplayName','Terzaghi (Grano liso)');
scatter(Sd5,kbey5, 70, 'filled', 'd', 'DisplayName','Beyer');
%scatter(Sd,kkc,'filled','DisplayName','Vocovic y Soro');
hold off
ylabel(['Conductividad Hidr$\acute{a}$ulica [cm/s]'], 'interpreter','latex');
xlabel(['Variaci$\acute{o}$n tama$\tilde{n}$o grano Sd [-]'],'interpreter','latex')
%xlabel('Variacion tama\tilde{n}o grano Sd [-]');
title(['K vs Sd. Tensi$\acute{o}$n normal 2743 [Pa]'], 'interpreter','latex');
legend({},'FontSize', 42,'FontWeight', 'bold', 'FontName', 'Bookman');
legend('Location','eastoutside');
legend('Show');
legend('boxoff');

%cd /home/diego/memoria/
%print -depsc2 -r600 'KvsSd_Conf2743.eps'
%cd /home/diego/memoria/Codigos/analisisRM

%close all 
