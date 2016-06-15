clear all

set(0, 'DefaultAxesFontSize', 16)
set(0, 'DefaultAxesFontName', 'Bookman')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
InB = load('TensABCD/tension_P3196234B');
R1B = InB(:,1);
TensB = InB(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%InA = load('granSkempton_A/tension_P1445434');
InA = load('TensABCD/tension_P1964129A');
R1A = InA(:,1);
TensA = InA(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
InD = load('TensABCD/tension_P2216751D');
R1D = InD(:,1);
TensD = InD(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%InC = load('granSkempton_C/tension_P693767');
InC = load('TensABCD/tension_P1720288C');
R1C = InC(:,1);
TensC = InC(:,2);



V=0;
vol=0;

Volt=R1A*0;
[R1o ind]= sort(R1A);
Tenso=TensA(ind);
Tensn=TensA./mean(TensA);
Volt=R1A.*R1A.*R1A;
n1=length(R1A);
Voltot=sum(Volt); 

for i=1:n1
    V=R1o(i)*R1o(i)*R1o(i);
    vol=vol+V;
    count=i;
    if vol>=Voltot*0.15
        count=i ;
        D15A=2*R1o(count); %aca D15
        lenD15A=count;     %aca posicion
        Count=0;
        vol=0;
        break
    end
end

Volt=R1B*0;
[R1o ind]= sort(R1B);
Tenso=TensB(ind);
Tensn=TensB./mean(TensB);
Volt=R1B.*R1B.*R1B;
n1=length(R1B);
Voltot=sum(Volt); 

for i=1:n1
    V=R1o(i)*R1o(i)*R1o(i);
    vol=vol+V;
    count=i;
    if vol>=Voltot*0.15
        count=i ;
        D15B=2*R1o(count); %aca D15
        lenD15B=count;     %aca posicion
        Count=0;
        vol=0;
        break
    end
end

Volt=R1C*0;
[R1o ind]= sort(R1C);
Tenso=TensC(ind);
Tensn=TensC./mean(TensC);
Volt=R1C.*R1C.*R1C;
n1=length(R1C);
Voltot=sum(Volt); 

for i=1:n1
    V=R1o(i)*R1o(i)*R1o(i);
    vol=vol+V;
    count=i;
    if vol>=Voltot*0.15
        count=i ;
        D15C=2*R1o(count); %aca D15
        lenD15C=count;     %aca posicion
        Count=0;
        vol=0;
        break
    end
end

Volt=R1D*0;
[R1o ind]= sort(R1D);
Tenso=TensD(ind);
Tensn=TensD./mean(TensD);
Volt=R1D.*R1D.*R1D;
n1=length(R1D);
Voltot=sum(Volt); 

for i=1:n1
    V=R1o(i)*R1o(i)*R1o(i);
    vol=vol+V;
    count=i;
    if vol>=Voltot*0.15
        count=i ;
        D15D=2*R1o(count); %aca D15
        lenD15D=count;     %aca posicion
        Count=0;
        vol=0;
        break
    end
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
pr=5;
L=[-8 6];
figure(2)
%scatter(log(R1A/mean(R1A)), log(TensA/mean(TensA)), pr)
%hold on
%scatter(log(R1B/mean(R1B)), log(TensB/mean(TensB)), pr,'r')
%scatter(log(R1C/mean(R1C)), log(TensC/mean(TensC)), pr,'g')
%scatter(log(R1D/mean(R1D)), log(TensD/mean(TensD)), pr,'k')
scatter(log(2*R1A/D15A), log(TensA/mean(TensA)), pr,'DisplayName', 'granulometria A ')
hold on
scatter(log(2*R1B/D15B), log(TensB/mean(TensB)), pr,'r','DisplayName', 'granulometria B ')
scatter(log(2*R1C/D15C), log(TensC/mean(TensC)), pr,'g','DisplayName', 'granulometria C ')
scatter(log(2*R1D/D15D), log(TensD/mean(TensD)), pr,'k','DisplayName', 'granulometria D ')
%plot([D15A D15A],L)
%plot([D15B D15B],L,'r')
%plot([D15D D15D],L,'k')
%plot([D15C D15C],L,'g')
%plot([log(D15A/2/mean(R1A)) log(D15A/2/mean(R1A))],L)
%plot([log(D15B/2/mean(R1B)) log(D15B/2/mean(R1B))],L,'r')
%plot([log(D15D/2/mean(R1D)) log(D15D/2/mean(R1D))],L,'k')
%plot([log(D15C/2/mean(R1C)) log(D15C/2/mean(R1C))],L,'g')
plot([0 0], [-7 5],'k','DisplayName', 'D15')
plot([-2.5 2.5], [0 0],'k','DisplayName', 'Tension Promedio')
hold off

ylim([-7.5 7.5])
xlim([-2.5 2.5])
ylabel(['$Log(T/<T>)$'], 'interpreter','latex');
xlabel(['Log(D/D15)'], 'interpreter','latex');
title(['Diametro vs Tension '], 'interpreter','latex');
%legend({},'FontSize', 6);
legend({}, 'FontWeight', 'bold', 'FontName', 'Bookman');
legend('Orientation','Horizontal','Location','southoutside');
legend('Show');
legend('boxoff');


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%[coun,cent]=hist(Tensn,3000);
%a=coun.*(cent(2)-cent(1));
%coun=coun./sum(a);
%coun=coun*(cent(2)-cent(1));

%[counf,centf]=hist(Tensfn,3000);
%af=counf.*(centf(2)-centf(1));
%counf=counf./sum(af);
%counf=counf*(centf(2)-centf(1));

%[coung,centg]=hist(Tensgn,3000);
%ag=coung.*(centg(2)-centg(1));
%coung=coung./sum(ag);
%coung=coung*(centg(2)-centg(1));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%figure(1)
%%bar(cent,coun);
%scatter(cent,coun);
%hold on
%scatter(centf,counf,'r');
%scatter(centg,coung,'g');
%%bar(centf,counf,'r');
%%bar(centg,coung,'g');
%hold off
%set(gca,'XScale','log');
%set(gca,'YScale','log');
%grid on
%%ylim([-1 100])
%%xlim([1e-6 10])
%ylabel(['Probabilidad'], 'interpreter','latex');
%xlabel(['Tension Normalizada'], 'interpreter','latex');
%title(['Distribucion de probabilidades de Tension normalizada '], 'interpreter','latex');
%legend({},'FontWeight', 'bold', 'FontName', 'Bookman');
%legend('Location','northwest');
%legend('Show');
%legend('boxoff');




