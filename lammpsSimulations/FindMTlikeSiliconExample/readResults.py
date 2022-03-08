import pandas
import matplotlib.pyplot as plt
import plumed as plm
import numpy as np

import matplotlib as mpl

# r2 = plm.read_as_pandas("COLVAR1260")
#
# histc, histb = np.histogram(r2["es.morethan"],bins=100,range=(0,100),weights=np.exp(r2["metad.rbias"]/2.48))
#
# s = 0.5*(histb[1:]+histb[:-1])
# F = -2.48*np.log(histc/max(histc))
#
# plt.plot(s,F)
#
# plt.xlabel("CV")
# plt.ylabel("Free Energy [kJ/mol]")
# plt.show()

# plt.show()
#
for temp in [1260,1310,1360,1410,1460]:
    data= pandas.read_csv(f"COLVAR{temp}", delimiter=r"\s+",skiprows=1,names=["time","mean","morethan",1,2],index_col=False)

    plt.plot(data.time,data["morethan"])
    plt.show()
    data = pandas.read_csv(f"fes_{temp}.dat", delimiter=r"\s+", skiprows=6, names=["morethan", "freeEnergy", "der"]).astype(float)
    plt.plot(data["morethan"],data["freeEnergy"])

    plt.show()
data= pandas.read_csv("1000/liquid/analysis.9.histo", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
plt.plot(data["mean"],data["hh"])
data= pandas.read_csv("1000/solid/analysis.9.histo", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
plt.plot(data["mean"],data["hh"])
plt.show()