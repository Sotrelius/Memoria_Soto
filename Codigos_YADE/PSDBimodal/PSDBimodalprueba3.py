#**********************************************************************
#Cuadrilatero con agua, PSD bimodal
#acoplado con flujo (ok)
#eliminado funciones kfin y kini, aumento de SD (ok)
#plotear cambios de posiciones despAcum despMax desMean despAcumMax(en proceso)
#28 de septiembre 2015
#(esta listo para los finos, hay que hacer analogo a los gros
# /home/diego/Diego/memoria/YADE/Codigos/PSDBimodal
#******************************************************************

from yade import geom, utils, export, pack, __builtin__,  plot

rmean=0.01
D=rmean*10   #*50 lo disminui para corre
h=rmean*16   #*80 the same shit
R1=5.
conf=10000
load=conf*D*D
fecha="21/09/2015"
R=D/2.
H=2.*h
mn,mx=Vector3(0,0,0),Vector3(D,D,1.3*H)

num_spheres=-1
mu=0.001
Pi=500
g=9.81
rhoh=1000
rhos=2700   #ojo que anduve jugando aqui
young=1e7    #ojo que anduve jugando aqui
angfric = 30
Sd=0.51 

#psdSizes=[1.2e-5, 2e-5, 3e-5, 4e-5, 5e-5, 7e-5, 1.6e-4, 2.2e-4, 3.8e-4, 7.5e-4]
psdSizes=[rmean/R1-rmean/R1*Sd, rmean/R1+rmean/R1*Sd, rmean-rmean*Sd ,rmean+rmean*Sd]
#psdCumm=[0.0162, 0.0807, 0.1452, 0.2097, 0.3226, 0.3549, 0.4355, 0.5484, 0.7096, 1.]
psdCumm=[0.0, 0.95, 0.95, 1.]

O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=0,density=0,label='walls'))
O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=radians(angfric),density=2600,label='sph'))

walls=aabbWalls([mn,mx],thickness=0,material='walls')
wallIds=O.bodies.append(walls)

sph1=pack.SpherePack()
sph1.makeCloud(mn,mx,-1,0,num_spheres,False, 0.95,psdSizes,psdCumm,False,seed=1)
#sp.makeCloud( minCorner=mn, maxCorner=mx, rmean= -1, rRelFuzz=0, intnum=-1, periodic= False, porosity=0.65, psdSizes=Sizes, psdCumm=Cumm, distributeMass=False, seed=0)
sph1.toSimulation(material='sph')

newton=NewtonIntegrator(damping=0.2,gravity=(0,0,-9.81))
O.bodies[5].state.vel[2]=-1 # era -0.05, pero agilizamos la wa

k1=0    
k2=0
n=1
icr=0
G=0

def parar():
   carga=O.forces.f(5)[2]
   O.bodies[5].state.vel[2]=-0.01 #agilizando la cosa
   if abs(carga)>load:
    O.bodies[5].state.vel[2]=0
    O.pause()
    flow.dead=0
    flow.defTolerance=0.03
    flow.useSolver=3
    flow.permeabilityFactor=1
    flow.viscosity=mu
    flow.bndCondIsPressure=[0,0,0,0,1,1]
    flow.bndCondValue=[0,0,0,0,Pi,0]
    flow.boundaryUseMaxMin=[0,0,0,0,0,0]
    flow.meshUpdateInterval=50
    flow.viscousNormalBodyStress=1
    flow.viscousShearBodyStress=1
    flow.multithread=1
    O.run()
    muro.dead=1
     
def flujest():  
   if flow.getBoundaryFlux(4)==0: Err=100
   else: Err=(flow.getBoundaryFlux(5)+flow.getBoundaryFlux(4))/flow.getBoundaryFlux(4)*100 
   if abs(Err)<0.01:
     Qout=flow.getBoundaryFlux(5)
     Qin=flow.getBoundaryFlux(4)
     dh=O.bodies[5].bound.refPos[2]
     __builtin__.k1=mu*Qin*1./Pi/(D*D)*dh
     __builtin__.k2=g*rhoh*Qin*1./Pi/(D*D)*dh*100
     __builtin__.n=flow.porosity
     print "Qin=",Qin," k1=",__builtin__.k1 ,"k2=",__builtin__.k2 ," Porosity=",__builtin__.n
     

