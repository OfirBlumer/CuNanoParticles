import pandas
import matplotlib.pyplot as plt
data= pandas.read_csv("wellTempered/colv", delimiter=r"\s+",skiprows=1,names=["time","mean","morethan",1,2,3],index_col=False)

plt.plot(data.time,data["morethan"])

plt.show()
