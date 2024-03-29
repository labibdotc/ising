import LatticeInterface as li
import MetropolisAlgorithm as m_a
import WolffAlgorithm as w_a
from matplotlib import animation, rc
from IPython.display import HTML
import numpy as np

def testAlgorithm(name, lattice: li.LatticeInterface, algorithm, plot) -> tuple[list[float],list[float],list[li.LatticeInterface]]:
  energies, avgMag, clones = algorithm(lattice)

  energiesPlot = plot
  magPlot = plot

  energiesPlot.plot(energies)
  energiesPlot.xlabel('Step')
  energiesPlot.ylabel('Energy (J)')
  energiesPlot.title(f'{name} Energy vs Step')
  energiesPlot.show()

  magPlot.plot(avgMag)
  magPlot.xlabel('Step')
  magPlot.ylabel('Average Magnetization')# A/m?
  magPlot.title(f'{name} Average Magnetization vs Step')
  magPlot.show()

  return energies, avgMag, clones

def runMetropolis(lattice: li.LatticeInterface, plot, N, T, kB) -> tuple[list[float],list[float],list[li.LatticeInterface]]:
  name = f'Metropolis (T={T}K)'
  return testAlgorithm(name, lattice.clone(), lambda x: m_a.metropolisAlgorithm(x, kB, T, N), plot)

def runWolff(lattice: li.LatticeInterface, plot, N, T, J) -> tuple[list[float],list[float]]:
  name = f'Wolff (T={T}K)'
  return testAlgorithm(name, lattice.clone(), lambda x: w_a.wolffAlgorithm(x, J, T, N), plot)

def animate(clones):
    fig, ax = plt.subplots()
    i = 0

    def update(frame):
        ax.clear()
        ax.imshow(clones[i], cmap='binary', interpolation='nearest')
        ax.set_title(f"Step {frame}")
        i += 1
        return ax

    ani = animation.FuncAnimation(fig, update, frames=nCycles, interval=200, repeat=False)
    """Display using HTML"""
    HTML(ani.to_jshtml())
    return ani