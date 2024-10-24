from flask import Flask, request, render_template, flash, redirect
import numpy as np
import pickle
import requests
import mysql.connector
import os

# importing model
model = pickle.load(open('model.pkl','rb'))
sc = pickle.load(open('standscaler.pkl','rb'))
ms = pickle.load(open('minmaxscaler.pkl','rb'))

# creating flask app
app = Flask(__name__)
app = Flask(__name__, template_folder="../templates",static_folder='../static')
app.secret_key = os.urandom(24)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="Bett",
        password="",
        database="crop_feedback"
    )
@app.route('/feedback', methods=['POST'])
def feedback():
    name = request.form['name']
    email = request.form['email']
    feedback_text = request.form['feedback']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO feedback (name, email, feedback_text) VALUES (%s, %s, %s)",
        (name, email, feedback_text)
    )
    conn.commit()
    conn.close()

    flash("Thank you for your feedback!", "success")
    return redirect('/')  # Redirect to home after successful submission


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    N = request.form['Nitrogen']
    P = request.form['Phosphorus']
    K = request.form['Potassium']
    temp = request.form['Temperature']
    humidity = request.form['Humidity']
    ph = request.form['Ph']
    rainfall = request.form['Rainfall']

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)
    prediction = model.predict(final_features)

    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    image_dict = {
        "Rice": "images/rice.jpg",
        "Maize": "images/maize.jpg",
        "Jute": "images/jute.jpg",
        "Cotton": "images/cotton.jpg",
        "Coconut": "images/coconut.jpg",
        "Papaya": "images/papaya.jpg",
        "Orange": "images/orange.jpg",
        "Apple": "images/apple.jpg",
        "Muskmelon": "images/muskmelon.jpg",
        "Watermelon": "images/watermelon.jpg",
        "Grapes": "images/grapes.jpg",
        "Mango": "images/mango.jpg",
        "Banana": "images/banana.jpg",
        "Pomegranate": "images/pomegranate.jpg",
        "Lentil": "images/lentil.jpg",
        "Blackgram": "images/blackgram.jpg",
        "Mungbean": "images/mungbean.jpg",
        "Mothbeans": "images/mothbeans.jpg",
        "Pigeonpeas": "images/pigeonpeas.jpeg",
        "Kidneybeans": "images/kidneybeans.jpg",
        "Chickpea": "images/chickpea.jpg",
        "Coffee": "images/coffee.jpg"
    }

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        image_file = image_dict[crop]  # Get the corresponding image file
        result = "{} is the best crop to be cultivated right there.".format(crop)
    else:
        result = "Sorry,I could not determine the best crop to be cultivated with the provided data."

    return render_template('index.html', result=result, image=image_file)
@app.route('/realtime_weather', methods=['POST'])
def realtime_weather():
    lat = request.form['lat']
    lon = request.form['lon']
    api_key = ''
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'

    response = requests.get(url)
    weather_data = response.json()

    if weather_data['cod'] == 200:  # Check if the request was successful
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']

        return render_template('index.html', weather_data={
            'temperature': temperature,
            'humidity': humidity,
            'description': description,
            'wind_speed': wind_speed
        }, result=None)  # Return to the same template with weather data
    else:
        return render_template('index.html', error="Failed to get weather data.", result=None)

if __name__ == "__main__":
    app.run(debug=True)
