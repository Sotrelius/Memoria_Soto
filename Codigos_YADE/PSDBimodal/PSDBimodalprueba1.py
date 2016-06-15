#**********************************************************************
#Cuadrilatero con agua, PSD bimodal
#acoplado con flujo
#09 de septiembre 2015
# /home/diego/Diego/memoria/YADE
#******************************************************************

from yade import geom, utils, export, pack, __builtin__,  plot

rmean=0.015  #Revisar velocidad cuando cambie orden de magnitud de rmean
D=rmean*10   #*50 lo disminui para corre
h=rmean*18   #*80 the same shit
R1=6.
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
rhos=2600
young=1e9 
angfric = 30
Sd=0.17 

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
O.bodies[5].state.vel[2]=-8 # era -0.05, pero agilizamos la wa
#Revisar velocidad cuando cambie orden de magnitud de rmean
k1=0    
k2=0
n=1
ki=1
kf=2
icr=0
G=0

def parar():
   carga=O.forces.f(5)[2]
   O.bodies[5].state.vel[2]=-0.1 #agilizando la cosa
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
   if abs(Err)<0.1:
     Qout=flow.getBoundaryFlux(5)
     Qin=flow.getBoundaryFlux(4)
     dh=O.bodies[5].bound.refPos[2]
     __builtin__.k1=mu*Qin*1./Pi/(D*D)*dh
     __builtin__.k2=g*rhoh*Qin*1./Pi/(D*D)*dh*100
     __builtin__.n=flow.porosity
     print "Qin=",Qin," k1=",__builtin__.k1 ,"k2=",__builtin__.k2 ," Porosity=",__builtin__.n
     

def kant():
   Qin=flow.getBoundaryFlux(4)
   dh=O.bodies[5].bound.refPos[2]
   if Qin==0: ki=1000
   else: __builtin__.ki=g*rhoh*Qin*1./Pi/(D*D)*dh*100

def final():
   Qin=flow.getBoundaryFlux(4)
   dh=O.bodies[5].bound.refPos[2]
   __builtin__.kf=g*rhoh*Qin*1./Pi/(D*D)*dh*100
   err=__builtin__.kf-__builtin__.ki
   if abs(err)<1e-3:
    O.pause() 
    file = open("/home/diego/memoria/Codigos/analisisPSD/resulconf", "a")
    result=repr(Sd)+" "+repr(__builtin__.k1)+" "+repr(__builtin__.k2)+" "+repr(__builtin__.n)+" "+repr(Qin)+" "+repr(D10)+" "+repr(D20)+" "+repr(D85)+" "+repr(rmean)+" "+fecha+"\n"
    file.write(result)
    file.close()
#    vtk=export.VTKExporter('/home/diego/memoria/Codigos/analisisRM/resultconf50')
#    vtk.exportSpheres('all',what=[])
#    O.exitNoBacktrace()
    
def ploteo():
    a1=0.
    a2=0.
    a3=0.
    cant1=0.
    cant2=0.
    cant3=0.
    for i in range(6, n1+6):
        b=O.forces.f(i)
        rii=O.bodies[i].shape.radius
        if 2*rii<D15:
         a2=a2+math.sqrt(numpy.dot(b, b))
         cant2=cant2+1
        if 2*rii>D85:
         a1=a1+math.sqrt(numpy.dot(b, b))
         cant1=cant1+1
        else: 
         a3=a3+math.sqrt(numpy.dot(b, b))
         cant3=cant3+1
    gross=a1*1.
    fino=a2*1.
    resto=a3*1.
    Gfin =fino/(fino+gross+resto)
    Ggros=gross/(fino+gross+resto)
    Gfp=fino/cant2/(fino/cant2+gross/cant1+resto/cant3)
    Ggp=gross/cant1/(fino/cant2+gross/cant1+resto/cant3)
    __builtin__.G=Gfp
    e=flow.porosity/(1-flow.porosity)
    Sf=0.15
    nf=e/Sf
    sigma=O.forces.f(5)[2]/(D*D)
    dz=O.bodies[5].bound.refPos[2]
    __builtin__.icr=G/(rhoh*dz*g)*(sigma*tan(radians(angfric)))*1.+nf*rhos/rhoh
    it=flow.bndCondValue[4]/(O.bodies[5].bound.refPos[2]*g*rhoh)
    time1=O.iter
    plot.addData(Gf=Gfin, i=O.iter, i1=O.iter, i2=O.iter, Gg=Ggros, Gfm=Gfp, Ggm=Ggp, ic=__builtin__.icr, ii=it)

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
PyRunner( command='flujest()', iterPeriod=500, firstIterRun=50000, label="agua"),
newton,
PyRunner(command='parar()', iterPeriod=50, firstIterRun=31100, label="muro"),
PyRunner(command='kant()', iterPeriod=200, firstIterRun=51000, label="kini"),
PyRunner(command='ploteo()', iterPeriod=50),
PyRunner(command='final()', iterPeriod=200, firstIterRun=51300, label="kfin")
]

#plot.plots={'i':('Gf'), 'i1':('Gg')}
plot.plots={'i':('Gfm', 'Ggm'), 'i2':('ic', 'ii') }
plot.plot()
O.run()

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
        Count=0
        vol=0
        break

print D10, D15, D85

