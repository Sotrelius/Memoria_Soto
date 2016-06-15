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

X = [ones(size(n)) log10(n) log10(d20)];
b = regress(log10(k2),X);
b



