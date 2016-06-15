############################
# Author: Paulo Herrera
# Modify: DNS Rodriguez #segunda modificacion de soteiro
# Date: 20/May/2015
# ModDate: 25/Ago/2015 #ni me acordaba que la habia modificado.
# primera modificacion de soteiro, correr varios script con las mismas caracteristicas, el siguiente paso, meter scripts aca y cambiarle parametros directamente desde la tabla.
####################################################

from subprocess import call
import multiprocessing as mp
import os

def each_call(input_params):
    ''' Call for each command to execute '''
    name, process, Rmean, Sd, conf, Pi = input_params #le agregue mis putos parametros madafaka
    RepRmean=repr(Rmean)
    RepSd=repr(Sd)
    Rmean2=RepRmean[2:]
    archivo='/home/diego/memoria/YADE/Codigos/Runs/PsdVarPRFX'+repr(process)
    file = open(archivo, 'a')
    file.write("from yade import geom, utils, export, pack, __builtin__, plot\n"
"rmean="+repr(Rmean)+"\n"
"D=rmean*45.\n" 
"h=rmean*80.\n"
"conf="+repr(conf)+"\n"
"load=conf*D*D\n"
"fecha='21/08/2015'\n"
"\n"
"Sd="+repr(Sd)+"\n"
"mu=0.001\n"
"Pi="+repr(Pi)+"\n"
"g=9.81\n"
"rhoh=1000\n"
"\n"
"R=D/2.\n"
"H=2.*h\n"
"mn,mx=Vector3(0,0,0),Vector3(D,D,H)\n"
"young=1e6\n"
"finalFricDegree = 30  \n"
"\n"
"O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=0,density=0,label='walls'))\n"
"O.materials.append(FrictMat(young=young,poisson=0.5,frictionAngle=radians(finalFricDegree),density=2600,label='sph'))\n"
"\n"
"walls=aabbWalls([mn,mx],thickness=0,material='walls')\n"
"wallIds=O.bodies.append(walls)\n"
"\n"
"cuadr=pack.inAlignedBox((0,0,0),(D,D,H))\n"
"spheres=pack.randomDensePack(cuadr,spheresInCell=3000,radius=rmean,rRelFuzz=Sd,returnSpherePack=True)\n"
"\n"
"spheres.toSimulation(material='sph')\n"
"\n"
"newton=NewtonIntegrator(damping=0.2,gravity=(0,0,-9.81))\n"
"O.bodies[5].state.vel[2]=-0.08 # era -0.05, pero agilizamos la wa\n"
"\n"
"k1=0    \n"
"k2=0\n"
"n=1\n"
"ki=1\n"
"kf=2\n"
"\n"
"def parar():\n"
"   carga=O.forces.f(5)[2]\n"
"   O.bodies[5].state.vel[2]=-0.03 #agilizando la cosa\n"
"   if abs(carga)>load:\n"
"    O.bodies[5].state.vel[2]=0\n"
"    O.pause()\n"
"    flow.dead=0\n"
"    flow.defTolerance=0.03\n"
"    flow.useSolver=3\n"
"    flow.permeabilityFactor=1\n"
"    flow.viscosity=mu\n"
"    flow.bndCondIsPressure=[0,0,0,0,1,1]\n"
"    flow.bndCondValue=[0,0,0,0,0,Pi]\n"
"    flow.boundaryUseMaxMin=[0,0,0,0,0,0]\n"
"    flow.meshUpdateInterval=50\n"
"    O.run()\n"
"    muro.dead=1\n"
"     \n"
"def flujest():  \n"
"   if flow.getBoundaryFlux(4)==0: Err=100\n"
"   else: Err=(flow.getBoundaryFlux(5)+flow.getBoundaryFlux(4))/flow.getBoundaryFlux(4)*100 \n"
"   if abs(Err)<0.1:\n"
"     Qout=flow.getBoundaryFlux(5)\n"
"     Qin=flow.getBoundaryFlux(4)\n"
"     dh=O.bodies[5].bound.refPos[2]\n"
"     __builtin__.k1=mu*Qin*1./Pi/(D*D)*dh\n"
"     __builtin__.k2=g*rhoh*Qin*1./Pi/(D*D)*dh*100\n"
"     __builtin__.n=flow.porosity\n"
"     print 'Qin=',Qin,' k1=',__builtin__.k1 ,'k2=',__builtin__.k2 ,' Porosity=',__builtin__.n\n"
"\n"     
"def kant():\n"
"   Qin=flow.getBoundaryFlux(4)\n"
"   dh=O.bodies[5].bound.refPos[2]\n"
"   if Qin==0: ki=1000\n"
"   else: __builtin__.ki=g*rhoh*Qin*1./Pi/(D*D)*dh*100\n"
"\n"
"def final():\n"
"   Qin=flow.getBoundaryFlux(4)\n"
"   dh=O.bodies[5].bound.refPos[2]\n"
"   __builtin__.kf=g*rhoh*Qin*1./Pi/(D*D)*dh*100\n"
"   err=__builtin__.kf-__builtin__.ki\n"
"   if abs(err)<1e-3:\n"
"    O.pause()\n" 
"    file = open('/home/diego/memoria/Codigos/analisisSD/resul"+Rmean2+"', 'a')\n"
"    result=repr(Sd)+' '+repr(__builtin__.k1)+' '+repr(__builtin__.k2)+' '+repr(__builtin__.n)+' '+repr(Qin)+' '+repr(D10)+' '+repr(D20)+' '+repr(D85)+' '+repr(rmean)+' '+repr(Pi)+' '+repr(conf)+' '+fecha+'\\n'\n"
"    file.write(result)\n"
"    file.close()\n"
"#    vtk=export.VTKExporter('/home/diego/memoria/Codigos/analisisRM/resultconf05')\n"
"#    vtk.exportSpheres('all',what=[])\n"
"    O.exitNoBacktrace()    \n"
"\n"
"O.engines=[\n"
"ForceResetter(),\n"
"InsertionSortCollider([Bo1_Sphere_Aabb(),Bo1_Box_Aabb()]),\n"
"InteractionLoop(\n"
"[Ig2_Sphere_Sphere_ScGeom(),Ig2_Box_Sphere_ScGeom()],\n"
"[Ip2_FrictMat_FrictMat_FrictPhys()],\n"
"[Law2_ScGeom_FrictPhys_CundallStrack()],\n"
"),\n"
"FlowEngine(dead=1, label='flow'),\n"
"GlobalStiffnessTimeStepper(active=1,timeStepUpdateInterval=100,timestepSafetyCoefficient=0.8),\n"
"PyRunner(command='flujest()', iterPeriod=500, firstIterRun=5000, label='agua'),\n"
"newton,\n"
"PyRunner(command='parar()', iterPeriod=50, firstIterRun=3100, label='muro'),\n"
"PyRunner(command='kant()', iterPeriod=200, firstIterRun=8000, label='kini'),\n"
"PyRunner(command='final()', iterPeriod=200, firstIterRun=8300, label='kfin')\n"
"]\n"
"\n"
"O.run()\n"
"\n"
"############################################################\n"
"#########################################################\n"
"n1=len(spheres)\n"
"Rad=[None]*n1\n"
"Volt=[None]*n1\n"
"V=0\n"
"vol=0\n"
"count=0\n"
"\n"
"for i in range(6, n1+6):\n"
"    Rad[i-6]=O.bodies[i].shape.radius\n"
"    Volt[i-6]=O.bodies[i].shape.radius*O.bodies[i].shape.radius*O.bodies[i].shape.radius\n"
"\n"
"Rad.sort()\n"
"Voltot=sum(Volt)\n"
"\n"
"for i in range(0, n1):\n"
"    V=Rad[i]*Rad[i]*Rad[i]\n"
"    vol=vol+V\n"
"    count=i\n"
"    if vol>=Voltot*.1 : \n"
"        D10=2*Rad[count]\n"
"        print count\n"
"        Count=0\n"
"        vol=0\n"
"        break\n"
"\n"
"for i in range(0, n1):\n"
"    V=Rad[i]*Rad[i]*Rad[i]\n"
"    vol=vol+V\n"
"    count=i\n"
"    if vol>=Voltot*.2 : \n"
"        D20=2*Rad[count]\n"
"        print count\n"
"        Count=0\n"
"        vol=0\n"
"        break\n"
"\n"
"\n"
"for i in range(0, n1):\n"
"    V=Rad[i]*Rad[i]*Rad[i]\n"
"    vol=vol+V\n"
"    count=i\n"
"    if vol>=Voltot*.85 : \n"
"        D85=2*Rad[count]\n"
"        print count\n"
"        Count=0\n"
"        vol=0\n"
"        break\n"
"\n")
    file.close()
    ruta='/home/diego/memoria/YADE/Codigos/Runs/'
    fileName='PsdVarPRF'+RepSd[2:]+'R'+RepRmean[2:]+'.py'
    command_name = 'touch '+ruta+fileName+' && cd '+ruta+' && cat '+archivo+' > '+fileName+' && cat /dev/null > '+archivo+ ' && cd && yade-1.14.0 /home/diego/memoria/YADE/Codigos/Runs/'+fileName   # Change for whatever commnad you need to call
    cmd = command_name + ' "Hello" ' + name + ' from process: ' + str(process) + ' in process: ' + str(os.getpid())

