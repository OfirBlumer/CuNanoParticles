import pandas
import matplotlib.pyplot as plt
#

# plt.show()
#
for temp in [1000,1200,1400]:
    # data= pandas.read_csv(f"COLVAR{temp}", delimiter=r"\s+",skiprows=1,names=["time","mean","morethan",1,2],index_col=False)
    #
    # plt.plot(data.time,data["morethan"])
    data = pandas.read_csv(f"fes_{temp}.dat", delimiter=r"\s+", skiprows=6, names=["morethan", "freeEnergy", "der"]).astype(float)
    plt.plot(data["morethan"],data["freeEnergy"])

    plt.show()
# data= pandas.read_csv("1000/liquid/analysis.9.histo", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
# plt.plot(data["mean"],data["hh"])
# data= pandas.read_csv("1000/solid/analysis.9.histo", delimiter=r"\s+",skiprows=6,names=["mean","hh", "dhh_es"],index_col=False)
# plt.plot(data["mean"],data["hh"])
# plt.show()