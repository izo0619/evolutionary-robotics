from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time

class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath()) # find data that comes with pybullet
        p.setGravity(0,0,-9.8) # add gravitational force

        self.world = WORLD()
        self.robot = ROBOT(solutionID)
    
    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                time.sleep(1/200)
        # self.robot.SaveValues()
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()


        
