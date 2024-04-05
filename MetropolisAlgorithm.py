## MetropolisAlgorithm.py - Husam Adam, Trevor Wallace, Ryan Afzal, Labib Afia
## This file implements the Metropolis algorithm

import LatticeInterface
import numpy as np
import random

def metropolisAlgorithm(lattice: LatticeInterface, kB: float, T: float, nCycles: int, animate: bool) -> tuple[list[float], list[float]]:
  #Initialize the proper arrays
  energies = []
  avgMag = []
  clones = []

  #If you are animating, add the initial lattice to the clones array
  if (animate):
    clones.append(lattice.clone())

  #Get the initial E value of the lattice  
  E = lattice.getE()
  energies.append(E)

  #Run Metropolis for nCycles
  for n in range(nCycles):
    #Choose random lattice site
    i = random.randint(0, lattice.getN() - 1)
    
    # Flip the spin at that site
    lattice.flipSpin(i)

    #Calculate the change in energy ΔE
    E1 = lattice.getE()
    deltaE = E1 - E

    #Decide if you want to accept the flip
    if (deltaE < 0 or (random.random() < np.exp(-deltaE/(kB*T)))):
      E = E1
    else:
      #Swap the spin back  
      lattice.flipSpin(i)

    #Add the current energy and magnetization to the right arrays  
    energies.append(E)
    avgMag.append(lattice.getM())

    #If animating, add a clone of the current lattice
    if (animate):
      clones.append(lattice.clone())

  #Return our arrays
  return energies, avgMag, clones