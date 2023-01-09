import numpy as np

bl_amplitude = np.pi/2
bl_frequency = 10
bl_phaseOffset = 0
bl_targetAngles = bl_amplitude * np.sin(bl_frequency * np.linspace(0, 2*np.pi, 1000) + bl_phaseOffset)
fl_amplitude = np.pi/2
fl_frequency = 10
fl_phaseOffset = 0
fl_targetAngles = fl_amplitude * np.sin(fl_frequency * np.linspace(0, 2*np.pi, 1000) + fl_phaseOffset)
numberOfGenerations = 25