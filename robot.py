import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR

class ROBOT:

    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, i):
        for sensor in self.sensors.values():
            sensor.GetValue(i)
    
    def Prepare_To_Act(self):
       self.motors = {}
       for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, i):
        for motor in self.motors.values():
            motor.SetValue(self.robotId, i)
    
    def SaveValues(self):
        for motor in self.motors.values():
            motor.SaveValues()
        for sensor in self.sensors.values():
            sensor.SaveValues() 