import matplotlib.pyplot as plt
import numpy as np

# Oppgave 1
# Lager t variabelen
t = np.linspace(0, 24, 1000)
# grunnlasten
L0 = 2
# Amplitude
A = [3, 5]
# tidspunkt for maksbelastning
mu = [7.5, 18.5]
# bredden til toppene
sigma = [2, 4]

L = L0

# Beregner belastningen over tid
for i in range(len(A)):
    L += A[i] * np.exp(-((t - mu[i]) ** 2) / (2 * sigma[i] ** 2))

# plotter belastningen over tid
plt.plot(t, L, color='hotpink')
plt.legend(["Lastprofil"])
plt.title("Lastprofil for en dag")
plt.xlabel("Tid (timer)")
plt.ylabel("Belastning (MW)")
plt.grid(True)
# Lagrer figuren som en PNG-fil
plt.savefig(r"C:\repos\ELK330-Oving5\Oppgave1.png")
plt.show()