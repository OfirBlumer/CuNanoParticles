import pandas
import matplotlib.pyplot as plt
import plumed as plm
import numpy as np
from unum.units import *

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
for temp in ["1220_2"]:
    data= pandas.read_csv(f"COLVAR{temp}", delimiter=r"\s+",skiprows=1,names=["time","mean","morethan",1,2],index_col=False)
    plt.plot(data.time,data["morethan"])
    plt.show()
    data = pandas.read_csv(f"fes_{temp}.dat", delimiter=r"\s+", skiprows=6, names=["morethan", "freeEnergy", "der"]).astype(float)
    plt.plot(data["morethan"],data["freeEnergy"])
    plt.show()
    data = pandas.read_csv(f"ff{temp}.dat", delimiter=r"\s+", skiprows=6, names=["morethan", "freeEnergy", "der"]).astype(float)
    plt.plot(data["morethan"],data["freeEnergy"])
    plt.show()
    data = pandas.read_csv(f"hh{temp}.dat", delimiter=r"\s+", skiprows=6, names=["morethan", "density", "der"]).astype(float)
    plt.plot(data["morethan"],data["density"])
    # pliquid = np.trapz(data.loc[data.morethan<128].density)
    # psolid = np.trapz(data.loc[data.morethan>128].density)
    # dg = -temp*1.380649e-23*J*np.log(psolid/pliquid)
    # print(dg,np.log(psolid/pliquid))
    plt.show()

# for temp in [1260,1310,1360,1410,1460]:
#     data= pandas.read_csv(f"COLVAR{temp}_2", delimiter=r"\s+",skiprows=1,names=["time","mean","morethan",1,2],index_col=False)
#
#     plt.plot(data.time,data["morethan"])
#     plt.show()
#     data = pandas.read_csv(f"fes_{temp}_2.dat", delimiter=r"\s+", skiprows=6, names=["morethan", "freeEnergy", "der"]).astype(float)
#     plt.plot(data["morethan"],data["freeEnergy"])
#     plt.show()
#     data = pandas.read_csv(f"ff{temp}.dat", delimiter=r"\s+", skiprows=6, names=["morethan", "freeEnergy", "der"]).astype(float)
#     plt.plot(data["morethan"],data["freeEnergy"])
#     plt.show()


# import plumed as plm
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# for temp in [1260,1360]:
#     kt=2.48*temp/300 #@300 K
#     r2 = plm.read_as_pandas(f"COLVAR{temp}_2")
#
#     histc, histb = np.histogram(r2["es.morethan"],bins=100,range=(0,256),weights=np.exp(r2["metad.rbias"]/kt))
#
#     s = 0.5*(histb[1:]+histb[:-1])
#     F = -kt*np.log(histc/max(histc))
#
#     plt.plot(s,F)
#
#     plt.xlabel("CV")
#     plt.ylabel("Free Energy [kJ/mol]")
#     plt.show()

# data= pandas.read_csv("1320/liquid/analysis.9.histo", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
# plt.plot(data["mean"],data["hh"])
# data= pandas.read_csv("1320/solid/analysis.9.histo", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
# plt.plot(data["mean"],data["hh"])
# plt.ylim(0,5)
# plt.xlim(0,1)
# plt.show()

# data= pandas.read_csv("1320/liquid/analysis.0.histoQ6", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
# plt.plot(data["mean"],data["hh"])
# data= pandas.read_csv("1320/solid/analysis.0.histoQ6", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
# plt.plot(data["mean"],data["hh"])
# data= pandas.read_csv("1320/liquid/analysis.9.histo", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
# plt.plot(data["mean"],data["hh"],linestyle="dashed")
# data= pandas.read_csv("1320/solid/analysis.9.histo", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
# plt.plot(data["mean"],data["hh"],linestyle="dashed")
# data= pandas.read_csv("1320/liquid/analysis.2.histoQ6", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
# plt.plot(data["mean"],data["hh"],linestyle="dotted")
# data= pandas.read_csv("1320/solid/analysis.2.histoQ6", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
# plt.plot(data["mean"],data["hh"],linestyle="dotted")
# plt.ylim(0,5)
# plt.xlim(0,1)
plt.show()
