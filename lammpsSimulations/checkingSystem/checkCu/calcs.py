from unum.units import *
import pandas
import matplotlib.pyplot as plt

for T in [300,600,900]:
    dataEam = pandas.read_csv(f"eam/Deg2Theta{T}.xrd", delimiter=r"\s+",
                             skiprows=2514,names=["i","2Theta","intensity","c"])
    dataLJ = pandas.read_csv(f"lennardJones/Deg2Theta{T}.xrd", delimiter=r"\s+",
                             skiprows=2514,names=["i","2Theta","intensity","c"])
    plt.plot(dataEam["2Theta"], dataEam["intensity"],dataLJ["2Theta"], dataLJ["intensity"])
    plt.show()

    hartreeLength = 0.529 # hartree units of length in angstrom
    dataEam = pandas.read_csv(f"eam/rdf_{T}.out", delimiter=r"\s+",
                             skiprows=1014,names=["i","bin","g(r)","coord(r)"])
    dataLJ = pandas.read_csv(f"lennardJones/rdf_{T}.out", delimiter=r"\s+",
                             skiprows=1014,names=["i","bin","g(r)","coord(r)"])
    plt.plot(dataEam["bin"]/hartreeLength, dataEam["g(r)"],dataLJ["bin"]/hartreeLength, dataLJ["g(r)"])
    plt.show()




# natoms = 32000
# Na = 6.02*10**23
# Nmols = natoms/Na*mol
# unitsConvEAM = ((1 * eV / Nmols / 1000).asUnit(J / mol)).asNumber()
# unitsConvLJ = 4.184/natoms
# dataEAM = pandas.read_csv("eam/heatingData", delimiter=r"\s+")
# dataEAM["E_kJ"] = unitsConvEAM * dataEAM.TotEng
# dataLJ = pandas.read_csv("lennardJones/heatingData", delimiter=r"\s+")
# dataLJ["E_kJ"] = unitsConvLJ * dataLJ.TotEng
# plt.plot(dataEAM.Temp, dataEAM.E_kJ,dataLJ.Temp, dataLJ.E_kJ)
# plt.show()