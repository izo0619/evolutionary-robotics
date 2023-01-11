import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:

    def __init__(self, myID) -> None:
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)*2 - 1
        self.myID = myID

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
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1] , size=[1, 1, 1])
        
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])


        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        sensor_neurons = ["Torso", "BackLeg", "FrontLeg", "LeftLeg", "RightLeg",  "BackLowerLeg", "FrontLowerLeg", "LeftLowerLeg", "RightLowerLeg"]
        joint_neurons = ["Torso_BackLeg", "Torso_FrontLeg", "Torso_LeftLeg", "Torso_RightLeg", "BackLeg_BackLowerLeg", "FrontLeg_FrontLowerLeg", "LeftLeg_LeftLowerLeg", "RightLeg_RightLowerLeg"]
        for i in range(len(sensor_neurons)):
             pyrosim.Send_Sensor_Neuron(name = i , linkName = sensor_neurons[i])
        for i in range(len(joint_neurons)):
            pyrosim.Send_Motor_Neuron( name = i+len(sensor_neurons) , jointName = joint_neurons[i])
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()
   
    def Mutate(self):
        randRow = random.randint(0, c.numSensorNeurons-1)
        randCol = random.randint(0, c.numMotorNeurons-1)
        self.weights[randRow][randCol] = random.random() * 2 + 1

    def Set_ID(self, myID):
        self.myID = myID


