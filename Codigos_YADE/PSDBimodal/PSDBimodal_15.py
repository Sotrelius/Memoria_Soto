#**********************************************************************
#Cuadrilatero con agua, PSD bimodal
#BIMODALPRUEBA3 PERO PARA VELOCITY.
#plotear cambios de velocidad 
#05 de octubre 2015
# /home/diego/Diego/memoria/YADE/Codigos/PSDBimodal
#******************************************************************

from yade import geom, utils, export, pack, __builtin__,  plot

rmean=0.01
D=rmean*10   #*50 lo disminui para corre
h=rmean*16   #*80 the same shit
R1=1.5
conf=10000
load=conf*D*D
fecha="21/09/2015"
R=D/2.
H=2.*h
mn,mx=Vector3(0,0,0),Vector3(D,D,1.3*H)

num_spheres=-1
mu=0.001
Pi=80
g=9.81
rhoh=1000
rhos=2700
young=1e7 
angfric = 30
Sd=0.05

#psdSizes=[1.2e-5, 2e-5, 3e-5, 4e-5, 5e-5, 7e-5, 1.6e-4, 2.2e-4, 3.8e-4, 7.5e-4]
psdSizes=[rmean/R1-rmean/R1*Sd, rmean/R1+rmean/R1*Sd, rmean-rmean*Sd ,rmean+rmean*Sd]
#psdCumm=[0.0162, 0.0807, 0.1452, 0.2097, 0.3226, 0.3549, 0.4355, 0.5484, 0.7096, 1.]
psdCumm=[0.0, 0.4, 0.4, 1.]

O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=0,density=0,label='walls'))
O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=radians(angfric),density=2600,label='sph'))

walls=aabbWalls([mn,mx],thickness=0,material='walls')
wallIds=O.bodies.append(walls)

sph1=pack.SpherePack()
sph1.makeCloud(mn,mx,-1,0,num_spheres,False, 0.95,psdSizes,psdCumm,False,seed=1)
#sp.makeCloud( minCorner=mn, maxCorner=mx, rmean= -1, rRelFuzz=0, intnum=-1, periodic= False, porosity=0.65, psdSizes=Sizes, psdCumm=Cumm, distributeMass=False, seed=0)
sph1.toSimulation(material='sph')

newton=NewtonIntegrator(damping=0.2,gravity=(0,0,-9.81))
O.bodies[5].state.vel[2]=-0.1 # era -0.05, pero agilizamos la wa

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
volp=0


for i in range(6, n1+6):
    Rad[i-6]=O.bodies[i].shape.radius
    Volt[i-6]=O.bodies[i].shape.radius*O.bodies[i].shape.radius*O.bodies[i].shape.radius

Rad.sort()
Voltot=sum(Volt)

for i in range(0, n1):
    volume=(Rad[i]*Rad[i]*Rad[i])/Voltot*100
    volp=volp+volume
    result=repr(Rad[i])+" "+repr(volp)+"\n"
    file = open("/home/diego/memoria/YADE/Codigos/PSDBimodal/gran_15", "a")
    file.write(result)
    file.close()

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
        lenD85=n1-lenD15 #largo arreglo
        Count=0
        vol=0
        break

print D10, D15, D85
##################################################################
##################################################################
#############################################################################

velFino=[None]*lenD15
velGros=[None]*lenD85  
PosAux=[Vector3]*n1
time1=0.

#############################################################################

def ploteo():
    a1=0.
    a2=0.
    a3=0.
    d1=0.
    d2=0.
    t1=0.
    t2=0.
    t3=0.
    cant1=0
    cant2=0
    cant3=0
    actual=O.iter
    inicial=graf.firstIterRun
    velMaxFino=0.
    velMaxGros=0.
    velMeanFino=0.
    velMeanGros=0.
    for i in range(6, n1+6):
        b=O.forces.f(i)
        rii=O.bodies[i].shape.radius
        tau=O.forces.f(i)/(pi*O.bodies[i].shape.radius**2)
        vel=O.bodies[i].state.vel
        velScalar=math.sqrt(numpy.dot(vel, vel))
        if 2*rii<D15:
         a2=a2+math.sqrt(numpy.dot(b, b))
         t2=t2+math.sqrt(numpy.dot(tau, tau))
         velFino[cant2]=velScalar
         d2=d2+velScalar
         cant2=cant2+1
        if 2*rii>=D15:
         a1=a1+math.sqrt(numpy.dot(b, b))
         t1=t1+math.sqrt(numpy.dot(tau, tau))
         velGros[cant1]=velScalar
         d1=d1+velScalar
         cant1=cant1+1

    __builtin__.time1=O.time
    velMaxFino=numpy.amax(velFino)
    velMeanFino=d2/cant2
    velMaxGros=numpy.amax(velGros)
    velMeanGros=d1/cant1

    gross=a1*1.
    fino=a2*1.
    resto=a3*1.
    Ff=fino/(gross+fino+resto+1e-10)
    Fg=(gross+resto)/(gross+fino+resto+1e-10)
    Gfp=fino/(cant2*1.)/(fino/(cant2*1.)+gross/(cant1*1.))
    Ggp=(gross/cant1*1.)/(fino/(cant2*1.)+gross/(cant1*1.))
    __builtin__.G=Gfp

    tensfp=t2/(cant2*1.)/(t2/(cant2*1.)+t1/(cant1*1.))
    tensgp=(t1/cant1*1.)/(t2/(cant2*1.)+t1/(cant1*1.))
    tensf=t2/(t1+t2+1e-10)
    tensg=(t1)/(t1+t2+1e-10)

    e=flow.porosity/(1-flow.porosity)
    Sf=0.15
    nf=e/Sf
    sigma=O.forces.f(5)[2]/(D*D)
    dz=O.bodies[5].bound.refPos[2] 
    __builtin__.icr=G/(rhoh*dz*g)*(sigma*tan(radians(angfric)))*1.+nf*rhos/rhoh
    __builtin__.icc=tensf/(rhoh*dz*g)*(sigma*tan(radians(angfric)))*1.+nf*rhos/rhoh
    it=flow.bndCondValue[4]/(O.bodies[5].bound.refPos[2]*g*rhoh)

    plot.addData(Vmf=velMeanFino, VMaxf=velMaxFino, Vmg=velMeanGros, VMaxg=velMaxGros, i=__builtin__.time1, i1=__builtin__.time1 , i2=__builtin__.time1, i3=__builtin__.time1, ic=__builtin__.icr, ii=it, Gf=Gfp, Gg=Ggp, Tf=tensfp, Tg=tensgp)
    print "time= ", __builtin__.time1
    print "Gf=",Gfp," Gg",Ggp,"Tf=",tensfp,"Tg=",tensgp
    cant1=0
    cant2=0
    cant3=0


#############################################################################
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
]

##############################################################################
plot.plots={'i':('Gf', 'Gg'), 'i1':('Tf','Tg'), 'i2':('VMaxf', 'Vmf', 'VMaxg', 'Vmg'), 'i3':('ic', 'ii') }
plot.plot()
#plot.plots={'i':('VMaxf', 'Vmf', 'VMaxg', 'Vmg'), 'i1':('ic', 'ii') }
O.run()
#yade.plot.saveDataTxt(fileName, vars=None)
