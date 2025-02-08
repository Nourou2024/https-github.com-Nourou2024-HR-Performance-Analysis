#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


dataset = pd.read_csv("HRDataset_v14.csv") 


# In[3]:


dataset.head()


# In[4]:





# In[5]:





# In[6]:


import pandas as pd
import numpy as np


# In[7]:


mean_value = df["Absences"].mean()


# In[8]:


import pandas as pd
import numpy as np


# In[9]:


# Moyenne
mean_value = df["Absences"].mean()

# Médiane
median_value = df["Absences"].median()

# Quartiles
Q1 = df["Absences"].quantile(0.25)  # 1er quartile (25%)
Q3 = df["Absences"].quantile(0.75)  # 3ème quartile (75%)

# Écart-type
std_dev = df["Absences"].std()

# IQR (Interquartile Range)
IQR = Q3 - Q1

# Affichage des résultats
print(f"Moyenne: {mean_value}")
print(f"Médiane: {median_value}")
print(f"1er Quartile (Q1): {Q1}")
print(f"3ème Quartile (Q3): {Q3}")
print(f"Écart-type: {std_dev}")
print(f"IQR (Écart interquartile): {IQR}")


# In[10]:


import pandas as pd
import numpy as np


# In[11]:


df = pd.read_csv("HRDataset_v14.csv")  


# In[12]:


# Moyenne
mean_value = df["Absences"].mean()

# Médiane
median_value = df["Absences"].median()

# Quartiles
Q1 = df["Absences"].quantile(0.25)  # 1er quartile (25%)
Q3 = df["Absences"].quantile(0.75)  # 3ème quartile (75%)

# Écart-type
std_dev = df["Absences"].std()

# IQR (Interquartile Range)
IQR = Q3 - Q1

# Affichage des résultats
print(f"Moyenne: {mean_value}")
print(f"Médiane: {median_value}")
print(f"1er Quartile (Q1): {Q1}")
print(f"3ème Quartile (Q3): {Q3}")
print(f"Écart-type: {std_dev}")
print(f"IQR (Écart interquartile): {IQR}")


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("HRDataset_v14.csv")  


# In[3]:


plt.figure(figsize=(8, 5))
sns.histplot(df["Absences"], bins=10, kde=True, color="blue")
plt.title("Distribution des absences des employés")
plt.xlabel("Nombre d'absences")
plt.ylabel("Nombre d'employés")
plt.show()


# In[4]:


plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Absences"], color="orange")
plt.title("Boxplot des absences")
plt.xlabel("Nombre d'absences")
plt.show()


# In[5]:


plt.figure(figsize=(8, 5))
sns.countplot(x=df["PerformanceScore"], palette="viridis")
plt.title("Répartition des scores de performance")
plt.xlabel("Score de Performance")
plt.ylabel("Nombre d'employés")
plt.show()


# In[6]:


plt.figure(figsize=(8, 5))
sns.barplot(x="PerformanceScore", y="Absences", data=df, palette="coolwarm")
plt.title("Absences moyennes par score de performance")
plt.xlabel("Score de Performance")
plt.ylabel("Moyenne des absences")
plt.show()


# In[7]:


plt.figure(figsize=(6, 6))
df["PerformanceScore"].value_counts().plot.pie(autopct="%1.1f%%", cmap="coolwarm", startangle=90)
plt.title("Répartition des scores de performance")
plt.ylabel("")  # Cacher le label y
plt.show()


# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


df = pd.read_csv("HRDataset_v14.csv")  


# In[10]:


#  à analyser (ex: Absences)
column = "Absences"

# Calcul des quartiles
Q1 = df[column].quantile(0.25)  # 1er quartile (25%)
Q3 = df[column].quantile(0.75)  # 3ème quartile (75%)

# Calcul de l'IQR (Interquartile Range)
IQR = Q3 - Q1

# Définition des bornes pour les outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filtrer les valeurs aberrantes
outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

# Affichage des outliers détectés
print("Valeurs aberrantes détectées :")
print(outliers[[column, "Employee_Name", "PerformanceScore"]])  # Ajouter d'autres colonnes si nécessaire


# In[11]:


plt.figure(figsize=(6, 4))
sns.boxplot(x=df[column], color="orange")
plt.title(f"Boxplot de {column} avec outliers")
plt.xlabel(column)
plt.show()


# In[12]:


columns_to_check = ["Absences", "PerfScoreID"]  # les colonnes

for col in columns_to_check:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    
    print(f"\n🔍 Outliers pour {col}:")
    print(outliers[[col, "Employee_Name", "PerformanceScore"]])


# In[ ]:




