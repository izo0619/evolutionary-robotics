import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
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

bl_amplitude = np.pi/4
bl_frequency = 10
bl_phaseOffset = 0
bl_targetAngles = bl_amplitude * np.sin(bl_frequency * np.linspace(0, 2*np.pi, 1000) + bl_phaseOffset)
# np.save('data/bl_targetAngles', bl_targetAngles)
fl_amplitude = np.pi/4
fl_frequency = 10
fl_phaseOffset = 0
fl_targetAngles = fl_amplitude * np.sin(fl_frequency * np.linspace(0, 2*np.pi, 1000) + fl_phaseOffset)
# np.save('data/fl_targetAngles', fl_targetAngles)
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = bl_targetAngles[i],
        maxForce = 25)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = fl_targetAngles[i],
        maxForce = 25)
    time.sleep(1/60)
    print("forloop iteration: " + str(i)) 
np.save('data/backLegSensorValues', backLegSensorValues)
np.save('data/frontLegSensorValues', frontLegSensorValues)
p.disconnect()