import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dt1 = pd.read_csv('kplr010666592-2011240104155_slc.csv')
print(dt1)

print('nome colonne', dt1.columns)

dt1.plot(x='TIME', y='SAP_FLUX', kind='line')
plt.title('tempo/flusso')
plt.xlabel('tempo')
plt.ylabel('flusso')
plt.grid(True)
plt.show()

dt1.plot(x='TIME', y='SAP_FLUX', kind='scatter')
plt.title('tempo/flusso')
plt.xlabel('tempo')
plt.ylabel('flusso')
plt.grid(True)
plt.show()

plt.errorbar(dt1['TIME'], dt1['SAP_FLUX'], yerr=dt1['SAP_FLUX_ERR'], fmt= '.')
plt.title('tempo/flusso')
plt.xlabel('tempo')
plt.ylabel('flusso')
plt.grid(True)
plt.savefig('grafico1.png', dpi=300)
plt.show()

dt2 = dt1[( dt1['TIME'] > 943.404) & (dt1['TIME'] < 944.006 )]
plt.errorbar(dt2['TIME'], dt2['SAP_FLUX'], yerr=dt2['SAP_FLUX_ERR'], fmt= '.')
plt.title('tempo/flusso')
plt.xlabel('tempo')
plt.ylabel('flusso')
plt.grid(True)
plt.show()

fig, ax = plt.subplots(figsize=(12,6))
plt.errorbar(dt1['TIME'], dt1['SAP_FLUX'], yerr=dt1['SAP_FLUX_ERR'], fmt= '.')
plt.title('tempo/flusso')
plt.xlabel('tempo')
plt.ylabel('flusso')
plt.grid(True)
ins_ax = ax.inset_axes([0.7, 0.7, 0.4, 0.4]) 
ins_ax.errorbar( dt2['TIME'], dt2['SAP_FLUX'], yerr=dt2['SAP_FLUX_ERR'], fmt = '.' )
plt.show()
