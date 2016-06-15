clear all

set(0, 'DefaultAxesFontSize', 16)
set(0, 'DefaultAxesFontName', 'Bookman')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%InA = load('TensABCD_def/tension_P3537720A');
InA = load('TensABCD_def/tension_P3854900A');
R1A = InA(:,1);
TensA = InA(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%InB = load('TensABCD_def/tension_P4246246B');
InB = load('TensABCD_def/tension_P4828107B');
R1B = InB(:,1);
TensB = InB(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%InC = load('TensABCD_def/tension_P2776355C');
InC = load('TensABCD_def/tension_P2995707C');
R1C = InC(:,1);
TensC = InC(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
InD = load('TensABCD_def/tension_P3865050D');
%InD = load('TensABCD_def/tension_P4019681D');
R1D = InD(:,1);
TensD = InD(:,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
V=0;
vol=0;
Dplot=linspace(-2,2,100);
DplotC=linspace(-1.4,-0.5,50);
DplotA=linspace(-2.08,-1.4,50);
DplotB=linspace(-2.18,-0.5,50);

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
mA=(log(Tenso(n1)/mean(Tenso))-log(Tenso(lenD15A)/mean(Tenso)))/(log(2*R1o(n1)/D15A)); %d15 ojo
cA=log(Tenso(lenD15A)/mean(Tenso))
xA=-2.08;
yA= -0.75; %mA*xA+cA;
yA2= 0.35;
xA2=-1.4;
mAf=(yA2-yA)/(xA2-xA);
cAf=yA-mAf*xA;
TfA=sum(Tenso(1:lenD15A))/sum(Tenso)
TgA=sum(Tenso(lenD15A+1:n1))/sum(Tenso)
alfA=TgA/TfA
betA=alfA*lenD15A/(n1-lenD15A-1)
zetA=alfA*betA

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
mB=(log(Tenso(n1)/mean(Tenso))-log(Tenso(lenD15B)/mean(Tenso)))/(log(2*R1o(n1)/D15B)); %d15 ojo
cB=log(Tenso(lenD15B)/mean(Tenso))
xB=-2.18;
yB= -1.27; %mA*xA+cA;
yB2= 1.03;
xB2=-0.6;
mBf=(yB2-yB)/(xB2-xB);
cBf=yB-mBf*xB;
TfB=sum(Tenso(1:lenD15B))/sum(Tenso)
TgB=sum(Tenso(lenD15B+1:n1))/sum(Tenso)
alfB=TgB/TfB
betB=alfB*lenD15B/(n1-lenD15B-1)
zetB=alfB*betB

Volt=R1C*0;
[R1o ind]= sort(R1C);
Tenso=TensC(ind);
TensCo=Tenso;
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
mC=(log(Tenso(n1)/mean(Tenso))-log(Tenso(lenD15C)/mean(Tenso)))/(log(2*R1o(n1)/D15C)); %d15 ojo
cC=log(Tenso(lenD15C)/mean(Tenso))
xC=-0.5;
yC=mC*xC+cC;
yC2=-0.48;
xC2=-1.25;
mCf=(yC2-yC)/(xC2-xC);
cCf=yC-mCf*xC;
TfC=sum(Tenso(1:lenD15C))/sum(Tenso)
TgC=sum(Tenso(lenD15C+1:n1))/sum(Tenso)
alfC=TgC/TfC
betC=alfC*lenD15C/(n1-lenD15C-1)
zetC=alfC*betC


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
mD=(log(Tenso(n1)/mean(Tenso))-log(Tenso(lenD15D)/mean(Tenso)))/(log(2*R1o(n1)/D15D)); %d15 ojo
cD=log(Tenso(lenD15D)/mean(Tenso))
TfD=sum(Tenso(1:lenD15D))/sum(Tenso)
TgD=sum(Tenso(lenD15D+1:n1))/sum(Tenso)
alfD=TgD/TfD
betD=alfD*lenD15D/(n1-lenD15D-1)
zetD=alfD*betD


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
TA=mA*log(2*R1A/D15A)+cA;
T=log(TensA/mean(TensA));
Taux=(TA-T).^2;
Taux(~isfinite(Taux))=0;
TA2=T;
TA2(~isfinite(T))=0;
DA=sum(Taux)/length(T)
Dl=(T-TA);
Dl(~isfinite(Dl))=0;
DlA=sum(Dl)/length(Dl)

TB=mB*log(2*R1B/D15B)+cB;
T=log(TensB/mean(TensB));
Taux=(TB-T).^2;
Taux(~isfinite(Taux))=0;
TB2=T;
TB2(~isfinite(T))=0;
DB=sum(Taux)/length(T)
Dl=(T-TB);
Dl(~isfinite(Dl))=0;
DlB=sum(Dl)/length(Dl)


TC=mA*log(2*R1C/D15C)+cC;
T=log(TensC/mean(TensC));
Taux=(TC-T).^2;
Taux(~isfinite(Taux))=0;
TC2=T;
TC2(~isfinite(T))=0;
DC=sum(Taux)/length(T)
Dl=(T-TC);
Dl(~isfinite(Dl))=0;
DlC=sum(Dl)/length(Dl)

TD=mD*log(2*R1D/D15D)+cD;
T=log(TensD/mean(TensD));
Taux=(TD-T).^2;
Taux(~isfinite(Taux))=0;
TD2=T;
TD2(~isfinite(T))=0;
DD=sum(Taux)/length(T)
Dl=(T-TD);
Dl(~isfinite(Dl))=0;
DlD=sum(Dl)/length(Dl)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
pr=5;
L=[-8 6];
figure(2)

h(1)=scatter(log(2*R1B/D15B),TB2 , pr,'g','DisplayName', 'granulometria B '); %log(TensB/mean(TensB))
hold on
h(2)=scatter(log(2*R1A/D15A),TA2 , pr,'b', 'DisplayName', 'granulometria A '); %log(TensA/mean(TensA))
hold on
h(3)=scatter(log(2*R1C/D15C), TC2 , pr,'m','DisplayName', 'granulometria C '); %log(TensC/mean(TensC))
%h(4)=scatter(log(2*R1D/D15D), TD2, pr,'r','DisplayName', 'granulometria D '); %log(TensD/mean(TensD))
plot(Dplot,mA*Dplot+cA , 'LineWidth', 2, 'Color', [0 0 0.65]);
%plot(DplotA,mAf*DplotA+cAf ,'k', 'LineWidth', 2);
%plot(Dplot,mB*Dplot+cB , 'LineWidth', 2, 'Color', [0 0.6 0]);
plot(DplotB,mBf*DplotB+cBf ,'k', 'LineWidth', 2);
plot(Dplot,mC*Dplot+cC , 'LineWidth', 2, 'Color', [0.6 0 0.6]);
plot(DplotC,mCf*DplotC+cCf ,'k', 'LineWidth', 2);
%plot(Dplot,mD*Dplot+cD , 'LineWidth', 2, 'Color',[0.6 0 0]);

plot([0 0], [-7 5],'k','DisplayName', 'D15')
plot([-2.5 2.5], [0 0],'k','DisplayName', 'Tension Promedio')
hold off

ylim([-4.5 4.5]);
xlim([-2.3 2.3]);
ylabel(['$Log(T/<T>)$'], 'interpreter','latex');
xlabel(['Log(D/D15)'], 'interpreter','latex');
title(['$Di\acute{a}metro$ $Normalizado$ vs $Tensi\acute{o}n$ $Normalizada$ '], 'interpreter','latex');
%legend({},'FontSize', 6);
legend({}, 'FontWeight', 'bold', 'FontName', 'Bookman');
legend(h(1:3),'Orientation','Horizontal','Location','southoutside');%%%aca arreglar leyenda
legend('Show');

legend('boxoff');


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%TA=mA*log(2*R1A/D15A)+cA;
%T=log(TensA/mean(TensA));
%Taux=(TA-T).^2;
%Taux(~isfinite(Taux))=0;
%DA=sum(Taux)/length(T)

%TB=mB*log(2*R1B/D15B)+cB;
%T=log(TensB/mean(TensB));
%Taux=(TB-T).^2;
%Taux(~isfinite(Taux))=0;
%DB=sum(Taux)/length(T)

%TC=mA*log(2*R1C/D15C)+cC;
%T=log(TensC/mean(TensC));
%Taux=(TC-T).^2;
%Taux(~isfinite(Taux))=0;
%DC=sum(Taux)/length(T)

%TD=mD*log(2*R1D/D15D)+cD;
%T=log(TensD/mean(TensD));
%Taux=(TD-T).^2;
%Taux(~isfinite(Taux))=0;
%DD=sum(Taux)/length(T)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%arreglar codigo, referencias a R1, R2, R3 y R4 se deben reemplazar R1A R1B R1C R1D y los percent_i
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%h1=R1A*4;
%n1=length(R1A);
%H1=zeros(n1,1);
%for i=1:n1
%    radio=h1(i);
%    if radio-R1A(n1) <= 0.00005;
%        indice1=abs(R1-radio);
%        indice=find(indice1==min(indice1));
%    else
%        indice=n1;
%    end
%    H1(i)=percent1(indice)-percent1(i);
%end
%fplot = linspace(0,40,200);
%percentf1=percent1(find(H1~=0));
%Hf1=H1(find(H1~=0));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%h2=R1B*4;
%n2=length(R2);
%H2=zeros(n2,1);
%for i=1:n2
%    radio=h2(i);
%    if radio-R2(n2) <= 0.00005;
%        indice1=abs(R2-radio);
%        indice=find(indice1==min(indice1));
%    else
%        indice=n2;
%    end
%    H2(i)=percent2(indice)-percent2(i);
%end
%fplot = linspace(0,40,200);
%percentf2=percent2(find(H2~=0));
%Hf2=H2(find(H2~=0));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%h3=R1C*4;
%n3=length(R3);
%H3=zeros(n3,1);
%for i=1:n3
%    radio=h3(i);
%    if radio-R3(n3) <= 0.00005;
%        indice1=abs(R3-radio);
%        indice=find(indice1==min(indice1));
%    else
%        indice=n3;
%    end
%    H3(i)=percent3(indice)-percent3(i);
%end
%fplot = linspace(0,40,200);
%percentf3=percent3(find(H3~=0));
%Hf3=H3(find(H3~=0));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%h4=R1D*4;
%n4=length(R4);
%H4=zeros(n4,1);
%for i=1:n4
%    radio=h4(i);
%    if radio-R4(n4) <= 0.00005;
%        indice1=abs(R4-radio);
%        indice=find(indice1==min(indice1));
%    else
%        indice=n4;
%    end
%    H4(i)=percent4(indice)-percent4(i);
%end
%fplot = linspace(0,40,200);
%percentf4=percent4(find(H4~=0));
%Hf4=H4(find(H4~=0));


%figure(2)
%plot(percentf1,Hf1,'k','DisplayName', 'granulometria A');
%hold on
%plot(percentf2,Hf2,'k','DisplayName', 'granulometria B');
%plot(percentf3,Hf3,'k','DisplayName', 'granulometria C');
%plot(percentf4,Hf4,'k','DisplayName', 'granulometria D');
%plot(1.3*fplot,fplot, 'R-','DisplayName', 'H/F=1.3' )
%plot(fplot,fplot, 'B-','DisplayName', 'H/F=1' )
%hold off
%xlabel(['Porcentaje que pasa[$\%$]'], 'interpreter','latex');
%legend('Location','northeast');
%legend('Show');
%legend('boxoff');
%xlim([-0.005 40])



