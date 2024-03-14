import algorithms
import matplotlib.pyplot as plt
import MatrixLattice as matrix

param_N = 10
param_T = 273.15
param_kB = 1#1.380649E-23
param_J = 1
param_ncycles = 50

#
# Create the lattice using the parameters
#
globalLattice = matrix.MatrixLattice(param_J, param_N)

#
# Run the algorithms on the lattice
#

#energies_m, mag_m = algorithms.runMetropolis(globalLattice, plt, param_ncycles, param_T, param_kB)
energies_w, mag_w = algorithms.runWolff(globalLattice, plt, param_ncycles, param_T, param_J)