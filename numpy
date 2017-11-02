numpy.genfromtxt()
numpy.clip()
numpy.fabs()     #绝对值
numpy.pow(a,b)   #a**b


import matplotlib.pyplot as plt
fig, axes = plt.subplots(figsize=(8,6))
axes.plot(x, y, 'r', linewidth=3)
axes.set_xlabel('Time(ps)')
axes.set_ylabel('Amplitude[a.u.]')
fig.savefig("triangular.png", dpi=600)
