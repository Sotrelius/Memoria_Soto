############################
# Author: Paulo Herrera
# Date: 20/May/2015
# primera modificacion de soteiro, correr varios script con las mismas caracteristicas, el siguiente paso, meter scripts aca y cambiarle parametros directamente desde la tabla.
####################################################

from subprocess import call
import multiprocessing as mp
import os

def each_call(input_params):
    ''' Call for each command to execute '''
    name, process = input_params
    command_name = ' echo $PWD && yade-1.14.0 /home/diego/memoria/YADE/Codigos/PsdVarPRF00.py '   # Change for whatever commnad you need to call
    cmd = command_name + ' "Hello" ' + name + ' from process: ' + str(process) + ' in process: ' + str(os.getpid())

    #print(cmd.split())
    call(cmd, shell = True)


#####################################################################
# Main program 
#####################################################################

# Input parameters to pass to external command. Each tuple represents parameters for one call.
inputs = [ ('Sotrero', 1), ('Hamilton', 2), ('verstapen', 3), ('shoreza', 4), ('kalvinklein', 5)]

# Create parallel pool of workers to run as 4 independent processes.
numprocesses = 2
pool = mp.Pool(processes = numprocesses)
pool.map(each_call, inputs) # apply each_call to each tuple in the list inputs


# Note that:
# - Names are printed in random order and not according to order in the list of input parameters.
# - Each call gets its own process id. 
# - If the number of items in the list of inputs is greater than numprocesses, 
#   then the additional commands await in a waiting list to be executed until there is an available process to run it.