#    print(cmd.split())
    call(cmd, shell = True)


#####################################################################
# Main program 
#####################################################################

# Input parameters to pass to external command. Each tuple represents parameters for one call.
Sd=0.17
conf=2000.
Pi=10.

inputs = [ ('Sotrero', 1, 0.006, Sd, conf, Pi), ('Hamilton', 2, 0.004, Sd, conf, Pi), ('verstapen', 3, 0.003, Sd, conf, Pi), ('shoreza', 4, 0.0025, Sd, conf, Pi ), ('UsainBolt', 5, 0.0015, Sd, conf,Pi), ('Schumacher', 6, 0.0005, Sd, conf, Pi), ('Skt1MPhelps', 7, 0.0003, Sd, conf, Pi)]
#objetos de soteiro. #los parametros son Rmean(int), Sd(doble[0,1]), Conf(double), Pi(double)
# Create parallel pool of workers to run as 4 independent processes. #ahorita son 4 wey
numprocesses = 2
pool = mp.Pool(processes = numprocesses)
pool.map(each_call, inputs) # apply each_call to each tuple in the list inputs


# Note that:
# - Names are printed in random order and not according to order in the list of input parameters.
# - Each call gets its own process id. 
# - If the number of items in the list of inputs is greater than numprocesses, 
#   then the additional commands await in a waiting list to be executed until there is an available process to run it.

