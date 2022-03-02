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
axs[0].hist(getInfo(3,1),bins=100)
axs[0].set_title("O-P")
axs[1].hist(getInfo(6,2),bins=100)
axs[1].set_title("OC-C")
axs[2].hist(getInfo(3,3),bins=100)
axs[2].set_title("C-O")
axs[3].hist(getInfo(27,4,cutoff=1.2),bins=100)
axs[3].set_title("C-H")
axs[4].hist(getInfo(12,5),bins=100)
axs[4].set_title("C-C")
plt.show()
fig, axs = plt.subplots(3,2)
axs = axs.flatten()
axs[0].hist(getInfo(3,1,"angle"),bins=100)
axs[0].set_title("C-C(O)-C")
axs[1].hist(getInfo(9,2,"angle"),bins=100)
axs[1].set_title("C-C-C")
axs[2].hist(getInfo(33,3,"angle"),bins=100)
axs[2].set_title("C-C-H")
axs[3].hist(getInfo(3,4,"angle"),bins=100)
axs[3].set_title("O-P-O")
axs[4].hist(getInfo(8,5,"angle"),bins=100)
axs[4].set_title("OC-C-H")
axs[5].hist(getInfo(9,6,"angle"),bins=100)
axs[5].set_title("OC-C-C")
plt.show()