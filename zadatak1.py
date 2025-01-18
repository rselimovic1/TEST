# -*- coding: utf-8 -*-
"""Zadatak1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qhv42_DhV44j83BBFYKH91d5aDji91aq
"""

# STUDENT: Rajza Selimović
# BR. INDEKSA: 18695/2302

import numpy as np
from matplotlib import pyplot as plt

"""**ZADATAK 1:**

Neka je slučajna promjenjiva podvrgnuta uniformnoj raspodjeli. Odabrati N koje predstavlja koliko je puta sproveden eksperiment čiji je ishod slučajna promjenjiva. Sprovesti eksperiment N puta i sačuvati sve vrijednosti. Na grafiku prikazati sve ishode eksperimenata.
"""

N = 1000; # broj provedenih eksperimenara

a = 2;
b = 6;
X = np.random.uniform(a,b,N);
n = range(N)

plt.title("Uniformna raspodjela");
plt.xlabel("Realizacija n");
plt.ylabel("Slučajna promjenljiva X");
plt.scatter(n,X,color='pink');

"""Nacrtati histogram slučajne varijable."""

plt.hist(X, bins = N, color = 'pink');
plt.grid();
plt.title("Uniformna raspodjela");

"""Izračunati očekivanu vrijednost/srednjekvadratnu vrijednost/varijansu na osnovu izvedene formule i uporediti je sa očekivanom vrijednosti/srednjekvadratnom vrijednosti/varijansom koja je
dobijena na osnovu eksperimenta.

"""

E_formula = (a+b)/2
E_eksperiment = np.mean(X)
print("Očekivana vrijednost na osnovu formule je %.2f, a dobijena je %.2f. Razlika: %.2f.\n"%(E_formula, E_eksperiment, E_formula - E_eksperiment))

E2_formula = (a**2 + a*b + b**2)/3
E2_eksperiment = np.mean(X**2);
print("Očekivana vrijednost na osnovu formule je %.2f, a dobijena je %.2f. Razlika: %.2f.\n"%(E2_formula, E2_eksperiment, E2_formula - E2_eksperiment))

Var_formula = (a-b)**2/12;
Var_eksperiment = np.var(X);
print("Očekivana vrijednost na osnovu formule je %.2f, a dobijena je %.2f. Razlika: %.2f.\n"%(Var_formula, Var_eksperiment, Var_formula-Var_eksperiment))

"""Demonstrirati kako se razlika vrijednosti spomenutih u prošlim stavkama (očekivana vrijednost, srednjekvadratna vrijednost, varijansa) mijenja u zavisnosti od broja sprovedenih eksperimenata.

"""

N = 10;
X = np.random.uniform(a,b,N);

E_formula = (a+b)/2
E_dobijena = np.mean(X)
print("Razlika: %.2f.\n"%(E_formula - E_dobijena))

E2_formula = (a**2 + a*b + b**2)/3
E2_dobijena = np.mean(X**2);
print("Razlika: %.2f.\n"%(E2_formula - E2_dobijena))

Var_formula = (a-b)**2/12;
Var_dobijena = np.var(X);
print("Razlika: %.2f.\n"%(Var_formula - Var_dobijena))

N = 100;
X = np.random.uniform(a,b,N);

E_formula = (a+b)/2
E_dobijena = np.mean(X)
print("Razlika: %.2f.\n"%(E_formula - E_dobijena))

E2_formula = (a**2 + a*b + b**2)/3
E2_dobijena = np.mean(X**2);
print("Razlika: %.2f.\n"%(E2_formula - E2_dobijena))

Var_formula = (a-b)**2/12;
Var_dobijena = np.var(X);
print("Razlika: %.2f.\n"%(Var_formula - Var_dobijena))

"""Zaključak: Razlika se smanjuje sa povećanjem broja provedenih eksperimenata."""

print("Medijana: {:.2f}".format(np.median(X)))