import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:

    def __init__(self, myID) -> None:
        self.numSegs = random.randint(5,10)
        self.weights = np.random.rand(self.numSegs+1,self.numSegs)*2 - 1
        self.myID = myID
        self.cubes = []
        self.joints = []
        self.sensor_neurons = []
        self.motor_neurons = []
        self.size = 0

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName, "r")
        fitness = f.read()
        self.fitness = float(fitness)
        f.close()
        os.system("rm " + fitnessFileName)

    def Create_World(self):
        # tell pyrosim the name of the file where information about the world you're about to create should be stored
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[2,1,0.5] , size=[1, 1, 1])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        self.cubes = []
        self.joints = []
        prev_cube_size = [1,1,1]
        pyrosim.Send_Cube(name="Head", pos=[0, 0, 0.5] , size=[1, 1, 1])
        self.cubes.append("Head")
        for i in range(self.numSegs):
            cur_cube = "Seg-" + str(i)
            prev_cube = self.cubes[-1]
            size_x = random.random()
            size_y = random.random()
            size_z = random.random()
            joint_axes = [0,0,0]
            if i == 0:
                pos = [0.5, 0.5, 0]
                joint_axes = [1,0,0]
            else:
                pos = [prev_cube_size[0]/2*random.randint(0,1), prev_cube_size[1]/2*random.randint(0,1), prev_cube_size[2]*random.randint(0,1)]
                joint_axes[random.randint(0,2)] = 1
            pyrosim.Send_Joint(name = prev_cube + "_" + cur_cube , 
                parent= prev_cube , child = cur_cube , type = "revolute", 
                position = pos, jointAxis = " ".join(str(j) for j in joint_axes))
            self.joints.append(prev_cube + "_" + cur_cube)
            pyrosim.Send_Cube(name=cur_cube, pos=[size_x/2, size_y/2, size_z/2], size=[size_x, size_y, size_z])
            self.cubes.append(cur_cube)
            prev_cube_size = (size_x, size_y, size_z)

        # for i in range(c.numSegs):
        #     cur_cube = "Seg-" + str(i)
        #     prev_cube = self.cubes[-1]
        #     # first joint is absolute
        #     if i == 0:
        #         joint_pos = [0,0.5,0]
        #         cube_pos = [0,(c.numSegs - i)*0.1/2, (c.numSegs - i)*0.1/2]
        #     else:
        #         joint_pos = [0, (c.numSegs - i + 1)*0.1 , 0]
        #         cube_pos = [0,(c.numSegs - i)*0.1/2,(c.numSegs - i)*0.1/2]
        #     pyrosim.Send_Joint(name = prev_cube + "_" + cur_cube , 
        #         parent= prev_cube , child = cur_cube , type = "revolute", position = joint_pos, jointAxis = "0 1 0")
        #     self.joints.append(prev_cube + "_" + cur_cube)
        #     pyrosim.Send_Cube(name=cur_cube, pos=cube_pos, size=[(c.numSegs - i)*0.1, (c.numSegs - i)*0.1, (c.numSegs - i)*0.1])
        #     self.cubes.append(cur_cube)

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        for i in range(len(self.cubes)):
             if random.random() > 0.5 or i == 0:
                pyrosim.Send_Sensor_Neuron(name = i , linkName = self.cubes[i])
                self.sensor_neurons.append(i)
        for i in range(len(self.joints)):
            pyrosim.Send_Motor_Neuron( name = i+len(self.cubes) , jointName = self.joints[i])
            self.motor_neurons.append(i)
        for currentRow in self.sensor_neurons:
            for currentColumn in self.motor_neurons:
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+len(self.cubes) , weight = self.weights[currentRow][currentColumn])
        pyrosim.End()
   
    def Mutate(self):
        randRow = random.randint(0, len(self.cubes)-1)
        randCol = random.randint(0, len(self.joints)-1)
        self.weights[randRow][randCol] = random.random() * 2 + 1

    def Set_ID(self, myID):
        self.myID = myID


