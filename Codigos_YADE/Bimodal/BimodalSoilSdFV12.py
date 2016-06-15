#**********************************************************************
#Cuadrilatero con agua
#**acercandose al modelo final
#**esferas gruesas, esferas finas, esferas gruesa y que zarpa.
#** Sd = 0 papeto
#14 de julio 2015 modificado 21 de julio 2015
#ultima modificacion 4 de agosto 2015
#
# /home/diego/Diego/memoria/YADE
#**********************************************************************
from yade import geom, utils, export, pack, __builtin__,  plot

rmean=0.003
D=rmean*20   #*50 lo disminui para corre
h=rmean*32   #*80 the same shit
R1=3
load=5e1
fecha="11/08/2015"

Sd=0.3
mu=0.001
Pi=1
g=9.81
rhoh=1000

R=D/2.
H=2.*h
mn,mx=Vector3(0,0,0),Vector3(1.01*D,1.01*D,1.3*H)
young=1e6 #1e9
angfric = 30  

O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=0,density=0,label='walls'))
O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=radians(angfric),density=2600,label='sph'))

walls=aabbWalls([mn,mx],thickness=0,material='walls')
wallIds=O.bodies.append(walls)

vect=[0, 1, 1.25, 2.25, 2.5, 3.5, 3.75, 4.75, 5., 6., 6.25, 7.25, 7.5]
vect=1/7.25*numpy.array(vect)

cuadr1=pack.inAlignedBox((0,0,H*vect[0]),(D,D,H*vect[1])) #grueso
cuadr2=pack.inAlignedBox((0,0,H*vect[1]),(D,D,H*vect[2])) #fino
cuadr3=pack.inAlignedBox((0,0,H*vect[2]),(D,D,H*vect[3])) #grueso
cuadr4=pack.inAlignedBox((0,0,H*vect[3]),(D,D,H*vect[4])) #fino
cuadr5=pack.inAlignedBox((0,0,H*vect[4]),(D,D,H*vect[5])) #grueso
cuadr6=pack.inAlignedBox((0,0,H*vect[5]),(D,D,H*vect[6])) #fino
cuadr7=pack.inAlignedBox((0,0,H*vect[6]),(D,D,H*vect[7])) #grueso
cuadr8=pack.inAlignedBox((0,0,H*vect[7]),(D,D,H*vect[8])) #fino
cuadr9=pack.inAlignedBox((0,0,H*vect[8]),(D,D,H*vect[9])) #grueso
cuadr10=pack.inAlignedBox((0,0,H*vect[9]),(D,D,H*vect[10])) #fino
cuadr11=pack.inAlignedBox((0,0,H*vect[10]),(D,D,H*vect[11])) #grueso
cuadr12=pack.inAlignedBox((0,0,H*vect[11]),(D,D,H*vect[12])) #fino

sph1=pack.randomDensePack(cuadr1,spheresInCell=1000,radius=rmean,rRelFuzz=Sd,returnSpherePack=True)
sph2=pack.randomDensePack(cuadr2,spheresInCell=2000,radius=rmean/R1,rRelFuzz=Sd,returnSpherePack=True)
sph3=pack.randomDensePack(cuadr3,spheresInCell=1000,radius=rmean,rRelFuzz=Sd,returnSpherePack=True)
sph4=pack.randomDensePack(cuadr4,spheresInCell=2000,radius=rmean/R1,rRelFuzz=Sd,returnSpherePack=True)
sph5=pack.randomDensePack(cuadr5,spheresInCell=1000,radius=rmean,rRelFuzz=Sd,returnSpherePack=True)
sph6=pack.randomDensePack(cuadr6,spheresInCell=2000,radius=rmean/R1,rRelFuzz=Sd,returnSpherePack=True)
sph7=pack.randomDensePack(cuadr7,spheresInCell=1000,radius=rmean,rRelFuzz=Sd,returnSpherePack=True)
sph8=pack.randomDensePack(cuadr8,spheresInCell=2000,radius=rmean/R1,rRelFuzz=Sd,returnSpherePack=True)
sph9=pack.randomDensePack(cuadr9,spheresInCell=1000,radius=rmean,rRelFuzz=Sd,returnSpherePack=True)
sph10=pack.randomDensePack(cuadr10,spheresInCell=2000,radius=rmean/R1,rRelFuzz=Sd,returnSpherePack=True)
sph11=pack.randomDensePack(cuadr11,spheresInCell=1000,radius=rmean,rRelFuzz=Sd,returnSpherePack=True)
sph12=pack.randomDensePack(cuadr12,spheresInCell=2000,radius=rmean/R1,rRelFuzz=Sd,returnSpherePack=True)

