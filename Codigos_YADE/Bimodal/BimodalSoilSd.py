#**********************************************************************
#Cuadrilatero con agua
#**acercandose al modelo final #no tay ni cerca (29/09/15)
#**esferas gruesas, esferas finas, esferas gruesa y que zarpa.
#(29/09)le voy a cambiar el valor de R1 y de Sd y el modulo de young
#** Sd = 0 papeto
#14 de julio 2015 modificado 21 de julio 2015
#manoseado 18 de mayo 2016 (agregue sacar volumen)
# /home/diego/Diego/memoria/YADE
#**********************************************************************
from yade import geom, utils, export, pack, __builtin__,  plot

rmean=0.003
D=rmean*20   #*50 lo disminui para corre
h=rmean*32   #*80 the same shit
R1=4.6
conf=2000 #cargao con 2 kilopascuales (29/09) 
load=conf*D*D   #calcula carga (29/09)
fecha="29/09/2015" #fecha anterior "21/07/2015"

Sd=0.17
mu=0.001
Pi=10
g=9.81
rhoh=1000

R=D/2.
H=2.*h
mn,mx=Vector3(0,0,0),Vector3(1.01*D,1.01*D,1.3*H)
young=1e9 #estuvo un tiempo en 1e6, ya esta como dios manda xD
angfric = 30  

O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=0,density=0,label='walls'))
O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=radians(angfric),density=2600,label='sph'))

walls=aabbWalls([mn,mx],thickness=0,material='walls')
wallIds=O.bodies.append(walls)

vect=[0, 1, 1.25, 2.25, 2.5, 3.5, 3.75]
vect=1/3.9*numpy.array(vect)

cuadr1=pack.inAlignedBox((0,0,H*vect[0]),(D,D,H*vect[1])) #grueso
cuadr2=pack.inAlignedBox((0,0,H*vect[1]),(D,D,H*vect[2])) #fino
cuadr3=pack.inAlignedBox((0,0,H*vect[2]),(D,D,H*vect[3])) #grueso
cuadr4=pack.inAlignedBox((0,0,H*vect[3]),(D,D,H*vect[4])) #fino
cuadr5=pack.inAlignedBox((0,0,H*vect[4]),(D,D,H*vect[5])) #grueso
cuadr6=pack.inAlignedBox((0,0,H*vect[5]),(D,D,H*vect[6])) #fino

sph1=pack.randomDensePack(cuadr1,spheresInCell=1000,radius=rmean,rRelFuzz=Sd,returnSpherePack=True)
sph2=pack.randomDensePack(cuadr2,spheresInCell=2000,radius=rmean/R1,rRelFuzz=Sd,returnSpherePack=True)
sph3=pack.randomDensePack(cuadr3,spheresInCell=1000,radius=rmean,rRelFuzz=Sd,returnSpherePack=True)
sph4=pack.randomDensePack(cuadr4,spheresInCell=2000,radius=rmean/R1,rRelFuzz=Sd,returnSpherePack=True)
sph5=pack.randomDensePack(cuadr5,spheresInCell=1000,radius=rmean,rRelFuzz=Sd,returnSpherePack=True)
sph6=pack.randomDensePack(cuadr6,spheresInCell=2000,radius=rmean/R1,rRelFuzz=Sd,returnSpherePack=True)

sph1.toSimulation(material='sph')
sph2.toSimulation(material='sph')
sph3.toSimulation(material='sph')
sph4.toSimulation(material='sph')
sph5.toSimulation(material='sph')
sph6.toSimulation(material='sph')

n1=len(sph1)
n2=len(sph2)
n3=len(sph3)
n4=len(sph4)
n5=len(sph5)
n6=len(sph6)

Vchi=(n2+n4+n6)*(rmean/R1)**3
Vgran=(n1+n3+n5)*(rmean)**3
R2=Vchi/Vgran

O.bodies[5].state.vel[2]=-0.05

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
    b=0
    V1=0
    V2=0
    V3=0
    V4=0
    V5=0
    V6=0
    for i in range(6, n1+6):
        b=O.forces.f(i)
        a1=a1+math.sqrt(numpy.dot(b, b))
        V1=V1+4/3*numpy.pi*O.bodies[i].shape.radius**3
    for i in range(n1+6, n1+n2+6):
        b=O.forces.f(i)
        a2=a2+math.sqrt(numpy.dot(b, b))
        V2=V2+4/3*numpy.pi*O.bodies[i].shape.radius**3
    for i in range(n1+n2+6, n1+n2+n3+6):
        b=O.forces.f(i)
        a3=a3+math.sqrt(numpy.dot(b, b))
        V3=V3+4/3*numpy.pi*O.bodies[i].shape.radius**3
    for i in range(n1+n2+n3+6, n1+n2+n3+n4+6):
        b=O.forces.f(i)
        a4=a4+math.sqrt(numpy.dot(b, b))
        V4=V4+4/3*numpy.pi*O.bodies[i].shape.radius**3
    for i in range(n1+n2+n3+n4+6, n1+n2+n3+n4+n5+6):
        b=O.forces.f(i)
        a5=a5+math.sqrt(numpy.dot(b, b))
        V5=V5+4/3*numpy.pi*O.bodies[i].shape.radius**3
    for i in range(n1+n2+n3+n4+n5+6, n1+n2+n3+n4+n5+n6+6):
        b=O.forces.f(i)
        a6=a6+math.sqrt(numpy.dot(b, b))
        V6=V6+4/3*numpy.pi*O.bodies[i].shape.radius**3
    
    Ps=O.forces.f(5)[2]/(D*D)
    fino=a2/n2+a4/n4+a6/n6
    gross=a1/n1+a3/n3+a5/n5
    G=fino/(fino+gross)
    Gbig=gross/(fino+gross)
#    fino=a2+a4+a6
#    gross=a1+a3+a5
#    G=fino/(fino+gross)
#    Gbig=gross/(fino+gross)
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

