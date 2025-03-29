from email import encoders
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtCore import Qt
import folium
import os
from geopy.geocoders import Nominatim
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import time
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error




class SecondPage(QWidget):
    def __init__(self):

        font_path1 = r"sources\KronaOne-Regular.ttf"
        font_id1 = QFontDatabase.addApplicationFont(font_path1)
        font_family1 = QFontDatabase.applicationFontFamilies(font_id1)[0] if font_id1 != -1 else "Arial"

        font_path2 = r"sources\InriaSans-Bold.ttf"
        font_id2 = QFontDatabase.addApplicationFont(font_path2)
        font_family2 = QFontDatabase.applicationFontFamilies(font_id2)[0] if font_id2 != -1 else "Arial"

        super().__init__()
        self.setWindowTitle("Indigrow Dashboard") 
        self.setGeometry(210, 100, 1500, 1000)
        self.setStyleSheet("background-color: white;")
        
        # Page title label
        self.label1 = QLabel("indigrow", self)
        self.label1.setFont(QFont(font_family1, 25))
        self.label1.move(30, 20)
        self.label1.setStyleSheet("color: black;")
        self.label1.adjustSize()

        # Image beside title
        self.image_label = QLabel(self)
        pixmap = QPixmap(r"sources\Vector.svg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.image_label.resize(50, 50)
        self.image_label.move(320, 20)

        # **Input Fields**
        self.text_state = QLineEdit(self)
        self.text_state.setPlaceholderText("State")
        self.text_state.setFont(QFont(font_family2, 12))
        self.text_state.setStyleSheet("padding: 10px; border: 1px solid grey; border-radius: 15px;")
        self.text_state.adjustSize()
        self.text_state.setGeometry(30, 100, 300, 50)

        self.text_district = QLineEdit(self)
        self.text_district.setPlaceholderText("District")
        self.text_district.setFont(QFont(font_family2, 12))
        self.text_district.adjustSize()
        self.text_district.setStyleSheet("padding: 10px; border: 1px solid grey; border-radius: 15px;")
        self.text_district.setGeometry(340, 100, 300, 50)

        self.text_soil = QLineEdit(self)
        self.text_soil.setPlaceholderText("Enter Soil Type")
        self.text_soil.setFont(QFont(font_family2, 12))
        self.text_soil.adjustSize()
        self.text_soil.setStyleSheet("padding: 10px; border: 1px solid grey; border-radius: 15px;")
        self.text_soil.setGeometry(650, 100, 300, 50)

        self.text_crop = QLineEdit(self)
        self.text_crop.setPlaceholderText("Enter Crop Type")
        self.text_crop.adjustSize()
        self.text_crop.setFont(QFont(font_family2, 12))
        self.text_crop.setStyleSheet("padding: 10px; border: 1px solid grey; border-radius: 15px;")
        self.text_crop.setGeometry(960, 100, 300, 50)

        # **Buttons**
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setFont(QFont(font_family2, 12, QFont.Bold))
        self.submit_button.setStyleSheet("background-color: black; color: white; padding: 10px; border-radius: 20px;")
        self.submit_button.setGeometry(30, 170, 130, 50)
        self.submit_button.clicked.connect(self.process_input)

        self.close_button = QPushButton("Close", self)
        self.close_button.setFont(QFont(font_family2, 15, QFont.Bold))
        self.close_button.setStyleSheet("background-color: black; color: white; padding: 5px; border-radius: 20px;")
        self.close_button.setGeometry(1330, 920, 130, 50)
        self.close_button.clicked.connect(self.close)

        self.label3 = QLabel("weather", self)
        self.label3.setFont(QFont(font_family2, 15))
        self.label3.move(30, 260)
        self.label3.setStyleSheet("color: black;")
        self.label3.adjustSize()

        #from file.py import weather
        weather= "Sunny"
        self.label4 = QLabel(weather, self)
        self.label4.setFont(QFont(font_family2, 15))
        self.label4.move(30,310)
        self.label4.setStyleSheet("border: 1px solid grey; padding: 5px; border-radius: 20px;")
        self.label4.adjustSize()

        self.label5 = QLabel("irrigation", self)
        self.label5.setFont(QFont(font_family2, 15))
        self.label5.move(300, 260)
        self.label5.setStyleSheet("color: black;")
        self.label5.adjustSize()

        #from file.py import irrigation
        irrigation= "Drip Irrigation"
        self.label6 = QLabel(irrigation, self)
        self.label6.setFont(QFont(font_family2, 15))
        self.label6.move(300,310)
        self.label6.setStyleSheet("border: 1px solid grey; padding: 5px; border-radius: 20px;")
        self.label6.adjustSize()

        self.label7 = QLabel("best crop", self)
        self.label7.setFont(QFont(font_family2, 15))
        self.label7.move(600, 260)
        self.label7.setStyleSheet("color: black;")
        self.label7.adjustSize()

        #from file.py import bestcrop
        bestcrop= "rice"
        self.label8 = QLabel(bestcrop, self)
        self.label8.setFont(QFont(font_family2, 15))
        self.label8.move(600,310)
        self.label8.setStyleSheet("border: 1px solid grey; padding: 5px; border-radius: 20px;")
        self.label8.adjustSize()

        self.label9 = QLabel("best fertilizer", self)
        self.label9.setFont(QFont(font_family2, 15))
        self.label9.move(30, 400)
        self.label9.setStyleSheet("color: black;")
        self.label9.adjustSize()

        #from file.py import bestfertilizer
        bestfertilizer= "npk"
        self.label10 = QLabel(bestfertilizer, self)
        self.label10.setFont(QFont(font_family2, 15))
        self.label10.move(30,450)
        self.label10.setStyleSheet("border: 1px solid grey; padding: 5px; border-radius: 20px;")
        self.label10.adjustSize()

        self.label11 = QLabel("estimated yield", self)
        self.label11.setFont(QFont(font_family2, 15))
        self.label11.move(300, 400)
        self.label11.setStyleSheet("color: black;")
        self.label11.adjustSize()

        #from file.py import estimatedyield
        estimatedyield= "1000 kg"
        self.label12 = QLabel(estimatedyield, self)
        self.label12.setFont(QFont(font_family2, 15))
        self.label12.move(300,450)
        self.label12.setStyleSheet("border: 1px solid grey; padding: 5px; border-radius: 20px;")
        self.label12.adjustSize()

    def process_input(self):
        state = self.text_state.text()
        district = self.text_district.text()
        soil = self.text_soil.text()
        crop = self.text_crop.text()

        self.user_data = [state, district, soil, crop]
        print("User Data:", self.user_data)

        # Show notification
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Data Submitted Successfully!")
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
    from sklearn.metrics import accuracy_score, mean_absolute_error
    def backend():
        path = r"sources\irrigation_data_with_next_crop_v2.csv"
        try:
            df=pd.read_csv(path)
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


        #first model : it will predict the best irrigation method
        y_predictor_irr=df['Irrigation Method']
        x_train,x_test,y_train,y_test=train_test_split(x,y_predictor_irr,test_size=0.2,random_state=42)
        #for training and tsteing
        irr_model= RandomForestClassifier(n_estimators=100, random_state=42)
        irr_model.fit(x_train,y_train)
        y_irr_new=irr_model.predict(x_test)
        print(f"Irrigation Accuracy: {accuracy_score(y_test,y_irr_new)*100:.2f}%")




        #model 2: this predicts the next best crop after the current crop is harvested

        y_predictor_crop=df['Next Crop']
        x_train,x_test,y_train,y_test=train_test_split(x,y_predictor_crop,test_size=0.2,random_state=42)
        crop_model=RandomForestClassifier(n_estimators=100,random_state=42)
        crop_model.fit(x_train,y_train)
        y_crop_new=crop_model.predict(x_test)
        print(f"Best Next Crop Accuracy: {accuracy_score(y_test,y_crop_new)*100:.2f}%")




        #model 3: for fertilizers
        y_predictor_fert=df['Suitable Fertilizer']
        x_train,x_test,y_train,y_test=train_test_split(x,y_predictor_fert,test_size=0.2,random_state=42)
        fert_model=RandomForestClassifier(n_estimators=100,random_state=42)
        fert_model.fit(x_train,y_train)
        y_fert_new=fert_model.predict(x_test)
        print(f"Best Fertilizer Accuracy: {accuracy_score(y_test,y_fert_new)*100:.2f}%")


        #model 4: for petscides
        y_predictor_pest=df['Suitable Pesticide']
        x_train,x_test,y_train,y_test=train_test_split(x,y_predictor_pest,test_size=0.2,random_state=42)
        pest_model=RandomForestClassifier(n_estimators=100,random_state=42)
        pest_model.fit(x_train,y_train)
        y_pest_new=pest_model.predict(x_test)
        print(f"Best Pesticide Accuracy: {accuracy_score(y_test,y_pest_new)*100:.2f}%")


        #model 5: yields
        y_predictor_yield = df['Crop_Yield_ton']
        x_train, x_test, y_train, y_test = train_test_split(x, y_predictor_yield, test_size=0.2, random_state=42)
        yield_model = RandomForestRegressor(n_estimators=100, random_state=42)
        yield_model.fit(x_train, y_train)
        y_yield_new = yield_model.predict(x_test)


    #main function to predict the values
        def predict(state, district, soil, crop):
            state_enc = encoders['State'].transform([state])[0]
            district_enc = encoders['District'].transform([district])[0]
            soil_enc = encoders['Soil Type'].transform([soil])[0]
            crop_enc = encoders['Crop Type'].transform([crop])[0]
            arr1 = np.array([[state_enc, district_enc, soil_enc, crop_enc]])  
            arr1 = pd.DataFrame(arr1, columns=['State', 'District', 'Soil Type', 'Crop Type']) 

            irrigation_method = irr_model.predict(arr1)[0]
            best_crop = crop_model.predict(arr1)[0]
            best_fert=fert_model.predict(arr1)[0]
            best_pest=pest_model.predict(arr1)[0]
            yield_est=yield_model.predict(arr1)[0]

            #reverting encoded numbers to names
            irrigation_method = encoders['Irrigation Method'].inverse_transform([irrigation_method])[0]
            best_crop = encoders['Next Crop'].inverse_transform([best_crop])[0]
            best_fert=encoders['Suitable Fertilizer'].inverse_transform([best_fert])[0]
            best_pest=encoders['Suitable Pesticide'].inverse_transform([best_pest])[0]

            print(f"Estimated Yield: {yield_est:.2f} Tons")

            print(f"Recommended Irrigation Method: {irrigation_method}")
            print(f"Best Crop to Grow after {user_data[3]} is: {best_crop}")
            print(f"Best Fertilizer to use is: {best_fert}")
            print(f"Best Pesticide to use is: {best_pest}")
            return irrigation_method, best_crop,best_fert,best_pest,yield_est

        state =self.user_data[0]
        district =self.user_data[1]
        soil =self.user_data[2]
        crop =self.user_data[3]
        predict(state, district, soil, crop)









class FirstPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Indigrow")
        self.setGeometry(210, 100, 1500, 1000)

        # Custom fonts
        font_path1 = "C://Users//athar//Downloads//hackknights//sources//KronaOne-Regular.ttf"
        font_id1 = QFontDatabase.addApplicationFont(font_path1)
        font_family1 = QFontDatabase.applicationFontFamilies(font_id1)[0] if font_id1 != -1 else "Arial"

        font_path2 = "C://Users//athar//Downloads//hackknights//sources//InriaSans-Bold.ttf"
        font_id2 = QFontDatabase.addApplicationFont(font_path2)
        font_family2 = QFontDatabase.applicationFontFamilies(font_id2)[0] if font_id2 != -1 else "Arial"

        # "Indigrow" Label
        self.label1 = QLabel("indigrow", self)
        self.label1.setFont(QFont(font_family1, 80))
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet("color: black;")
        self.label1.adjustSize()

        # Image beside "Indigrow"
        self.image_label = QLabel(self)
        pixmap = QPixmap("C:/Users/athar/Downloads/hackknights/sources/Vector.svg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.image_label.resize(150, 150)

        # Tagline below "Indigrow"
        self.label2 = QLabel("planting solutions", self)
        self.label2.setFont(QFont(font_family2, 23))
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("color: black;")
        self.label2.move(748,395)  # Set position to (0, 0) to center it below the first label
        self.label2.adjustSize()

        # Button to open indigrow dashboard in a new window
        self.next_button = QPushButton("Dashboard", self)
        self.next_button.setStyleSheet("background-color: black; color: white; padding: 20px; border-radius: 20px;")
        self.next_button.setFont(QFont(font_family2, 15, QFont.Bold))
        self.next_button.clicked.connect(self.open_second_page)
        self.next_button.adjustSize()

        self.resizeEvent(None)

    def resizeEvent(self, event):
        label1_x = (self.width() - self.label1.width()) // 2 - 80
        label1_y = (self.height() - self.label1.height()) // 2
        self.label1.move(label1_x, label1_y)

        spacing = 20
        image_label_x = label1_x + self.label1.width() + spacing
        image_label_y = label1_y + (self.label1.height() - self.image_label.height()) // 2
        self.image_label.move(image_label_x, image_label_y)
        button_margin = 30
        self.next_button.move(self.width() - self.next_button.width() - button_margin, self.height() - self.next_button.height() - button_margin)

    def open_second_page(self):
        """Opens SecondPage in a separate window without closing FirstPage"""
        self.second_page = SecondPage()
        self.second_page.show()




        # Clears input fields after submission
        self.text_soil.clear()
        self.text_crop.clear()
        self.text_state.clear()
        self.text_district.clear()


app = QApplication(sys.argv)
window = FirstPage()
window.show()
sys.exit(app.exec_())
