from unum.units import *
ml = 0.001*L

CuMols = 0.5e-3*mol
solventVolume = 8*ml
additiveVolume = 1.6*ml
solventMm = 252.486*g/mol
solventDensity = 789*kg/m**3
additiveMm = 320*g/mol
additiveDensity = 1184*kg/m**3

solventMols = solventVolume*solventDensity/solventMm
additiveMols = additiveVolume*additiveDensity/additiveMm
print(solventMols,additiveMols,(solventMols+additiveMols)/CuMols)