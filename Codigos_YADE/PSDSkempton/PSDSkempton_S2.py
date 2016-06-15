#**********************************************************************
#Cuadrilatero con agua, PSD bimodal
#Prueba granulometria real piping para gradientes criticos
#plotear cambios de velocidad 
#10 de febrero 2016

# /home/diego/memoria/YADE/Codigos/PSDSkempton
#******************************************************************

from yade import geom, utils, export, pack, __builtin__,  plot

#################################################################
##################  Variables globales  #########################
#################################################################

D=0.005  #dimension final 0.05
H=0.50   #dimension final ?????
conf=10000     #10[KPa]
load=conf*D*D
fecha="02/03/2016"
mn,mx=Vector3(0,0,0),Vector3(D,D,H)
num_spheres=-1
mu=0.001
Pi=10
g=9.81
rhoh=1000
rhos=2600
young=1e7 
angfric = 30
Sd=0.68
Vel=H/4 

###################################################################
############## granulometria y materiales #########################
##################################################################

psdSizes=[1e-4, 2e-4, 3e-4, 4e-4, 5e-4 , 6e-4, 1e-3]
psdCumm=[0.0, 0.08, 0.2, 0.4, 0.6, 0.8 , 1.]

O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=0,density=0,label='walls'))
O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=radians(angfric),density=rhos,label='sph'))

walls=aabbWalls([mn,mx],thickness=0,material='walls')
wallIds=O.bodies.append(walls)
mx1=Vector3(D,D,H/64*1.4)
sph1=pack.SpherePack()
sph1.makeCloud(mn,mx1,-1,0,num_spheres,False, 0.65,psdSizes,psdCumm,True,seed=1)
#sp.makeCloud( minCorner=mn, maxCorner=mx, rmean= -1, rRelFuzz=0, intnum=-1, periodic= False, porosity=0.65, psdSizes=Sizes, psdCumm=Cumm, distributeMass=False, seed=0)
sph1.toSimulation(material='sph')

##################################################################

newton=NewtonIntegrator(damping=0.2,gravity=(0,0,-9.81))
O.bodies[5].state.vel[2]=0 # era -0.05, pero agilizamos la wa

############################################################################
################ Caracteristicas granulometricas ###########################
############################################################################
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
    file = open("/home/diego/memoria/YADE/Codigos/PSDSkempton/granSkempton_S2a", "a")
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

########################################################################
################  control de la modelacion ############################
######################################################################

k1=0    
k2=0
n=1
icr=0
icc=0
G=0

def parar():
   carga=O.forces.f(5)[2]
   if abs(carga)>0.65*load:
    O.bodies[5].state.vel[2]=-Vel/2 #agilizando la cosa
   if abs(carga)>0.85*load:
    O.bodies[5].state.vel[2]=-Vel/4
   if abs(carga)>0.95*load:
    O.bodies[5].state.vel[2]=-Vel/10
   if abs(carga)>1.03*load:
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
    flow.multithread=1
    flow.viscousShearBodyStress=1
    print "time= ", __builtin__.time1
    O.save('/home/diego/memoria/YADE/Codigos/PSDSkempton/granSkempton_S2/S2_conf.bz2')
    O.run()
    muro.dead=1
##########################################################################

def TensionesR():
   O.pause()
   for i in range(6, n1+6):
        F=O.forces.f(i)
        f=math.sqrt(numpy.dot(F, F))
        R=O.bodies[i].shape.radius
        Tens=f/(pi*R*R)
        N=O.iter
        id=i
        result=repr(R)+" "+repr(Tens)+" "+repr(i)+"\n"
        ruta2="/home/diego/memoria/YADE/Codigos/PSDSkempton/granSkempton_S2/tension_P"+repr(N)
        file = open(ruta2, "a")
        file.write(result)
        file.close()
   O.run()


 O.save('/home/diego/memoria/YADE/Codigos/PSDSkempton/granSkempton_D/D_corr.bz2') 