def aumentapresure():
    Pn=flow.bndCondValue[4]*1.02
    flow.bndCondValue=[0,0,0,0,Pn,0]
############################################################
#########################################################
n1=len(sph1)
Rad=[None]*n1
Volt=[None]*n1
V=0
vol=0


for i in range(6, n1+6):
    Rad[i-6]=O.bodies[i].shape.radius
    Volt[i-6]=O.bodies[i].shape.radius*O.bodies[i].shape.radius*O.bodies[i].shape.radius

Rad.sort()
Voltot=sum(Volt)

for i in range(0, n1):
    volume=(Rad[i]*Rad[i]*Rad[i])/Voltot*100
    vol=vol+volume
    result=repr(Rad[i])+" "+repr(vol)+"\n"
    file = open("/home/diego/memoria/YADE/Codigos/PSDBimodal/granulometryP3", "a")
    file.write(result)
    file.close()
    vol=0

for i in range(0, n1):
    V=Rad[i]*Rad[i]*Rad[i]
    vol=vol+V
    count=i
    if vol>=Voltot*.1 :
        count=i 
        D10=2*Rad[count]
        Count=0
        vol=0
        break

for i in range(0, n1):
    V=Rad[i]*Rad[i]*Rad[i]
    vol=vol+V
    count=i
    if vol>=Voltot*.15 :
        count=i 
        D15=2*Rad[count]
        lenD15=count
        Count=0
        vol=0
        break

for i in range(0, n1):
    V=Rad[i]*Rad[i]*Rad[i]
    vol=vol+V
    count=i
    if vol>=Voltot*.2 :
        count=i 
        D20=2*Rad[count]
        Count=0
        vol=0
        break

for i in range(0, n1):
    V=Rad[i]*Rad[i]*Rad[i]
    vol=vol+V
    count=i
    if vol>=Voltot*.60 :
        count=i 
        D60=2*Rad[count]
        Count=0
        vol=0
        break

for i in range(0, n1):
    V=Rad[i]*Rad[i]*Rad[i]
    vol=vol+V
    count=i
    if vol>=Voltot*.85 :
        count=i 
        D85=2*Rad[count]
        lenD85=n1-count
        Count=0
        vol=0
        break

print D10, D15, D85
##################################################################
##################################################################
despAcumFino=[None]*lenD15
despAcumFinoB=[None]*lenD15  
despAcumGros=[None]*lenD85 
despAcumGrosB=[None]*lenD85 
despFino=[None]*lenD15
despGros=[None]*lenD85  
PosAux=[Vector3]*n1
time1=0.
time2=0.

def possBefore():
    for i in range(6, n1+6):
     PosAux[i-6]=O.bodies[i].state.se3[0]
    B=__builtin__.despAcumFino
    D=__builtin__.despAcumGros
    __builtin__.despAcumFinoB=B
    __builtin__.despAcumGrosB=D
    if O.iter==0:
     C=0
    else:
     C=__builtin__.time1
    __builtin__.time2=C
    despAcumFinoMaxB=numpy.amax(__builtin__.despAcumFinoB)
    print "AcumFinoB=",despAcumFinoMaxB, "time1=", C

