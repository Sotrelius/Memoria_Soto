clear all

set(0, 'DefaultAxesFontSize', 28)
set(0, 'DefaultAxesFontName', 'Bookman')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
z1 = load('granulometrySd17');
R1 = z1(:,1);
percent1 = z1(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
z2 = load('granulometrySd34');
R2 = z2(:,1);
percent2 = z2(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
z3 = load('granulometrySd51');
R3 = z3(:,1);
percent3 = z3(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
z4 = load('granulometrySd68');
R4 = z4(:,1);
percent4 = z4(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
z5 = load('granulometrySd75');
R5 = z5(:,1);
percent5 = z5(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
z6 = load('granulometrySd85');
R6 = z6(:,1);
percent6 = z6(:,2);
alfa=[2*0.003 2*0.003];
beta=[0 100];

plot(alfa,beta,'c','DisplayName', '0.00');
hold on
plot(2*R1,percent1,'k','DisplayName', '0.17');
%hold on
plot(2*R2,percent2,'r', 'DisplayName', '0.34');
plot(2*R3,percent3,'b', 'DisplayName', '0.51');
plot(2*R4,percent4,'m', 'DisplayName', '0.68');
%plot(2*R5,percent5,'g', 'DisplayName', 'Sd75');
%semilogx(2*R6,percent6,'m', 'DisplayName', 'Sd85');
hold off
set(gca,'XScale','log');
grid on

xlabel(['Di$\acute{a}$metro [m]'], 'interpreter','latex');
ylim([-1 100])
xlim([0.0009 0.02])
ylabel(['Porcentaje que pasa[$\%$]'], 'interpreter','latex');
title(['Curva granulom$\acute{e}$trica para distintos valores de Sd'], 'interpreter','latex');
legend({},'FontWeight', 'bold', 'FontName', 'Bookman');
legend('Location','northwest');
legend('Show');
legend('boxoff');
