import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) # find data that comes with pybullet
p.setGravity(0,0,-9.8) # add gravitational force
planeId = p.loadURDF("plane.urdf") # add floor plane
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = (random.random()-0.5)*math.pi,
        maxForce = 25)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = (random.random()-0.5)*math.pi,
        maxForce = 25)
    time.sleep(1/60)
    print("forloop iteration: " + str(i)) 
np.save('data/backLegSensorValues', backLegSensorValues)
np.save('data/frontLegSensorValues', frontLegSensorValues)
p.disconnect()