sph1.toSimulation(material='sph')
sph2.toSimulation(material='sph')
sph3.toSimulation(material='sph')
sph4.toSimulation(material='sph')
sph5.toSimulation(material='sph')
sph6.toSimulation(material='sph')
sph7.toSimulation(material='sph')
sph8.toSimulation(material='sph')
sph9.toSimulation(material='sph')
sph10.toSimulation(material='sph')
sph11.toSimulation(material='sph')
sph12.toSimulation(material='sph')


n1=len(sph1)
n2=len(sph2)
n3=len(sph3)
n4=len(sph4)
n5=len(sph5)
n6=len(sph6)
n7=len(sph7)
n8=len(sph8)
n9=len(sph9)
n10=len(sph10)
n11=len(sph11)
n12=len(sph12)

Vchi=(n2+n4+n6+n8+n10+n12)*(rmean/R1)**3
Vgran=(n1+n3+n5+n7+n9+n11)*(rmean)**3
R2=Vchi/Vgran

O.bodies[5].state.vel[2]=-0.1

def parar():
   carga=O.forces.f(5)[2]
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
    flow.iterPeriod=10
    flow.meshUpdateInterval=10
    flow.pumpTorque=1
    flow.viscousNormalBodyStress=1
    flow.viscousShearBodyStress=1
    O.run()
    muro.dead=1
    Saveflow.dead=0
    SaveEsf.dead=0
    print O.iter

def ploteo():
    a1=0
    a2=0
    a3=0
    a4=0
    a5=0
    a6=0
    a7=0
    a8=0
    a9=0
    a10=0
    a11=0
    a12=0
    b=0
    for i in range(5, n1+5):
        b=O.forces.f(i)[2]
        a1=a1+abs(b)
    corch=n1+5
    for i in range(corch, corch+n2):
        b=O.forces.f(i)[2]
        a2=a2+abs(b)
    corch=n1+5+n2
    for i in range(corch, corch+n3):
        b=O.forces.f(i)[2]
        a3=a3+abs(b)
    corch=n1+5+n2+n3
    for i in range(corch, corch+n4):
        b=O.forces.f(i)[2]
        a4=a4+abs(b)
    corch=n1+5+n2+n3+n4
    for i in range(corch, corch+n5):
        b=O.forces.f(i)[2]
        a5=a5+abs(b)
    corch=n1+5+n2+n3+n4+n5
    for i in range(corch, corch+n6):
        b=O.forces.f(i)[2]
        a6=a6+abs(b)
    corch=n1+5+n2+n3+n4+n5+n6
    for i in range(corch, corch+n7):
        b=O.forces.f(i)[2]
        a7=a7+abs(b)
    corch=n1+5+n2+n3+n4+n5+n6+n7
    for i in range(corch, corch+n8):
        b=O.forces.f(i)[2]
        a8=a8+abs(b)
    corch=n1+5+n2+n3+n4+n5+n6+n7+n8
    for i in range(corch, corch+n9):
        b=O.forces.f(i)[2]
        a9=a9+abs(b)
    corch=n1+5+n2+n3+n4+n5+n6+n7+n8+n9
    for i in range(corch, corch+n10):
        b=O.forces.f(i)[2]
        a10=a10+abs(b)
    corch=n1+5+n2+n3+n4+n5+n6+n7+n8+n10
    for i in range(corch, corch+n11):
        b=O.forces.f(i)[2]
        a11=a11+abs(b)
    corch=n1+5+n2+n3+n4+n5+n6+n7+n8+n10+n11
    for i in range(corch, corch+n12):
        b=O.forces.f(i)[2]
        a12=a12+abs(b)

#    fino=a2/n2+a4/n4+a6/n6
#    gross=a1/n1+a3/n3+a5/n5
#    G=fino/(fino+gross)
#    Gbig=gross/(fino+gross)
    fino=a2+a4+a6+a8+a10+a12
    gross=a1+a3+a5+a7+a9+a11
    G=fino/(fino+gross)
    Gbig=gross/(fino+gross)
    time1=O.iter
    plot.addData(Gt=G,i=O.iter, i1=O.iter, Gb=Gbig)
    
newton=NewtonIntegrator(damping=0.2,gravity=(0,0,-9.81))

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
PyRunner(command='parar()', iterPeriod=50, label="muro"),
PyRunner(dead=1, command='flow.saveVtk()', iterPeriod=500, label="Saveflow"),
#VTKRecorder(dead=1, fileName='Esfestr2-vtk-',recorders=['all'],iterPeriod=500, label="SaveEsf"),
PyRunner(command='ploteo()', iterPeriod=50),
newton
]

plot.plots={'i':('Gt'), 'i1':('Gb')}
plot.plot()
O.run()
