## WolffAlgorithm.py - Husam Adam, Trevor Wallace, Ryan Afzal, Labib Afia
## This file implements the wolffAlgorithm

import LatticeInterface
import numpy as np
import random

def wolffAlgorithm(lattice: LatticeInterface, J: float, T: float, nCycles: int, animate: bool) -> tuple[list[float], list[float]]:
    #Initialize proper arrays
    energies = []
    avgMag = []
    clones = []

    #Get size of the lattice and E value
    E = lattice.getE()
    N = lattice.getN()

    #Add initial energy of lattice to energies array
    energies.append(E)
    avgMag.append(lattice.getM())

    #If we are animating, then add a clone to the clones array
    if (animate):
        clones.append(lattice.clone())
    
    def activate_links(curr, cluster, activated):
        #Create an array of 4 neighbors
        neighbors = lattice.getNeighbors(curr)

        #Loop through the neighbors
        for neighbor in neighbors:
            # If neighbor is not part of cluster and not activated, run probabilistic analysis
            if not cluster[neighbor] and not activated[neighbor]:
                #Only give probability >= zero if neighbor and current have same spin
                if lattice.getSpin(neighbor) == lattice.getSpin(curr):
                    #Calculate activate probability
                    p_activate = 1 - np.exp(-2 * J / T)
                    if p_activate > random.random():
                        #Add the activated neighbor to the cluster and activate it
                        cluster[neighbor] = 1
                        activated[neighbor] = 1

                        #Run activate_links again recursively on the activated neighbor
                        activate_links(neighbor, cluster, activated)

    #Loop nCycles times
    for _ in range(nCycles):
        #Choose a random initial point
        curr = random.randint(0, N-1)

        #Create arrays of N zeros
        cluster = [0 for _ in range(N)]
        activated = [0 for _ in range(N)]

        #Add the current point to the cluster and run activate_links() on the current point
        cluster[curr - 1] = 1
        activate_links(curr, cluster, activated)

        #Loop through the entire lattice and flip the spins of every point in the cluster
        for i in range(N):
            if cluster[i]:
                lattice.flipSpin(i)

        #Get the energy of the entire lattice and append to the energies array
        E = lattice.getE()
        energies.append(E)
        avgMag.append(lattice.getM())

        #If we are animating, then add a clone to the clones array
        if (animate):
            clones.append(lattice.clone())
    
    #Return our arrays
    return energies, avgMag, clones
