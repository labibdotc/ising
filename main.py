## main.py - Husam Adam, Trevor Wallace, Ryan Afzal, Labib Afia
## This file is meant to simulate the Ising model using the Metropolis and Wolff algorithms.

import algorithms
import matplotlib.pyplot as plt
import MatrixLattice as matrix
import numpy as np

#Set parameters
param_N = 15
param_T = 0.00000001
param_kB = 1
param_J = 1
param_ncycles = 100

#Decide on if you want clones and plots
algorithms.clonesOn = True
algorithms.plotsOn = False

#Create the lattice using the parameters
globalLattice = matrix.MatrixLattice(param_J, param_N)

#Initialize arrays for plotting Metropolis
magnetizationArr = []
energiesArr = []
tempArr = []

#Initialize arrays for plotting Wolff
magnetizationArr2 = []
energiesArr2 = []
tempArr2 = []

#Run the algorithms on the lattice
energies_m, mag_m, clones_m = algorithms.runMetropolis(globalLattice, plt, param_ncycles, param_T, param_kB)
energies_w, mag_w, clones_w = algorithms.runWolff(globalLattice, plt, param_ncycles, param_T, param_J)

## Animation ##
#run the animate functions and save them as an mp4 file
ani_w = algorithms.animate(clones_w, plt)
ani_w.save('animation_w.mp4', writer='ffmpeg')
ani_m = algorithms.animate(clones_m, plt)
ani_m.save('animation_m.mp4', writer='ffmpeg')

## Metropolis ##
for n in range(250):
  #run metropolis
  energies_m, mag_m, clones_m = algorithms.runMetropolis(globalLattice, plt, param_ncycles, param_T, param_kB)

  #Process magnetization data
  mag_m = np.absolute(mag_m[100:])
  energies_w = np.absolute(energies_m[100:])

  #To print the magnetization data - uncomment the two lines below this
  # print(np.std(mag_m))
  # print(np.std(energies_m))

  #Store the results in our arrays
  magnetizationArr.append(np.std(mag_m))
  energiesArr.append(np.std(energies_m))
  tempArr.append(param_T)

  #Increase the temperature
  param_T = param_T + 0.04

#Plot our graphs for Metropolis
plt.plot(tempArr, magnetizationArr)
plt.xlabel('Temperature (Nondimensionalized)')
plt.xlim(0,10)
plt.ylabel('Average Std Dev Abs Val Magnetization (Stable Zone)')
plt.suptitle('Std Dev Magnetization vs. Temperature', fontsize=14)
plt.title('Metropolis Algorithm | 250 Temperatures, 500 Cycles', fontsize=12)
plt.show()

plt.plot(tempArr, energiesArr)
plt.xlabel('Temperature (Nondimensionalized)')
plt.xlim(0,10)
plt.ylabel('Average Std Dev Abs Val Energy (Stable Zone)')
plt.suptitle('Std Dev Energy vs. Temperature', fontsize=14)
plt.title('Metropolis Algorithm | 250 Temperatures, 500 Cycles', fontsize=12)
plt.show()

## Wolff ##
for n in range(5):
  #Run wolff
  energies_w, mag_w, clones_w = algorithms.runWolff(globalLattice, plt, param_ncycles, param_T, param_J)

  #Process magnetization data
  mag_w = np.absolute(mag_w[2500:])
  energies_w = np.absolute(energies_w[2500:])

  #To print the magnetization data - uncomment the two lines below this
  # print(np.std(mag_w))
  # print(np.std(energies_w))

  #Store the results in our arrays
  magnetizationArr2.append(np.std(mag_w))
  energiesArr2.append(np.std(energies_w))
  tempArr2.append(param_T)

  #Increase the temperature
  param_T = param_T + 0.01

#Plot our graphs for Wolff
plt.plot(tempArr2, magnetizationArr2)
plt.xlabel('Temperature (Nondimensionalized)')
plt.ylabel('Average Std Dev Abs Val Magnetization (Stable Zone)')
plt.suptitle('Std Dev Magnetization vs. Temperature', fontsize=14)
plt.title('Wolff Algorithm | 500 Temperatures, 5000 Cycles', fontsize=12)
plt.show()

plt.plot(tempArr2, energiesArr2)
plt.xlabel('Temperature (Nondimensionalized)')
plt.ylabel('Average Std Dev Abs Val Energy (Stable Zone)')
plt.suptitle('Std Dev Energy vs. Temperature', fontsize=14)
plt.title('Wolff Algorithm | 500 Temperatures, 5000 Cycles', fontsize=12)
plt.show()