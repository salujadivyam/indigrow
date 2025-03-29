import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import numpy as np

def Load(fpath):    
    try:
        data=pd.read_csv(fpath)
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def preprocessdata(data):
    labelEncoders={}
    for column in ["State","Area","Soil Type","Crop"]:
        le=LabelEncoder()
        data[column]=le.fit_transform(data[column])
        labelEncoders[column]=le
        features=data[["State","Area","Soil Type","Crop"]]
        targets={"Temperature":data["Temperature('C)"],"Rainfall":data["Rainfall(mm)"],"Humidity":data["Humidity(%)"],"Wind Speed":data["Wind Speed(km/hr)"],"BEst irrigation time":data["Best Irrigation Time"],"Best Fertilizer":data["Best Fertilizer"],"Alternative Fertilizer":data:["Alternative Fertilizer"]}
        return features,targets,labelEncoders
    

def trainmodels(features,targets):
    models={}
    for target_name,targetvalues in targets.items():
        if target_name in ["Best Irrigation Time","Best Fertilizer","Alternative Fertilizer"]:
            le=LabelEncoder()
            target_values_encoded=le.fit_transform(targetvalues)
            model=RandomForestRegressor()
            model.fit(features,target_values_encoded)
            models[target_name]=(models,le)
        else:
            model=RandomForestRegressor()
            model.fit(features,targetvalues)
            models[target_name]=model
            return models