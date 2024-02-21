import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialisation de Faker pour générer des données factices
fake = Faker()

# Définition du nombre de lignes dans le DataFrame
num_rows = 100

# Génération des données
dataClient = {
    'nom': [fake.last_name() for _ in range(num_rows)],
    'prenom': [fake.first_name() for _ in range(num_rows)],
    'age': [random.randint(20, 65) for _ in range(num_rows)],
    'salaire': [random.randint(30000, 150000) for _ in range(num_rows)],
    'email': [fake.email() for _ in range(num_rows)],
    'date_naissance': [fake.date_of_birth(minimum_age=20, maximum_age=65) for _ in range(num_rows)]
}

dataProduits = {
    'libelle': [fake.word() for _ in range(num_rows)],
    'prix': [round(random.uniform(10, 1000), 2) for _ in range(num_rows)],
    'quantite': [random.randint(1, 100) for _ in range(num_rows)],
    'etat': [random.choice(["disponible", "rupture"]) for _ in range(num_rows)],
    'nb_achats': [random.randint(0, 50) for _ in range(num_rows)]
}

# Création du DataFrame
df = pd.DataFrame(dataProduits)

# Enregistrement du DataFrame au format CSV
df.to_csv('produits.csv', index=False)
