
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

ruta_archivo = ('Dataset-Mental-Disorders.csv')
df = pd.read_csv(ruta_archivo)

#df.info()

df = df.drop(columns=['Patient Number'])
#df.head()

labelencoder= LabelEncoder()

# transformar la columna sentimientos en una matriz de características numéricas
df['Sadness'] = labelencoder.fit_transform(df['Sadness'])
df['Exhausted'] = labelencoder.fit_transform(df['Exhausted'])
df['Euphoric'] = labelencoder.fit_transform(df['Euphoric'])
df['Sleep dissorder'] = labelencoder.fit_transform(df['Sleep dissorder'])
df['Mood Swing'] = labelencoder.fit_transform(df['Mood Swing'])
df['Suicidal thoughts'] = labelencoder.fit_transform(df['Suicidal thoughts'])
df['Anorxia'] = labelencoder.fit_transform(df['Anorxia'])
df['Authority Respect'] = labelencoder.fit_transform(df['Authority Respect'])
df['Try-Explanation'] = labelencoder.fit_transform(df['Try-Explanation'])
df['Aggressive Response'] = labelencoder.fit_transform(df['Aggressive Response'])

df['Ignore & Move-On'] = labelencoder.fit_transform(df['Ignore & Move-On'])
df['Nervous Break-down'] = labelencoder.fit_transform(df['Nervous Break-down'])
df['Admit Mistakes'] = labelencoder.fit_transform(df['Admit Mistakes'])
df['Overthinking'] = labelencoder.fit_transform(df['Overthinking'])

df['Sexual Activity'] = labelencoder.fit_transform(df['Sexual Activity'])
df['Concentration'] = labelencoder.fit_transform(df['Concentration'])
df['Optimisim'] = labelencoder.fit_transform(df['Optimisim'])
df['Expert Diagnose'] = labelencoder.fit_transform(df['Expert Diagnose'])

#df.head()

#df['Expert Diagnose']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df.drop('Expert Diagnose', axis=1), df['Expert Diagnose'], test_size=0.30)
print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)

naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)
y_pred = naive_bayes.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo de Naive Bayes:", accuracy)

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


ruta_archivo = ('Dataset-Mental-Disorders.csv')
df = pd.read_csv(ruta_archivo)


df = df.drop(columns=['Patient Number'])


labelencoder = LabelEncoder()


for column in df.columns:
    df[column] = labelencoder.fit_transform(df[column])


X = df.drop('Expert Diagnose', axis=1)
y = df['Expert Diagnose']


y = labelencoder.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)


naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)


y_pred = naive_bayes.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)


new_data = {
    'Sadness': 2,
    'Exhausted': 1,
    'Euphoric': 0,
    'Sleep dissorder': 1,
    'Mood Swing': 0,
    'Suicidal thoughts': 0,
    'Anorxia': 0,
    'Authority Respect': 1,
    'Try-Explanation': 1,
    'Aggressive Response': 0,
    'Ignore & Move-On': 0,
    'Nervous Break-down': 0,
    'Admit Mistakes': 1,
    'Overthinking': 1,
    'Sexual Activity': 1,
    'Concentration': 1,
    'Optimisim': 0
}


new_data_df = pd.DataFrame(new_data, index=[0])


for column in new_data_df.columns:
    new_data_df[column] = labelencoder.transform([new_data_df[column]])[0]

column_order = X_train.columns
new_data_df = new_data_df[column_order]
prediction = naive_bayes.predict(new_data_df)
predicted_disorder_label = labelencoder.inverse_transform(prediction)[0]
#print("Precisión del modelo de Naive Bayes:", accuracy)

#print("Trastorno mental predicho:", predicted_disorder_label)

# Mapeo de números a etiquetas de trastornos mentales
diagnose_mapping = {
    0: 'Bipolar Type-1',
    1: 'Bipolar Type-2',
    2: 'Depression',
    3: 'Normal'
    # Agrega más mapeos si hay más etiquetas en tu conjunto de datos
}

# Predecir con el modelo entrenado
prediction = naive_bayes.predict(new_data_df)

# Convertir la predicción nuevamente a texto utilizando el mapeo
predicted_disorder_label = diagnose_mapping[prediction[0]]

print("Trastorno mental predicho:", predicted_disorder_label)