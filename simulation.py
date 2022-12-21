from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time

class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath()) # find data that comes with pybullet
        p.setGravity(0,0,-9.8) # add gravitational force

        self.world = WORLD()
        self.robot = ROBOT()
    
    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            time.sleep(1/40)
        # self.robot.SaveValues()
    def __del__(self):
        p.disconnect()


        
