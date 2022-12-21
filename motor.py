import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        if self.jointName == b'Torso_BackLeg':
            print("in torso backleg")
            self.frequency = 5
        else:
            print("not in torso backleg")
            self.frequency = 10
        self.amplitude = np.pi/4
        self.phaseOffset = 0
        self.values = self.amplitude * np.sin(self.frequency * np.linspace(0, 2*np.pi, 1000) + self.phaseOffset)

    def SetValue(self, robotId, i):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.values[i],
            maxForce = 25)
    
    def SaveValues(self):
        np.save('data/' + str(self.jointName), self.values)