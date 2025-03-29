import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error

path = r"C:\Users\divyu\OneDrive\Documents\GitHub\indigrow\updated_india_agriculture_dataset.csv"
try:
    df=pd.read_csv(path)
except FileNotFoundError:
    print("File not Found")
columns=['State','Crop','Soil','District','Irrigation Method','Best Next Crop']
for col in columns:
    if col not in df.columns:
        print(f"Column {col} is not in the dataset")
encoder=LabelEncoder()
for col in ['State', 'District', 'Soil', 'Crop', 'Irrigation Method', 'Best Next Crop']:
    df[col] = encoder.fit_transform(df[col])


x= df[['State','District','Crop','Soil',]]

#first model : it will predict the best irrigation method
y_predictor_irr=df['Irrigation Method']
x_train,x_test,y_train,y_test=train_test_split(x,y_predictor_irr,test_size=0.2,random_state=42)
#for training and tsteing, the random state is 42 and test size is .2
irr_model= RandomForestClassifier(n_estimators=100, random_state=42)
irr_model.fit(x_train,y_train)
y_irr_new=irr_model.predict(x_test)
print(f"Irrigation Accuracy: {accuracy_score(y_test,y_irr_new)*100:.2f}%")

#model 2: this predicts the est crop after the current crop is harvested

y_predictor_crop=df['Best Next Crop']
x_train,x_test,y_train,y_test=train_test_split(x,y_predictor_crop,test_size=0.2,random_state=42)
crop_model=RandomForestClassifier(n_estimators=100,random_state=42)
crop_model.fit(x_train,y_train)
y_crop_new=crop_model.predict(x_test)
print(f"Best Next Crop Accuracy: {accuracy_score(y_test,y_crop_new)*100:.2f}%")


#model 3: this will predict best yield accuracy

y_predictor_yield=df['Estimated Yield']
x_train,x_test,y_train,y_test=train_test_split(x,y_predictor_yield,test_size=0.2,random_state=42)
yield_model= RandomForestClassifier(n_estimators=100, random_state=42)
yield_model.fit(x_train,y_train)
y_yield_new=yield_model.predict(x_test)
print(f"Yield Accuracy: {accuracy_score(y_test,y_yield_new)*100:.2f}%")