# Présentation du Projet
Ce projet se concentre sur la compréhension des tendances de la performance des employés à travers des analyses statistiques et des visualisations de données. En analysant les statistiques descriptives et en détectant les valeurs aberrantes dans les heures de travail et les scores de performance des employés, l'objectif est de fournir des informations qui aideront la direction à optimiser ses stratégies RH pour améliorer la productivité et la satisfaction des employés.

# Données Utilisées
Le jeu de données contient les informations suivantes :

-	Données des Employés : Département, niveau d'éducation, satisfaction, etc.
-	Indicateurs de Performance : Scores de performance, nombre de projets gérés, heures de travail, heures de formation, etc.
-	Facteurs RH : Salaire, heures supplémentaires, absences, etc.

# source : https://www.kaggle.com/datasets/rhuebner/human-resources-data-set
# Outils et Technologies
Python : Pandas, Seaborn, Matplotlib

# Méthodologie et Approche
## Statistiques Descriptives :
Calcul de la moyenne, médiane, quartiles et écart-type pour analyser la performance des employés.
## Visualisation des Données :
-	Création d'histogrammes pour explorer la distribution des scores de performance et des heures de travail.
-	Utilisation de boxplots pour identifier les tendances de performance et les disparités salariales.
-	Génération de diagrammes à barres pour comparer la performance entre départements.
## Détection des Valeurs Aberrantes :
-	Application de la règle 1,5 * IQR (plage interquartile) pour détecter les anomalies dans les heures de travail et les scores de performance des employés.
## Insights et Recommandations :
-	Fourniture d'informations sur la distribution de la performance pour aider la direction à prendre des décisions RH basées sur les données.
# Résultats Clés
-	La plupart des employés ayant de meilleurs scores de performance ont également plus d'heures de formation et une plus grande implication dans les projets.
-	Des valeurs aberrantes dans les heures de travail et les scores de performance ont été identifiées et analysées, ce qui pourrait indiquer des problèmes liés à l'équilibre travail-vie personnelle ou une performance incohérente.
-	Des disparités salariales ont été observées entre les départements, ce qui pourrait être exploré pour une optimisation future.

