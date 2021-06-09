#-----------------------------------------------------------------------
# Diagramme binaire
#-----------------------------------------------------------------------
# Renseignements/bugs : Guillaume Dewaele <agreg(at)sci-phy.org>
#-----------------------------------------------------------------------

# Espèce 1

E1 = r"$thymol_{sol}$"  # Nom
M1 = 150.22e-3             # Masse molaire, g/mol
Tf1 = 50                   # Température de fusion, °C
col1 = 'g'                 # Couleur sur le graphe

# Espèce 2

E2 = r"$acide palamitique_{sol}$" # Nom
E2r = r"acide palamitique"     # Nom (abscisses)
M2 = 256.42e-3         # Masse molaire, g/mol
Tf2 = 63               # Température de fusion, °C
col2 = 'b'             # Couleur sur le graphe

# Solide

col3 = 'r'             # Couleur sur le graphe


# Points
# (fraction massique, température, err_fraction, err_temperature, couleur)

points = [
  ('k', [ (0, 48.3, 0.02, 1),
          (0.1, 44.5, 0.02, 1),
          (0.24, 40, 0.02, 1),
          (0.5, 50.7, 0.02, 1) ]),
  ('b', [ (1, 62, 0.02, 1) ])
]

#-----------------------------------------------------------------------

# Bibliothèques utilisées

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
import matplotlib.pylab as plb

#-----------------------------------------------------------------------

memParams = plb.rcParams

plb.rcParams.update(
  { 'legend.fontsize' : 'medium',
    'axes.labelsize' : 'medium',
    'axes.titlesize' : 'medium',
    'xtick.labelsize' : 'medium',
    'ytick.labelsize' : 'medium',
    'font.size' : 12 })

# Détection utilisation hors Pyzo

if '__iep__' not in globals() :
    matplotlib.interactive(False)


# Calcul du point E

wE = 0.24
TE = 40

# Calcul de l'échelle verticale

Tmin = 20
Tmax = 80

# Séparation des donnees

W = np.array([0,0.1,0.24,0.5,1])
W1 = np.array([0,0.1,0.24])
W2 = np.array([0.24,0.5,1])
T = np.array([48.3,44.5,40,50.7,62])
T1 = np.array([48.3,44.5,40])
T2 = np.array([40,50.7,62])

# Tracé

plt.figure(figsize=(10, 8))

plt.fill_between(W, Tmin*np.ones(W.shape), T, color=col3, alpha=0.2)
plt.fill_between(W1, TE*np.ones(W1.shape), T1, color=col1, alpha=0.2)
plt.fill_between(W2, TE*np.ones(W2.shape), T2, color=col2, alpha=0.2)

plt.text(0.5, (TE+Tmin)/2.0, E1+"+"+E2, fontsize=16, ha="center", va="center", color='r')
plt.text(wE/3.0, (3*TE+Tf1)/4.0, "L+"+E1, fontsize=16, ha="center", va="center", color='g')
plt.text((2+wE)/3.0, (3*TE+Tf2)/4.0, "L+"+E2, fontsize=16, ha="center", va="center", color='b')
plt.text(wE, (2*max(Tf1, Tf2)+min(Tf1, Tf2))/3.0, "L", fontsize=16, ha="center", va="center")

plt.annotate("liquidus", (0.7, 55),(0.6, 65), arrowprops=dict(facecolor='black', alpha=0.3, shrink=0.1), ha='left', va='bottom', alpha=0.5, fontsize=12)
plt.annotate("liquidus", (0.15, 43),(0.25, 53), arrowprops=dict(facecolor='black', alpha=0.3, shrink=0.1), ha='right', va='bottom', alpha=0.5, fontsize=12)

plt.text(wE+0.008, TE-2.5, "E", fontsize=12)

# Points

for col, lst in points :
    plt.errorbar([ e[0] for e in lst ],
                 [ e[1] for e in lst ],
                 [ e[3] for e in lst ],
                 [ e[2] for e in lst ],
                 fmt='s', color=col)

# Fignolage

plt.gca().tick_params(right=True, labelright=True)

plt.grid(alpha=0.3)
plt.xlim(0, 1)
plt.ylim(Tmin, Tmax)

plt.ylabel(r"Température T (°C)")
plt.xlabel(r"Fraction massique w en acide palmitique")

plt.title("diagramme binaire de l'acide palmitique et du thymol")

#-----------------------------------------------------------------------

plb.rcParams.update(memParams)

# Détection utilisation hors Pyzo

if '__iep__' not in globals() :
    plt.show()