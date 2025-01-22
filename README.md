# Crop Recommendation System using Flask🌱

This project is a **Crop Recommendation System** built using **Flask**. It leverages machine learning to recommend the best crop to grow based on environmental conditions, helping farmers make data-driven decisions.

## Features ✨
- **Input Parameters**:  
  - Nitrogen (N)  
  - Phosphorus (P)  
  - Potassium (K)  
  - Temperature (°C)  
  - Humidity (%)  
  - pH  
  - Rainfall (mm)  
- **Prediction Output**: Recommends the most suitable crop.  
- **Crop Images**: Displays the predicted crop’s image from the `/static/images/` folder.
- **OpenWeather API Integration**: Retrieve weather data for precise recommendations and weather updates.

## Technologies Used 💻
- **Python** (Flask, scikit-learn)  
- **HTML5**, **CSS3** (Frontend)  
- **JavaScript** (for dynamic weather updates)  
- **OpenWeather API**

## Project Structure 📁
```
|-- app.py               # Flask application entry point  
|-- /static              # Static files (CSS, JS, images)  
|   |-- /images          # Crop images  
|-- /templates           # HTML templates  
|   |-- index.html       # Main interface  
|-- trial.pth            # Pre-trained ML model  
|-- requirements.txt     # Project dependencies  
```

## How to Run Locally 🛠️
1. **Clone the repository:**
   ```bash
   git clone https://github.com/KIPROTICHBETT53/crop-recommendation-system.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd crop-recommendation-system
   ```
3. **Create a conda environment and install dependencies:**
   ```bash
   conda create --name crop-env python=3.8
   conda activate crop-env
   pip install -r requirements.txt
   ```
4. **Run the Flask app,:**
   ```bash
   python app.py
   ```
5. **Access the application in your browser:**  
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Contact 📧
- **Email**: [ellybett53@gmail.com](mailto:ellybett53@gmail.com)  
- **LinkedIn**: [Elly Bett](https://www.linkedin.com/in/elly-bett-5b2535247)  
- **GitHub**: [KIPROTICHBETT53](https://github.com/KIPROTICHBETT53)
