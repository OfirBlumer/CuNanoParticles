import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv(f"wellTempered/fes_1.dat", delimiter=r"\s+", skiprows=6, names=["morethan", "freeEnergy", "der"]).astype(float)
plt.plot(data["morethan"],data["freeEnergy"])
plt.show()

