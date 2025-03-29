import pandas as pd
#import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error
path = r'C:\Users\anshv\OneDrive - Manipal Academy of Higher Education\Documents\GitHub\indigrow\Shreyansh\updated_india_agriculture_dataset.csv'
try:
    df=pd.read_csv(path)
except FileNotFoundError:
    print("File not Found")
#columns=['State','Crop','Soil','District','Irrigation Method','Best Next Crop']
columns=["State","Soil Type","Crop","District","Best Fertilizer","Alternative Fertilizer"]
for col in columns:
    if col not in df.columns:
        print(f"Column {col} is not in the dataset")
encoder=LabelEncoder()
#for col in ['State', 'District', 'Soil', 'Crop', 'Irrigation Method', 'Best Next Crop']:
for col in ["State","Soil Type","Crop","District","Best Fertilizer","Alternative Fertilizer"]:
    df[col] = encoder.fit_transform(df[col])


x= df[['State','District','Crop','Soil Type']]


#model 3(Shresh's model)

y_predictor_fert=df['Best Fertilizer']
x_train,x_test,y_train,y_test=train_test_split(x,y_predictor_fert,test_size=0.2,random_state=42)
#for training and tsteing, the random state is 42 and test size is .2
fert_model= RandomForestClassifier(n_estimators=100, random_state=42)
fert_model.fit(x_train,y_train)
y_fert_new=fert_model.predict(x_test)
print(f"Irrigation Accuracy: {accuracy_score(y_test,y_fert_new)*100:.2f}%")


y_predictor_alt=df['Alternate Fertilizer']
x_train,x_test,y_train,y_test=train_test_split(x,y_predictor_alt,test_size=0.2,random_state=42)
#for training and tsteing, the random state is 42 and test size is .2
alt_model= RandomForestClassifier(n_estimators=100, random_state=42)
alt_model.fit(x_train,y_train)
y_alt_new=alt_model.predict(x_test)
print(f"Irrigation Accuracy: {accuracy_score(y_test,y_alt_new)*100:.2f}%")