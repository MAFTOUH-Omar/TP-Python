import numpy as np

# Génération des données aléatoires pour X et Y
X = np.random.normal(loc=100 , scale=20, size=(1 , 12))
Y = np.random.normal(loc=120 , scale=25, size=(1 , 12))

# Calcul de l'écart-type pour X et Y
ecartTypeX = np.std(X)
ecartTypeY = np.std(Y)
print(f"Ecart Type du X : {ecartTypeX}")
print(f"Ecart Type du Y : {ecartTypeY}")

""""
    Pour X, un écart-type de 20 signifie que les ventes mensuelles varient d'environ 20 unités autour de la moyenne.
    Pour Y, un écart-type de 25 signifie que les ventes mensuelles varient d'environ 25 unités autour de la moyenne.
"""

# Calcul du coefficient de corrélation entre X et Y
CoeCorrelationX = np.corrcoef(X , Y)
print(f"le coefficient de correlation : \n{CoeCorrelationX}")

""""
    Un coefficient de corrélation proche de 1 indiquerait une corrélation positive, c'est-à-dire que lorsque les ventes mensuelles de X augmentent, les ventes mensuelles de Y ont tendance à augmenter également.
    Un coefficient de corrélation proche de -1 indiquerait une corrélation négative, ce qui signifie que lorsque les ventes mensuelles de X augmentent, les ventes mensuelles de Y ont tendance à diminuer.
    Un coefficient de corrélation proche de 0 indiquerait une faible corrélation linéaire entre les ventes mensuelles de X et de Y.
"""

# 4

""""
    Un écart type plus élevé indique une plus grande variabilité des ventes mensuelles. 
    Ainsi, un écart-type élevé pour un produit indique que les ventes fluctuent davantage autour de la moyenne, 
    ce qui peut indiquer une demande plus volatile ou des facteurs externes affectant les ventes de manière significative.
"""

# 5

""""
    Le coefficient de corrélation mesure la relation linéaire entre les ventes de X et Y.
    Un coefficient positif indique une tendance à augmenter ensemble, tandis qu'un coefficient négatif indique une tendance inverse.
    Un coefficient proche de zéro indique une faible relation linéaire.
    En utilisant ce coefficient, on peut évaluer l'ampleur et la signification de la relation entre les ventes de X et Y.
"""