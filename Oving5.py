import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

# Oppgave 2
# Leser inn CSV-filen
df = pd.read_csv("ProductionConsumption-2026.csv")

# Endrer datatype til datetime og setter "Time(Local)" som indeks
# Fjerner UTC offset fra "Time(Local)" kolonnen slik at det kan konverteres til datetime
df["Time(Local)"] = df["Time(Local)"].str[:-7]
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"], format="%d.%m.%Y %H:%M:%S")
df = df.set_index("Time(Local)")

# Velger ut data for en spesifikk dag
day = df.loc["2026-04-14"]

# Kun last dataene for dagen
lastprofil = day["Consumption"]

#plotter døgnets lastprofil
plt.plot(lastprofil, color='hotpink')
plt.legend(["Last"])
plt.title("Lastprofil")
plt.xlabel("Tid")
plt.ylabel("Forbruk (MW)")
plt.grid(True)
plt.savefig(r"C:\repos\ELK330-Oving5\Oppgave2.png")
plt.show()


# Oppgave 3
# undersøker døgnprofilen

min_last = lastprofil.min()
max_last = lastprofil.max()
tid_max = lastprofil.idxmax()
print(min_last)
print(max_last)
print(tid_max)

# tidsvariabelen for gauss-modellen slik at kurven blir glatt
t = np.linspace(0, 24, 1000)
# tidsvariabelen for lastprofilen 
t_data = np.arange(len(lastprofil))

# Setter L0 til minimumsverdien av lastprofilen
L0 = min_last

# første topp er satt til max verdien til lasten - L0 (morgentopp)
# andre topp er satt til 2300 MW (kveldstopp)
A = [2800, 2200, 1700, 500]

# tidspunkt for første topp er satt til tidspunktet for maksbelastning
# tidspunkt for andre topp er satt til 18.5 (kveldstopp)
mu = [8.5, 16, 21, 0]

# bredden til toppene er satt til 2 timer for første topp 
# 3 timer for andre topp
sigma = [1.5, 3, 2, 2]

# velger min verdi av L til L0
L = L0
# Beregner belastningen over tid
for i in range(len(A)):
    L += A[i] * np.exp(-((t - mu[i]) ** 2) / (2 * sigma[i] ** 2))

# plotter gauss modellen
plt.plot(t, L, color='hotpink')
plt.legend(["Last", "Gauss modell"])
plt.title("Lastprofil")
plt.xlabel("Tid")
plt.ylabel("Forbruk (MW)")
plt.grid(True)
plt.savefig(r"C:\repos\ELK330-Oving5\GaussModell.png")
plt.show()

# plotter begge sammen for å sammenligne
plt.plot(t_data, lastprofil, color='orangered')
plt.plot(t, L, color='hotpink')
plt.legend(["Last", "Gauss modell"])
plt.title("Lastprofil")
plt.xlabel("Tid")
plt.ylabel("Forbruk (MW)")
plt.grid(True)
plt.savefig(r"C:\repos\ELK330-Oving5\Sammenligning.png")
plt.show()


