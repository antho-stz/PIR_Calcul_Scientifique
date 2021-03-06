from math import *
from numpy import *
from matplotlib.pyplot import *

# SEITZ Anthony

"""Modèle épidémologique SIR, SIS, MSIR, SEIR, SEIS, MSEIR, MSEIRS :
S : (susceptible) population susceptible d'etre contaminee
I : (infected) population infectee
R : (recovered) population guerie
M : (maternal) nouveaux-nes immunise maternellement pour une duree provisoire
E : (exposed) population exposee

Avec u = [M,S,E,I,R], le modèle donne l'equation : du/dt = f(u)
avec f qui varie selon la complexite du modele. """


## Fonctions f du modele
def f_SIR(u,parametres):
    """Calcule f(u) selon le modele SIR sans dynamique demographique."""
    #R_0 = beta/gamma
    M = u[0]
    S = u[1]
    E = u[2]
    I = u[3]
    R = u[4]
    N = parametres[0]
    beta = parametres[1]
    gamma = parametres[2]
    Lambda = parametres[3]
    mu = parametres[4]
    delta = parametres[5]
    epsilon = parametres[6]
    sigma = parametres[7]
    rho = parametres[8]
    dM_dt = 0
    dS_dt = -beta*I*S/N
    dE_dt = 0
    dI_dt = beta*I*S/N - gamma*I
    dR_dt = gamma*I
    return array([dM_dt,dS_dt,dE_dt,dI_dt,dR_dt])

def f_SIR_dyn(u,parametres):
    """Calcule f(u) selon le modele SIR avec dynamique demographique."""
    #R_0 = beta*Lambda/mu/(mu+gamma)
    M = u[0]
    S = u[1]
    E = u[2]
    I = u[3]
    R = u[4]
    N = parametres[0]
    beta = parametres[1]
    gamma = parametres[2]
    Lambda = parametres[3]
    mu = parametres[4]
    delta = parametres[5]
    epsilon = parametres[6]
    sigma = parametres[7]
    rho = parametres[8]
    dM_dt = 0
    dS_dt = Lambda - mu*S - beta*I*S/N
    dE_dt = 0
    dI_dt = beta*I*S/N - gamma*I - mu*I
    dR_dt = gamma*I - mu*R
    return array([dM_dt,dS_dt,dE_dt,dI_dt,dR_dt])

def f_SIS(u,parametres):
    """Calcule f(u) selon le modele SIS sans dynamique demographique."""
    #R_0 = beta/gamma
    M = u[0]
    S = u[1]
    E = u[2]
    I = u[3]
    R = u[4]
    N = parametres[0]
    beta = parametres[1]
    gamma = parametres[2]
    Lambda = parametres[3]
    mu = parametres[4]
    delta = parametres[5]
    epsilon = parametres[6]
    sigma = parametres[7]
    rho = parametres[8]
    dM_dt = 0
    dS_dt = -beta*I*S/N + gamma*I
    dE_dt = 0
    dI_dt = beta*I*S/N - gamma*I
    dR_dt = 0
    return array([dM_dt,dS_dt,dE_dt,dI_dt,dR_dt])

def f_MSIR(u,parametres):
    """Calcule f(u) selon le modele MSIR avec dynamique demographique."""
    M = u[0]
    S = u[1]
    E = u[2]
    I = u[3]
    R = u[4]
    N = parametres[0]
    beta = parametres[1]
    gamma = parametres[2]
    Lambda = parametres[3]
    mu = parametres[4]
    delta = parametres[5]
    epsilon = parametres[6]
    sigma = parametres[7]
    rho = parametres[8]
    dM_dt = Lambda - delta*M - mu*M
    dS_dt = delta*M - beta*I*S/N - mu*S
    dE_dt = 0
    dI_dt = beta*I*S/N - (gamma+mu)*I
    dR_dt = gamma*I - mu*R
    return array([dM_dt,dS_dt,dE_dt,dI_dt,dR_dt])

def f_SEIR(u,parametres):
    """Calcule f(u) selon le modele SEIR avec dynamique demographique."""
    #R_0 = a/(mu+a)*beta/(mu+gamma)
    M = u[0]
    S = u[1]
    E = u[2]
    I = u[3]
    R = u[4]
    N = parametres[0]
    beta = parametres[1]
    gamma = parametres[2]
    Lambda = parametres[3]
    mu = parametres[4]
    delta = parametres[5]
    epsilon = parametres[6]
    sigma = parametres[7]
    rho = parametres[8]
    dM_dt = 0
    dS_dt = Lambda - mu*S - beta*I*S/N
    dE_dt = beta*I*S/N-(mu+epsilon)*E
    dI_dt = epsilon*E - (gamma+mu)*I
    dR_dt = gamma*I - mu*R
    return array([dM_dt,dS_dt,dE_dt,dI_dt,dR_dt])

