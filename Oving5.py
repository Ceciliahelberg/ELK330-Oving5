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

