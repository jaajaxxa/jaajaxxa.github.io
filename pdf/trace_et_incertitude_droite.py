import numpy as np
import scipy.optimize as spo
import matplotlib.pyplot as plt

# données expérimentales
"""
donnees = np.loadtxt("G:\Prépa Agreg\MP\MP17 Métaux\Table1.txt")
x=donnees[:,0]
ux=donnees[:,1]
y=donnees[:,2]
uy=donnees[:,3]
"""
x = np.array([1.0,2.1,3.1,3.9])
y = np.array([2.1,3.9,6.1,7.8])
# incertitudes-types sur les données expérimentales
ux = np.array([0.2,0.3,0.2,0.2])
uy = np.array([0.3,0.3,0.2,0.3])
x_live=np.array([2.1])
y_live=np.array([3.9])
ux_live=np.array([0.3])
uy_live=np.array([0.3])


# fonction f décrivant la courbe à ajuster aux données
def f(x,p):
    a,b = p 
    return a*x+b
# dérivée de la fonction f par rapport à la variable de contrôle x
def Dx_f(x,p):
    a,b = p
    return a

# fonction d'écart pondérée par les erreurs
def residual(p, y, x):
    return (y-f(x,p))/np.sqrt(uy**2 + (Dx_f(x,p)*ux)**2)

# estimation initiale des paramètres
# elle ne joue généralement aucun rôle
# néanmoins, le résultat de l'ajustement est parfois aberrant
# il faut alors choisir une meilleure estimation initiale
p0 = np.array([0,0])

# on utilise l'algorithme des moindres carrés non-linéaires 
# disponible dans la biliothèque scipy (et indirectement la
# bibliothèque Fortran MINPACK qui implémente l'algorithme
# de Levenberg-Marquardt) pour déterminer le minimum voulu
result = spo.leastsq(residual, p0, args=(y, x), full_output=True)

# on obtient :
# les paramètres d'ajustement optimaux
popt = result[0];
# la matrice de variance-covariance estimée des paramètres
pcov = result[1];
# les incertitudes-types sur ces paramètres
upopt = np.sqrt(np.abs(np.diagonal(pcov)))

# calcul de la valeur du "chi2 réduit" pour les paramètres ajustés
chi2r = np.sum(np.square(residual(popt,y,x)))/(x.size-popt.size)

# tracé des fonctions et de l'ajustement
plt.errorbar(x,y,xerr=ux,yerr=uy,fmt="o",color="b",ecolor="b")
plt.plot(x,f(x,popt),color="r")

# ajout du point en live sur le tracé
plt.errorbar(x_live,y_live,xerr=ux_live,yerr=uy_live,fmt="o",color="g",ecolor="g")

# ajout legendes et texte
plt.xlabel("L en m")
plt.ylabel("U en V")
plt.title("ajustement de U en fonction de L")
plt.text(1,7,"y = ax+b \na = {} $\pm$ {} \nb = {} $\pm$ {}".format(round(popt[0],5),round(upopt[0],5),round(popt[1],5),round(upopt[1],5)))



plt.show()