def f_SEIS(u,parametres):
    """Calcule f(u) selon le modele SEIS avec dynamique demographique."""
    M = u[0]
    S = u[1]
    E = u[2]
    I = u[3]
    R = u[4]
    N = parametres[0]
    beta = parametres[1]
    gamma = parametres[2]
    Lambda = parametres[3]
    mu = parametres[4]
    delta = parametres[5]
    epsilon = parametres[6]
    sigma = parametres[7]
    rho = parametres[8]
    dM_dt = 0
    dS_dt = Lambda - mu*S - beta*I*S/N +gamma*I
    dE_dt = beta*I*S/N-(mu+epsilon)*E
    dI_dt = epsilon*E - (gamma+mu)*I
    dR_dt = 0
    return array([dM_dt,dS_dt,dE_dt,dI_dt,dR_dt])

def f_MSEIR(u,parametres):
    """Calcule f(u) selon le modele MSEIR avec dynamique demographique."""
    M = u[0]
    S = u[1]
    E = u[2]
    I = u[3]
    R = u[4]
    N = parametres[0]
    beta = parametres[1]
    gamma = parametres[2]
    Lambda = parametres[3]
    mu = parametres[4]
    delta = parametres[5]
    epsilon = parametres[6]
    sigma = parametres[7]
    rho = parametres[8]
    dM_dt = Lambda - (delta+mu)*M
    dS_dt = delta*M - mu*S - beta*I*S/N
    dE_dt = beta*I*S/N-(mu+epsilon)*E
    dI_dt = epsilon*E - (gamma+mu)*I
    dR_dt = gamma*I - mu*R
    return array([dM_dt,dS_dt,dE_dt,dI_dt,dR_dt])

def  f_MSEIRS(u,parametres):
    """Calcule f(u) selon le modele MSEIRS avec dynamique demographique."""
    M = u[0]
    S = u[1]
    E = u[2]
    I = u[3]
    R = u[4]
    N = parametres[0]
    beta = parametres[1]
    gamma = parametres[2]
    Lambda = parametres[3]
    mu = parametres[4]
    delta = parametres[5]
    epsilon = parametres[6]
    sigma = parametres[7]
    rho = parametres[8]
    dM_dt = Lambda - (delta+mu)*M
    dS_dt = delta*M - mu*S - beta*I*S/N + sigma*R
    dE_dt = beta*I*S/N-(mu+epsilon)*E
    dI_dt = epsilon*E - (gamma+mu)*I
    dR_dt = gamma*I - (mu+sigma)*R
    return array([dM_dt,dS_dt,dE_dt,dI_dt,dR_dt])


## Methodes de resolution
def Euler_explicite(u0,f,parametres):
    """Resout du/dt=f(u) avec la methode d'Euler explicite (ou Runge-Kutta d'ordre 1)."""
    U = [u0]
    u = u0
    for t in temps[:-1]:
        u = u + pas*f(u,parametres)
        U.append(u)
    return array(U)

def Newton(x0,h):
    """Resout l'equation h(x)=0 en partant de x0 avec la methode de Newton."""
    x = x0
    epsilon = 1e-5
    nb_max = 100
    delta = 1e-7
    for i in range(nb_max):
        dh = array([(h([x[j]+delta*(j==i) for j in range(len(x))])-h(x))/delta for i in range(len(x))])
        norm_dh2 = linalg.norm(dh)**2
        if norm_dh2<epsilon:
            print("Probleme : impossible de resoudre le modele avec la methode d'Euler implicite : division par 0 lors de la methode de Newton !\n")
            break
        else:
            dx = -h(x)*dh/norm_dh2
            x = x + dx
            if linalg.norm(dx) < epsilon:
                break
    return x

def Euler_implicite(u0,f,parametres):
    """Resout du/dt=f(u) avec la methode d'Euler implicite."""
    U = [u0]
    u = u0
    for t in temps[:-1]:
        u = Newton(u,lambda x : linalg.norm(u-x+pas*f(u,parametres)))
        U.append(u)
    return array(U)

def Heun(u0,f,parametres):
    """Resout du/dt=f(u) avec la methode de Heun."""
    U = [u0]
    u = u0
    for t in temps[:-1]:
        u = u + pas/2*(f(u,parametres)+f(u+pas*f(u,parametres),parametres))
        U.append(u)
    return array(U)

def Runge_Kutta_2(u0,f,parametres):
    """Resout du/dt=f(u) avec la methode de Runge-Kutta d'ordre 2."""
    U = [u0]
    u = u0
    for t in temps[:-1]:
        u = u + pas*f(u+pas/2*f(u,parametres),parametres)
        U.append(u)
    return array(U)

def Runge_Kutta_4(u0,f,parametres):
    """Resout du/dt=f(u) avec la methode de Runge-Kutta d'ordre 4."""
    U = [u0]
    u = u0
    for t in temps[:-1]:
        k1 = f(u,parametres)
        k2 = f(u+pas/2*k1,parametres)
        k3 = f(u+pas/2*k2,parametres)
        k4 = f(u+pas*k3,parametres)
        u = u + pas/6*(k1+2*k2+2*k3+k4)
        U.append(u)
    return array(U)


