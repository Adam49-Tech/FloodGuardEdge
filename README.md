FloodGuardEdge 🌊
AI-powered Flood Risk Monitoring and Visualization Tool
---
❗ Problem Statement
Flooding is a recurring and devastating issue in Nigeria, especially in states like Benue, Kogi, Lagos, Abuja, Niger, Borno, Anambra and Bayelsa. It disrupts lives, destroys property, and poses significant environmental and economic challenges.
There is an urgent need for predictive, accessible, and real-time flood risk monitoring tools to aid early warning and disaster preparedness.
---
🚀 Overview
FloodGuardEdge is a prototype that predicts and visualizes flood risk areas using satellite rainfall and elevation data for key Nigerian states.
This project was developed for the 3MTT Knowledge Showcase to demonstrate how machine learning and geospatial analysis can be combined to address real-world environmental challenges.
---
🌍 Key Features
📌 Focus Areas: Benue, Abuja, Niger, Lagos, Kogi, Bayelsa, Anambra, Borno
☔ Data Used: CHIRPS Rainfall, SRTM Elevation (Google Earth Engine)
🧠 Model: Logistic Regression for flood risk prediction
🔄 Interactivity: Adjustable rainfall thresholds and region selection
🎯 Output: Dynamic flood risk maps with user-controlled parameters
---
💾 Project Structure
FloodGuardEdge/
│
├── pre-processing/
│   ├── prepare_data.py
│   ├── generate_training_data.py
│   ├── train_model.py
│   ├── predict_flood_risk.py
│   └── visualize_prediction.py
│
├── processed/
│   ├── flood_risk_map.tif
│   ├── flood_map_visual.png
│   └── training_data.csv
│
├── data/
│   ├── CHIRPS_AprilOct2024.tif
│   └── SRTM_Elevation_Reduced.tif
│
├── app.py
└── README.md
---
🛠️ How to Run the App
1. Clone the Repository
git clone https://github.com/Adam49-Tech/FloodGuardEdge.git
2. Install Required Libraries
pip install -r requirements.txt
3. Run the App
streamlit run app.py
---
📊 Data Sources
CHIRPS Rainfall: Climate Hazards Group
SRTM Elevation: NASA / Google Earth Engine
---
🌟 About the Developer
Built as part of the 3MTT Knowledge Showcase 2025 to demonstrate real-world AI solutions for environmental management in Nigeria.