def ploteo():
    a1=0.
    a2=0.
    a3=0.
    d1=0.
    d2=0.
    cant1=0
    cant2=0
    cant3=0
    actual=O.iter
    inicial=graf.firstIterRun
    despMaxFino=0.
    despMaxGros=0.
    despMeanFino=0.
    despMeanGros=0.
    despAcumMaxFino=0.
    despAcumMaxGros=0.
    time=O.engines[4].timeStepUpdateInterval*O.engines[4].previousDt
    for i in range(6, n1+6):
        b=O.forces.f(i)
        rii=O.bodies[i].shape.radius
        if actual<=inicial:
         PosBefore=O.bodies[i].state.refPos
        else:
         PosBefore=PosAux[i-6]
        PosNow=O.bodies[i].state.se3[0]
        PosStart=O.bodies[i].state.refPos
        deltaVect=PosNow-PosBefore
        deltaScalar=math.sqrt(numpy.dot(deltaVect, deltaVect))
        if 2*rii<D15:
         a2=a2+math.sqrt(numpy.dot(b, b))
         despFino[cant2]=deltaScalar
         d2=d2+deltaScalar
         cant2=cant2+1
        if 2*rii>D85:
         a1=a1+math.sqrt(numpy.dot(b, b))
         despGros[cant1]=deltaScalar
         d1=d1+deltaScalar
         cant1=cant1+1
        else: 
         a3=a3+math.sqrt(numpy.dot(b, b))
#         despRest[cant3]=deltaScalar
         cant3=cant3+1
    if actual<=inicial:
     __builtin__.time1=time
     __builtin__.despAcumFino=despFino
     __builtin__.despAcumGros=despGros
    else:     
     __builtin__.time1=time+__builtin__.time2
     __builtin__.despAcumFino=despFino+__builtin__.despAcumFinoB
     __builtin__.despAcumGros=despGros+__builtin__.despAcumGrosB
    despMaxFino=numpy.amax(despFino)
    despAcumMaxFino=numpy.amax(__builtin__.despAcumFino)
    despMeanFino=d2/cant2
    despMaxGros=numpy.amax(despGros)
    despAcumMaxGros=numpy.amax(__builtin__.despAcumGros)
    despMeanGros=d1/cant1
    gross=a1*1.
    fino=a2*1.
    resto=a3*1.
    Gfp=fino/(cant2*1.)/(fino/(cant2*1.)+gross/(cant1*1.)+resto/(cant3*1.))
    __builtin__.G=Gfp
    e=flow.porosity/(1-flow.porosity)
    Sf=0.15
    nf=e/Sf
    sigma=O.forces.f(5)[2]/(D*D)
    dz=O.bodies[5].bound.refPos[2] 
    __builtin__.icr=G/(rhoh*dz*g)*(sigma*tan(radians(angfric)))*1.+nf*rhos/rhoh
    it=flow.bndCondValue[4]/(O.bodies[5].bound.refPos[2]*g*rhoh)
    print "DesFino",despMeanFino," Cant2",cant2,"desAcumMax", despAcumMaxFino, "desMax", despMaxFino
    plot.addData(dmf=despMeanFino, dMaxf=despMaxFino,dMaxAcumf=despAcumMaxFino, i=__builtin__.time1, i1=__builtin__.time1 , i2=O.iter, ic=__builtin__.icr, ii=it)
    cant1=0
    cant2=0
    cant3=0

O.engines=[
ForceResetter(),
InsertionSortCollider([Bo1_Sphere_Aabb(),Bo1_Box_Aabb()]),
InteractionLoop(
[Ig2_Sphere_Sphere_ScGeom(),Ig2_Box_Sphere_ScGeom()],
[Ip2_FrictMat_FrictMat_FrictPhys()],
[Law2_ScGeom_FrictPhys_CundallStrack()],
),
FlowEngine(dead=1, label="flow"),
GlobalStiffnessTimeStepper(active=1,timeStepUpdateInterval=100,timestepSafetyCoefficient=0.8),
PyRunner( command='flujest()', iterPeriod=500, firstIterRun=30000, label="agua"),
PyRunner( dead=1, command='aumentapresure()', iterPeriod=8000, firstIterRun=100000, label="presion"),
newton,
PyRunner(command='parar()', iterPeriod=50, firstIterRun=28100, label="muro"),
PyRunner(command='ploteo()', iterPeriod=100, label='graf',firstIterRun=50),
PyRunner(command='possBefore()', iterPeriod=100, label='auxiliar',firstIterRun=0),
]

#plot.plots={'i':('Gf'), 'i1':('Gg')}
plot.plots={'i':('dMaxf', 'dmf', 'dMaxAcumf'), 'i1':('ic', 'ii') }
plot.plot()
O.run()

