class LatticeInterface:
  """Stores spin lattice data"""

  def getN(self) -> int:
    """Returns the number of lattice points"""
    pass

  def getJ(self) -> float:
    """Returns the parameter J"""
    pass

  def getSpin(self, i: int) -> int:
    """Returns the spin state [-1, 1] of the specified lattice point"""
    pass

  def setSpin(self, i: int, spin: int):
    """Sets the spin state [-1, 1] of the specified lattice point"""
    pass

  def getNeighbors(self, i: int) -> list[int]:
    """Returns a list of indices of the neighbors of the specified lattice point"""
    pass

#   def clone(self) -> LatticeInterface:
#     """Returns a copy of this LatticeInterface"""
#     pass

  def flipSpin(self, i: int):
    """Flips the spin state [-1, 1] of the specified lattice point"""
    if (self.getSpin(i) == 1):
      self.setSpin(i, -1)
    else:
      self.setSpin(i, 1)

  def getE(self) -> float:
    """Returns the value of the Hamiltonian H"""
    sum = 0
    for i in range(self.getN()):
      for j in self.getNeighbors(i):
        sum += self.getSpin(i) * self.getSpin(j)
    return sum * (-self.getJ())

  def getM(self) -> float:
    """Returns the value of the average magnetization M"""
    sum = 0
    for i in range(self.getN()):
      sum += self.getSpin(i)
    return sum / self.getN()