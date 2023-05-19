import matplotlib.pyplot as plt
import pandas as pd

pontos = pd.read_csv('tensaoxcorrente-lampada.csv')

"""plt.scatter(pontos.amperagem,pontos.voltagem)
plt.xlabel('Amperagem (mA)')
plt.ylabel('Voltagem (V)')

plt.savefig('LabFisica-3/Relatorio2/grafico-lampada-pontos.png')

plt.close()

pontos.plot()"""

x = list(pontos.amperagem)
y = list(pontos.voltagem)

for i in range(len(x)):
    print(f"${y[i]}$ & ${x[i]}$ \\ \hline")