##########################################################################

def perfilVertTens():
    dz=O.bodies[5].bound.refPos[2]
    vert=numpy.linspace(0,dz,100)
    N=O.iter
    ruta="/home/diego/memoria/YADE/Codigos/PSDSkempton/granSkempton_S2/perfil_"+repr(N)
    for i in range(0, 100):
        alfa=vert[i]
        Tensf=0.
        Tensg=0.
        count1=1e-11
        count2=1e-11
        for j in range(6,n1+6):
            Radio=O.bodies[j].shape.radius
            zeta=O.bodies[j].state.refPos[2]
            equis=O.bodies[j].state.refPos[0]
            yeta=O.bodies[j].state.refPos[1]
            force=O.forces.f(i)
            Forc=math.sqrt(numpy.dot(force, force))
            if abs(zeta-alfa)<=Radio:
             if Radio<=D15:
              areaf=pi*(Radio**2-(zeta-alfa)**2)
              T1=Forc/areaf
              Tensf=Tensf+T1
              count1=count1+1
             if Radio>D15:
              areag=pi*(Radio**2-(zeta-alfa)**2)
              T2=Forc/areag
              Tensg=Tensg+T2
              count2=count2+1
        Tensfp=Tensf/count1
        Tensgp=Tensg/count2
        Tmpf=Tensfp/(Tensfp+Tensgp+1e-15)
        Tmpg=Tensgp/(Tensfp+Tensgp+1e-15)
        result=repr(alfa)+" "+repr(Tensf)+" "+repr(Tensg)+" "+repr(Tensfp)+" "+repr(Tensgp)+" "+repr(Tmpf)+" "+repr(Tmpg)+"\n"
        file = open(ruta, "a")
        file.write(result)
        file.close()
#############################################################################

def aumentapresure():  #cuando lo activo??? def iter periodo
    Pn=flow.bndCondValue[4]*1.02
    flow.bndCondValue=[0,0,0,0,Pn,0]

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
        else: 
         a3=a3+math.sqrt(numpy.dot(b, b))
         t3=t3+math.sqrt(numpy.dot(tau, tau))
         cant3=cant3+1
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
    Gfp=fino/(cant2*1.)/(fino/(cant2*1.)+gross/(cant1*1.)+resto/(cant3*1.))
    Ggp=(gross/cant1*1.+resto/cant3*1.)/(fino/(cant2*1.)+gross/(cant1*1.)+resto/(cant3*1.))
    __builtin__.G=Gfp

    tensfp=t2/(cant2*1.)/(t2/(cant2*1.)+t1/(cant1*1.)+t3/(cant3*1.))
    tensgp=(t1/cant1*1.+t3/cant3*1.)/(t2/(cant2*1.)+t1/(cant1*1.)+t3/(cant3*1.))
    tensf=t2/(t1+t2+t3+1e-10)
    tensg=(t1+t3)/(t1+t2+t3+1e-10)

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

############################################################################
#################  motor de la simulacion ##################################
############################################################################
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
PyRunner( dead=1, command='aumentapresure()', iterPeriod=8000, firstIterRun=100000, label="presion"),
newton,
PyRunner(command='perfilVertTens', label="perfilV", dead=1),
PyRunner(command='TensionesR', label="distProb", dead=1),
PyRunner(command='parar()', iterPeriod=50, firstIterRun=90100, label="muro"),
PyRunner(command='ploteo()', iterPeriod=300, label='graf',firstIterRun=50),
]

##############################################################################
plot.plots={'i':('Gf', 'Gg'), 'i1':('Tf','Tg'), 'i2':('VMaxf', 'Vmf', 'VMaxg', 'Vmg'), 'i3':('ic', 'ii') }
plot.plot()
#plot.plots={'i':('VMaxf', 'Vmf', 'VMaxg', 'Vmg'), 'i1':('ic', 'ii') }
O.run()
#yade.plot.saveDataTxt(fileName, vars=None)

