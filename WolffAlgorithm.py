## This code was written using ChatGPT by feeding a detailed pseudocode outline and the beginning of an implementation scheme.
## This is testable once main() is completed and should work properly.
## I cleaned up the ChatGPT code and this SOMETIMES works.
# TODO: Fix the wraparound. Indices get out of bounds sometimes.

# Basic pseudocode outline:
# 1. Choose a random single site to build a cluster
# 2. Consider links to initial site:
#       p_l_min = 0
#       p_l_plus = 1 - exp(-2*beta*sigma_min*sigma_plus)
# 3. Given set of sites added to cluster in previous update, consider links to sites outside cluster:
#       Activate l_plus links with probabilty p_l_plus
# 4. Loop back to Step 3 until set of links left for activation in next round is empty.
# 5. Flip whole cluster with probability 1. Loop back to step 1.

# from random import randint, exp
import LatticeInterface
import numpy as np
import random

def wolffAlgorithm(lattice: LatticeInterface, beta: float, T: float, nCycles: int) -> tuple[list[float], list[float]]:
    energies = [] # Initialize energies array
    avgMag = []
    clones = []
    clones.append(lattice.clone())
    E = lattice.getE()
    energies.append(E) # Add initial energy of lattice to energies array
    avgMag.append(lattice.getM())
    N = lattice.getN() # Get size of lattice - or should this be sqrt(N) ?

    def activate_links(curr, cluster, activated):
        neighbors = lattice.getNeighbors(curr) # Create an array of 4 neighbors

        for neighbor in neighbors: # Loop through the 4 neighbors
            # If neighbor is not part of cluster and not activated, run probabilistic analysis
            if not cluster[neighbor] and not activated[neighbor]: ### MAY BE WRONG - wraparound
                # n_idx = lattice[neighbor]
                if lattice.getSpin(neighbor) == lattice.getSpin(curr): # Only give probability >= zero if neighbor and current have same spin
                    p_activate = 1 - np.exp(-2 * beta) # I don't think this is correct ? Should incorporate spins I think. Maybe not because they already are.
                    if p_activate > random.random():
                        cluster[neighbor] = 1 # Add the activated neighbor to the cluster...
                        activated[neighbor] = 1 # and activate it.
                        activate_links(neighbor, cluster, activated) # Run activate_links again recursively on the activated neighbor

    for _ in range(nCycles): # Loop nCycles times
        curr = random.randint(0, N-1) # Chooses a random initial point

        cluster = [0 for _ in range(N)] # Creates an array of N zeros
        activated = [0 for _ in range(N)] # Creates an array of N zeros

        cluster[curr - 1] = 1 # Adds the current point to the cluster ## IS -1 CORRECT???
        activate_links(curr, cluster, activated) # Runs activate_links() on the current point

        for i in range(N): # Loop through the entire lattice and flip the spins of every point in the cluster
            if cluster[i]:
                lattice.flipSpin(i)

        E = lattice.getE() # Get the energy of the entire lattice and append to the energies array
        energies.append(E)
        avgMag.append(lattice.getM())
        clones.append(lattice.clone())


    return energies, avgMag, clones
