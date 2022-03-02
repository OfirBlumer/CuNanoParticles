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

fig, axs = plt.subplots(3,2)
axs = axs.flatten()
axs[0].hist(getInfo(4,1,cutoff=1.2),bins=100)
axs[0].set_title("C(sp2)-H")
axs[1].hist(getInfo(1,2),bins=100)
axs[1].set_title("C(sp2)-C(sp2)")
axs[2].hist(getInfo(1,3),bins=100)
axs[2].set_title("C(sp3)-C(sp2)")
axs[3].hist(getInfo(47,4,cutoff=1.2),bins=100)
axs[3].set_title("C(sp3)-H")
axs[4].hist(getInfo(14,5),bins=100)
axs[4].set_title("C(sp3)-C(sp3)")
plt.show()

fig, axs = plt.subplots(3,3)
axs = axs.flatten()
axs[0].hist(getInfo(4,1,"angle"),bins=100)
axs[0].set_title("C(sp2)-C(sp2)-H")
axs[1].hist(getInfo(93,2,"angle"),bins=100)
axs[1].set_title("C(sp3)-C(sp3)-H")
axs[2].hist(getInfo(3,3,"angle"),bins=100)
axs[2].set_title("C(sp2)-C(sp3)-H")
axs[3].hist(getInfo(93,4,"angle"),bins=100)
axs[3].set_title("H-C(sp3)-H")
axs[4].hist(getInfo(14,5,"angle"),bins=100)
axs[4].set_title("C(sp3)-C(sp3)-C(sp3)")
axs[5].hist(getInfo(1,6,"angle"),bins=100)
axs[5].set_title("C(sp3)-C(sp2)-H")
axs[6].hist(getInfo(1,7,"angle"),bins=100)
axs[6].set_title("H-C(sp2)-H")
axs[7].hist(getInfo(1,8,"angle"),bins=100)
axs[7].set_title("C(sp2)-C(sp3)-C(sp3)")
axs[8].hist(getInfo(1,9,"angle"),bins=100)
axs[8].set_title("C(sp2)-C(sp2)-C(sp3)")
plt.show()