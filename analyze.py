import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
plt.plot(backLegSensorValues, lineWidth=2)
plt.plot(frontLegSensorValues)
plt.legend(["backLeg", "frontLeg"])
plt.show()