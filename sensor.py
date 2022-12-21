import numpy as np
import pyrosim.pyrosim as pyrosim
class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(1000)

    def GetValue(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # if i == (len(self.values) - 1):
        #     print(self.values)
    
    def SaveValues(self):
        np.save('data/' + str(self.linkName), self.values)