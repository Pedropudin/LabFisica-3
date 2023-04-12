import matplotlib.pyplot as plt
import pandas as pd

pontos = pd.read_csv('LabFisica-3/Relatorio2/tensaoxcorrente-lampada.csv')

plt.scatter(pontos.amperagem,pontos.voltagem)
plt.xlabel('Amperagem (mA)')
plt.ylabel('Voltagem (V)')

plt.savefig('LabFisica-3/Relatorio2/grafico-lampada-pontos.png')

plt.close()
