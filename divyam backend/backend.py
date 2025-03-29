import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error



l1=["Karnataka","South","Saline","Cotton"]
path = r"C:\Users\divyu\OneDrive\Documents\GitHub\indigrow\updated_india_agriculture_dataset.csv"
try:
    df=pd.read_csv(path)
except FileNotFoundError:
    print("File not Found")



columns=['State','Crop','Soil','District','Irrigation Method','Best Next Crop','Best Fertilizer']
for col in columns:
    if col not in df.columns:
        print(f"Column {col} is not in the dataset")
encoders = {}
for col in ['State', 'District', 'Soil', 'Crop', 'Irrigation Method', 'Best Next Crop','Best Fertilizer']:
    encoders[col] = LabelEncoder()
    df[col] = encoders[col].fit_transform(df[col])



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




#model 3: for fertilisers'
y_predictor_fert=df['Best Fertilizer']
x_train,x_test,y_train,y_test=train_test_split(x,y_predictor_fert,test_size=0.2,random_state=42)
fert_model=RandomForestClassifier(n_estimators=100,random_state=42)
fert_model.fit(x_train,y_train)
y_fert_new=fert_model.predict(x_test)
print(f"Best Fertilizer Accuracy: {accuracy_score(y_test,y_fert_new)*100:.2f}%")





#main function to predict the values
def predict(state, district, soil, crop):
    state_enc = encoders['State'].transform([state])[0]
    district_enc = encoders['District'].transform([district])[0]
    soil_enc = encoders['Soil'].transform([soil])[0]
    crop_enc = encoders['Crop'].transform([crop])[0]
    arr1 = np.array([[state_enc, district_enc, crop_enc, soil_enc]])  
    arr1 = pd.DataFrame(arr1, columns=['State', 'District', 'Crop', 'Soil']) 

    irrigation_method = irr_model.predict(arr1)[0]
    best_crop = crop_model.predict(arr1)[0]
    best_fert=fert_model.predict(arr1)[0]

    #reverting encoded numbers to names
    irrigation_method = encoders['Irrigation Method'].inverse_transform([irrigation_method])[0]
    best_crop = encoders['Best Next Crop'].inverse_transform([best_crop])[0]
    best_fert=encoders['Best Fertilizer'].inverse_transform([best_fert])[0]

    return irrigation_method, best_crop,best_fert



state = l1[0]
district = l1[1]
soil = l1[2]
crop = l1[3]
irrigation, best_crop, best_fert = predict(state, district, soil, crop)
print(f"Recommended Irrigation Method: {irrigation}")
print(f"Best Crop to Grow after {l1[3]} is: {best_crop}")
print(f"Best Fertilizer to use is: {best_fert}")