import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error

path = r"sources\irrigation_data_with_next_crop_v2.csv"
try:
    df = pd.read_csv(path)
except FileNotFoundError:
    print("File not Found")

columns = ["State", "District", "Soil Type", "Crop Type", "Irrigation Method", "Next Crop", "Suitable Fertilizer", "Suitable Pesticide"]
for col in columns:
    if col not in df.columns:
        print(f"Column {col} is not in the dataset")
encoders = {}
for col in columns:
    encoders[col] = LabelEncoder()
    df[col] = encoders[col].fit_transform(df[col])

x = df[['State', 'District', 'Soil Type', 'Crop Type']]

# First model: Predict the best irrigation method
y_predictor_irr = df['Irrigation Method']
x_train, x_test, y_train, y_test = train_test_split(x, y_predictor_irr, test_size=0.2, random_state=42)
irr_model = RandomForestClassifier(n_estimators=100, random_state=42)
irr_model.fit(x_train, y_train)
y_irr_new = irr_model.predict(x_test)
print(f"Irrigation Accuracy: {accuracy_score(y_test, y_irr_new) * 100:.2f}%")

# Model 2: Predict the next best crop after the current crop is harvested
y_predictor_crop = df['Next Crop']
x_train, x_test, y_train, y_test = train_test_split(x, y_predictor_crop, test_size=0.2, random_state=42)
crop_model = RandomForestClassifier(n_estimators=100, random_state=42)
crop_model.fit(x_train, y_train)
y_crop_new = crop_model.predict(x_test)
print(f"Best Next Crop Accuracy: {accuracy_score(y_test, y_crop_new) * 100:.2f}%")

# Model 3: Predict the best fertilizer
y_predictor_fert = df['Suitable Fertilizer']
x_train, x_test, y_train, y_test = train_test_split(x, y_predictor_fert, test_size=0.2, random_state=42)
fert_model = RandomForestClassifier(n_estimators=100, random_state=42)
fert_model.fit(x_train, y_train)
y_fert_new = fert_model.predict(x_test)
print(f"Best Fertilizer Accuracy: {accuracy_score(y_test, y_fert_new) * 100:.2f}%")

# Model 4: Predict the best pesticide
y_predictor_pest = df['Suitable Pesticide']
x_train, x_test, y_train, y_test = train_test_split(x, y_predictor_pest, test_size=0.2, random_state=42)
pest_model = RandomForestClassifier(n_estimators=100, random_state=42)
pest_model.fit(x_train, y_train)
y_pest_new = pest_model.predict(x_test)
print(f"Best Pesticide Accuracy: {accuracy_score(y_test, y_pest_new) * 100:.2f}%")

# Model 5: Predict crop yield
y_predictor_yield = df['Crop_Yield_ton']
x_train, x_test, y_train, y_test = train_test_split(x, y_predictor_yield, test_size=0.2, random_state=42)
yield_model = RandomForestRegressor(n_estimators=100, random_state=42)
yield_model.fit(x_train, y_train)
y_yield_new = yield_model.predict(x_test)

# Main function to predict the values
def predict(state, district, soil, crop):
    state_enc = encoders['State'].transform([state])[0]
    district_enc = encoders['District'].transform([district])[0]
    soil_enc = encoders['Soil Type'].transform([soil])[0]
    crop_enc = encoders['Crop Type'].transform([crop])[0]
    arr1 = np.array([[state_enc, district_enc, soil_enc, crop_enc]])
    arr1 = pd.DataFrame(arr1, columns=['State', 'District', 'Soil Type', 'Crop Type'])

    irrigation_method = irr_model.predict(arr1)[0]
    best_crop = crop_model.predict(arr1)[0]
    best_fert = fert_model.predict(arr1)[0]
    best_pest = pest_model.predict(arr1)[0]
    yield_est = yield_model.predict(arr1)[0]

    # Reverting encoded numbers to names
    irrigation_method = encoders['Irrigation Method'].inverse_transform([irrigation_method])[0]
    best_crop = encoders['Next Crop'].inverse_transform([best_crop])[0]
    best_fert = encoders['Suitable Fertilizer'].inverse_transform([best_fert])[0]
    best_pest = encoders['Suitable Pesticide'].inverse_transform([best_pest])[0]
    print(f"Estimated Yield: {yield_est:.2f} Tons")
    print(f"Recommended Irrigation Method: {irrigation_method}")
    print(f"Best Crop to Grow after {crop} is: {best_crop}")
    print(f"Best Fertilizer to use is: {best_fert}")
    print(f"Best Pesticide to use is: {best_pest}")
    return irrigation_method, best_crop, best_fert, yield_est


