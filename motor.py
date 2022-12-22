import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName

    def SetValue(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 25)