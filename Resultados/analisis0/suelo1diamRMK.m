clear all

%VERSION CORREGIDA
%set(0, 'DefaultAxesFontSize', 20)
%set(0, 'DefaultAxesFontName', 'times')

z = load('resultados');
r = z(:,1);
k2 = z(:,3);
n = z(:,4);

D=2*r;
rho=1.;%1000kg/m3 to g/cm3 => 1000/100^3 => 10^6/10^6 
g=981;%cm/s
mu=0.01;%0.001kg/m/s to g/cm/s => 1000/100 =>10^-3*10
rl=log10(D);
k2l=log10(k2);
E=n/(1-n);
De=[0.001, 0.002];
ke=[1.15, 4.76];


%keyboard
figure
set(gcf, 'DefaultAxesFontSize', 20)
set(gcf, 'DefaultAxesFontName', 'times')

plot(D,k2,'pk', 'MarkerSize',10,'DisplayName', 'DEM-PFV acople');
hold on
plot(D,10^6.109*D.^1.931, 'DisplayName', 'K = 1.28e-6 d^{1.931}');
%scatter(D,10*(D*100).^2, 'filled', 'DisplayName', 'Hazen simplificada');
plot(D,300000*(D*1000).^2*5.263157894736842e-8/0.092903*100, 'b--', 'DisplayName', 'Shepherd, esferas de vidrio');
plot(D,208818*(D*1000).^1.94*5.263157894736842e-8/0.092903*100, 'g--', 'DisplayName', 'Schriever, esferas de vidrio');
plot(D,40000*(D*1000).^1.85*5.263157894736842e-8/0.092903*100, 'c--o', 'DisplayName', 'Shepherd, de textura madura');
plot(D,12000*(D*1000).^1.75*5.263157894736842e-8/0.092903*100, 'k--', 'DisplayName', 'Shepherd, Dunas');
plot(D,3500*(D*1000).^1.65*5.263157894736842e-8/0.092903*100, 'r--', 'DisplayName', 'Shepherd, Playa');
plot(D,800*(D*1000).^1.5*5.263157894736842e-8/0.092903*100, 'm--', 'DisplayName', 'Shepherd, canal inmaduro');
scatter(D,128996*(D*100*3.28084).^2.05*5.263157894736842e-8/0.092903*100, 'filled', 'DisplayName', 'Harleman et al, tamano uniforme');
scatter(D,rho*g/mu*6e-4*(1+10*(n-0.26)).*(D*100).^2, 'filled', 'DisplayName', 'Hazen');
scatter(D,rho*g/mu*5.2e-4*log10(500)*(D*100).^2, 'filled', 'DisplayName', 'Beyer');
scatter(D,rho*g/mu*10.7e-3*(n-0.13./(1-n).^(1/3)).^2.*(D*100).^2, 'filled', 'DisplayName', 'Terzaghi (Grano liso)');
%scatter(D,rho*g/mu*6.1e-3*(n-0.13/(1-n)^(1/3))^2*(D*100).^2, 'filled', 'DisplayName', 'Terzaghy (Coarse grains)');
scatter(D,rho*g/mu*1e-2*n.^3.287.*(D*100).^2, 'filled', 'DisplayName', 'Slichter');
scatter(D,rho*g/mu*4.8e-4*10^0.3*((D*100).^1.15).^2, 'filled', 'DisplayName', 'Bialas');
%scatter(D,10*10^(1.291*E-0.6435)*((D*100).^(10^(0.5504-0.2937*E)/2.)).^2, 'DisplayName', 'Chapuis');
%scatter(D,rho*g/mu*7.501e-6*(2.^D).^2, 'DisplayName', 'Krumbein and Monk');
plot(De,ke,'pb', 'MarkerSize',10, 'DisplayName', 'Experimentos esferas de vidrio');
hold off

set(gca,'YScale','log');
set(gca,'XScale','log');
xlabel('$d [m]$','interpreter', 'latex');
ylabel('$K [cm/s$]','interpreter', 'latex');
title('Di$\acute{a}$metro vs Conductividad Hidr$\acute{a}$ulica','interpreter', 'latex');
legend({},'FontSize',29,'FontWeight', 'bold', 'FontName', 'Bookman');
legend('Location','eastoutside');
legend('Show');
legend('boxoff');

%get(gcf, 'DefaultAxesFontSize')
%get(gcf, 'DefaultAxesFontName')

%set(0, 'DefaultAxesFontSize', 8)
%set(0, 'DefaultAxesFontName', 'times')

%pause
%cd /home/diego/memoria/

%% str = 'ValRcte2.eps';
%print -depsc2 -r600 'ValRcte2RMK2.eps'
%% print -depsc2 -r600 str
%% print(str, '-depsc2')
%cd /home/diego/memoria/Codigos/analisis0
%close all 

%funciones = cell(10,1);
%funciones{1} = inline();
%funciones{2} = inline();
%funciones{3} = inline();
%funciones{4} = inline();
%funciones{5} = inline();
%funciones{6} = inline();

%nombres  = cell(10,1);
%nombres{1} = 'fulano';
%nombres{2} = 'fulano';
%nombres{3} = 'fulano';
%nombres{4} = 'fulano';
%nombres{5} = 'fulano';
%nombres{6} = 'fulano';


%estructuraPlot = [];

%for iFunc = 1:10
%	aux = struct();
%	aux.nombre = nombres{iFunc};
%	aux.funcion = funciones{iFunc};
%	estructuraPlot = [estructuraPlot, aux];
%end
