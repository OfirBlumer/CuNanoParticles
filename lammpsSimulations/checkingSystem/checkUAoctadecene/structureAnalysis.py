import matplotlib.pyplot as plt

def getInfo(n,id,type="bond",cutoff=1000):
    with open(f'{type}s/{type}{id}.dump') as f:
        lines = f.readlines()
    values = []
    for l in [9+j*(9+n) for j in range(1000)]:
        for k in range(n):
            if float(lines[l+k]) < cutoff:
                values.append(float(lines[l+k]))
    return values

fig, axs = plt.subplots(2,2)
axs = axs.flatten()
axs[0].hist(getInfo(16,1),bins=100)
axs[0].set_title("C(sp3)-C(sp3)")
axs[1].hist(getInfo(1,2),bins=100)
axs[1].set_title("C(sp3)-C(sp2)")
axs[2].hist(getInfo(1,1,"angle"),bins=100)
axs[2].set_title("C(sp3)-C(sp3)-C(sp2)")
axs[3].hist(getInfo(15,2,"angle"),bins=100)
axs[3].set_title("C(sp3)-C(sp3)-C(sp3)")
plt.show()