clear all 

z = load('resultmanualBPSD');
R1 = z(:,1);
G = z(:,2);


%scatter(G,R1,'+r', 'DisplayName', 'Acople DEM-PFV');
plot(R1, G,'*--r', 'DisplayName', 'Granos Finos   .');
hold on
plot(R1, 1-G,'*--g', 'DisplayName', 'Granos Gruesos');
%scatter(Sd,kh,'filled','DisplayName','Harleman et al, tamano 
%scatter(Sd,kkc,'filled','DisplayName','Vocovic y Soro');
hold off
ylabel('G [-]');
xlabel('d_{max}/d_{min} [-]');
set(gca,'YScale','log');
ylim([1e-3 2]);
xlim([0.6 6]);
title(['Porcentaje de transmisi$\acute{o}$n de fuerzas vs R '], 'interpreter','latex');
legend({},'FontSize',16,'FontWeight', 'bold', 'FontName', 'Bookman');
legend('Location','southoutside','Orientation', 'horizontal');
legend('Show');
legend('boxoff');

