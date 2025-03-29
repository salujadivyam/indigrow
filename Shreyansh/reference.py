
#model 4(Shresh's model)

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