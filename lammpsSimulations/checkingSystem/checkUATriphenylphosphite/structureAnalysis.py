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
axs[0].hist(getInfo(3,1),bins=100)
axs[0].set_title("O-P")
axs[1].hist(getInfo(6,2),bins=100)
axs[1].set_title("OC-C")
axs[2].hist(getInfo(3,3),bins=100)
axs[2].set_title("C-O")
axs[3].hist(getInfo(12,4),bins=100)
axs[3].set_title("C-C")
plt.show()
fig, axs = plt.subplots(2,2)
axs = axs.flatten()
axs[0].hist(getInfo(3,1,"angle"),bins=100)
axs[0].set_title("C-C(O)-C")
axs[1].hist(getInfo(9,2,"angle"),bins=100)
axs[1].set_title("C-C-C")
axs[2].hist(getInfo(3,3,"angle"),bins=100)
axs[2].set_title("O-P-O")
axs[3].hist(getInfo(9,4,"angle"),bins=100)
axs[3].set_title("OC-C-C")
plt.show()