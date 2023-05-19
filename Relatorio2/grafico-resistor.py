import matplotlib.pyplot as plt
import pandas as pd
from regressao import minimos_quadrados

pontos = pd.read_csv('tensaoxcorrente-resistor.csv')

"""plt.scatter(pontos.amperagem,pontos.voltagem)
plt.xlabel('Amperagem (mA)')
plt.ylabel('Voltagem (V)')

plt.savefig('grafico-resistor-pontos.png')

plt.close()

minimos_quadrados(list(pontos.amperagem),list(pontos.voltagem))"""

x = list(pontos.amperagem)
y = list(pontos.voltagem)

for i in range(len(x)):
    print(f"${y[i]}$ & ${x[i]}$ \\ \hline")