## Trace
def trace(U,modele=None,methode=None,cree=True):
    """Trace les solutions obtenues u en ouvrant une nouvelle fenetre si cree=True."""
    M = U[:,0]
    S = U[:,1]
    E = U[:,2]
    I = U[:,3]
    R = U[:,4]
    titre = "Evolution de l'epidemie au cours du temps"
    if cree:
        figure()
        plot(temps,M,':',color="yellow",label="M")
        plot(temps,S,':',color="blue",label="S")
        plot(temps,E,':',color="orange",label="E")
        plot(temps,I,':',color="red",label="I")
        plot(temps,R,':',color="green",label="R")
        if modele != None:
            titre += " modele " + noms_modeles[modeles.index(modele)]
        if methode != None:
            titre += " (methode " + noms_methodes[methodes.index(methode)] + ")"
        legend()
    else:
        plot(temps,M,':',color="yellow")
        plot(temps,S,':',color="blue")
        plot(temps,E,':',color="orange")
        plot(temps,I,':',color="red")
        plot(temps,R,':',color="green")
    title(titre)
    xlabel("Temps en jours")
    ylabel("Population")


## Resolution

def solution(modele,u0,cree):
    """Trace la solution exacte du modele selon la fonction f du modele choisie en ouvrant une nouvelle fenetre si cree=True."""
    U=[u0]
    for t in temps[:-1]:
        #A completer
        U.append(u0)
    trace(U,modele,cree)
    return array(U)

def resolution(methode,modele,parametres,u0,cree):
    """Resout numeriquement le modele a partir de u0 selon la fonction f du modele et avec la methode de
    resolution choisies et trace la solution en ouvrant une nouvelle fenetre si cree=True."""
    U = methode(u0,modele,parametres)
    trace(U,modele,methode,cree)
    return U


## Parametres

# Parametres d'affichage
duree = 80 # Duree (jour)
nb_pts = 10000
pas = duree/nb_pts
temps = linspace(0,duree,nb_pts)

# Parametres de modelistaion
N = 100000 # Population totale
beta = 1.4 # Contact par pers. infectee par jour
gamma = 1/12 # Inverse de la duree de guerison
Lambda = 0.012/365*N # Natalite (nb/jour)
mu = 0.009/365 # Taux de mortalite (nb/pers/jour)
delta = 0.012/365 # Taux de desimmunisation (nb/pers/jour)
epsilon = 1/5 # Inverse de la duree d'incubation
sigma = 1/30 # Inverse de la duree d'immunite (modele MSEIRS)
rho = 0.01 # Taux de letalite de l'epidemie
# R_0 represente le nombre de contact par pers. infectee, varie selon le choix de f.

parametres = [N,beta,gamma,Lambda,mu,delta,epsilon,sigma,rho]

modeles = [f_SIR,f_SIR_dyn,f_SIS,f_MSIR,f_SEIR,f_SEIS,f_MSEIR,f_MSEIRS]
noms_modeles = ["SIR","SIR","SIS","MSIR","SEIR","SEIS","MSEIR","MSEIRS"]
modeles_avec_dyn = [f_SIR_dyn,f_MSIR,f_SEIR,f_SEIS,f_MSEIR,f_MSEIRS]
modeles_sans_dyn = [f_SIR,f_SIS]

# Parametres de resolution
proportion_M0_dans_N = 0
M0 = proportion_M0_dans_N*N
E0 = 0
I0 = 10
S0 = N-I0-M0
R0 = 0
u0 = array([M0,S0,E0,I0,R0]) # [M,S,E,I,R]

methode = Runge_Kutta_4 # Methode de resolution
modele = f_SIR # Modele d'epidemie
cree = True # Affiche le resultat sur une nouvelle fenetre

methodes = [Euler_explicite,Euler_implicite,Heun,Runge_Kutta_2,Runge_Kutta_4]
noms_methodes = ["Euler_explicite","Euler_implicite","Heun","Runge_Kutta_2","Runge_Kutta_4"]


## Affichage

#resolution(methode,modele,parametres,u0,cree)

"""
for modele in modeles_avec_dyn:
    if 'M' in noms_modeles[modeles.index(modele)]:
        M0 = proportion_M0_dans_N*N
        u0 = array([M0,N-I0-M0,0,I0,0])
    else:
        u0 = array([0,N-I0,0,I0,0])
    resolution(methode,modele,parametres,u0,True)
    grid()#"""

#resolution(Runge_Kutta_4,f_SIR,parametres,u0,True)
#resolution(Runge_Kutta_4,f_SIR_dyn,parametres,u0,True)
U=resolution(Runge_Kutta_4,modele,parametres,u0,True)

grid()
show()





