clear all 

z = load('resultmanualPSD');
SD = z(:,1);
R1 = z(:,2);
R = z(:,3);
Gf = z(:,4);
Gg = z(:,5);

subplot(2,1,1);
%scatter(G,R1,'+r', 'DisplayName', 'Acople DEM-PFV');
plot(R, Gf, '*--r', 'DisplayName', 'Granos finos');
hold on
plot(R, Gg, '*--b', 'DisplayName', 'Granos Gruesos');
plot(R,Gg+Gf,'*--g', 'DisplayName', 'Granos Gruesos mas finos');
%scatter(Sd,kkc,'filled','DisplayName','Vocovic y Soro');
hold off
ylabel('G');
ylim([0 1]);
xlim([1 7.5]);
xlabel('d_{max}/d_{min} [-]');
title('R vs Porcentaje de transmicion de esfuerzos');
%legend({},'FontSize',16,'FontWeight', 'bold', 'FontName', 'Bookman');
%legend('Show');
%legend('boxoff');

subplot(2,1,2);
%scatter(G,R1,'+r', 'DisplayName', 'Acople DEM-PFV');
plot(R1,Gg+Gf,'*--g', 'DisplayName', 'Granos Gruesos+finos     .');
hold on
plot(R1,Gg,'*--b', 'DisplayName', 'Granos Gruesos     .');
plot(R1,Gf,'*--r', 'DisplayName', 'Granos finos      ');
%scatter(Sd,kkc,'filled','DisplayName','Vocovic y Soro');
hold off
ylabel('G');
ylim([0 1]);
xlim([1.2 1.6]);
xlabel('d_{85}/d_{15} [-]');
title('R1 vs Porcentaje de transmicion de esfuerzos');
legend({},'FontSize',11,'FontWeight', 'bold', 'FontName', 'Bookman');
legend('Location','southoutside','Orientation', 'horizontal');
%legend('Location','northeast');
legend('Show');
legend('boxoff');
