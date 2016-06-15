clear all

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
E=n./(1-n);

plot(rl,k2l,'*r','DisplayName', 'DEM-PFV acople');
xlabel(['$Log(D)$ [$Log(m)$]'], 'interpreter','latex');
ylabel(['Log(K) [Log(cm/s)]'], 'interpreter','latex');
%title(['$Log10(Diametro)$ vs $Log10(Conductividad hidraulica)$'], 'interpreter','latex');
legend('Location','northwest');
legend('Show');
legend('boxoff');

