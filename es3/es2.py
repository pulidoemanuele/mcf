import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import MultipleLocator


dt1 = pd.read_csv('ExoplanetsPars_2025.csv', comment='#')

"""
plt.scatter( dt1['pl_orbper'], dt1['pl_bmassj'], color='royalblue', s= 25, label='pianeti')
plt.title('periodo/massa')
plt.xlabel('periodo orbitale')
plt.ylabel('massa del pianeta')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()
"""

'''
a1 = np.array([ dt1['pl_orbsmax'] ])
a2 = np.array([ dt1['st_mass'] ])
a3 = a1**2 / a2

plt.scatter( dt1['pl_orbper'], a3, color='royalblue', s= 25 )
plt.title('r^2/m*')
plt.xlabel('periodo orbitale')
plt.ylabel('r^2/m*')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()
'''


dt2 = dt1[( dt1['discoverymethod'] == 'Transit')]
dt3 = dt1[( dt1['discoverymethod'] == 'Radial Velocity')]


'''
plt.scatter( dt2['pl_orbper'], dt2['pl_bmassj'], color='royalblue', s= 15, label='transit', alpha= 0.4)
plt.scatter( dt3['pl_orbper'], dt3['pl_bmassj'], color='red', s= 15, label='rad-vel', alpha= 0.4)
plt.title('periodo/massa')
plt.xlabel('periodo orbitale')
plt.ylabel('massa del pianeta')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()
'''

'''
plt.hist( dt2['pl_bmassj'], bins=200, alpha=0.4, color= 'red', align= 'mid')
plt.hist( dt3['pl_bmassj'], bins=200, alpha=0.4, color= 'royalblue', align='mid')
plt.xlim(0, 4)
plt.gca().xaxis.set_major_locator(MultipleLocator(0.02))
plt.xlabel('massa del pianeta', fontsize= 12)
plt.show()
'''


'''
plt.hist( dt2['pl_bmassj'], bins=200, alpha=0.4, color= 'red', align= 'mid')
plt.hist( dt3['pl_bmassj'], bins=200, alpha=0.4, color= 'royalblue', align=>
plt.xlim(0, 4)
plt.xscale('log')
plt.gca().xaxis.set_major_locator(MultipleLocator(0.02))
plt.xlabel('massa del pianeta', fontsize= 12)
plt.show()
'''



plt.scatter( np.log(dt2['pl_orbper']), np.log(dt2['pl_bmassj']), color='royalblue', s= 15 )
plt.scatter( np.log(dt3['pl_orbper']), np.log(dt3['pl_bmassj']), color='red', s= 15 )
plt.title('periodo/massa')
plt.xlabel('periodo orbitale')
plt.ylabel('massa del pianeta')
plt.grid(True)
plt.show()
