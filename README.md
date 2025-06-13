FloodGuardEdge – Predicting Urban Flood Risk Using Satellite Data 🌊
🚀 Project Overview
FloodGuardEdge is an interactive AI-powered flood risk prediction app that visualizes flood-prone areas across Nigeria using satellite-derived rainfall and elevation data. This tool is designed to support communities, planners, and emergency responders in flood risk assessment.
🌧️ Problem
Urban flooding in Nigeria frequently causes significant damage to lives, property, and infrastructure. Many areas lack localized, real-time flood prediction systems.
✅ Solution
FloodGuardEdge provides:
- Real-time flood risk mapping
- Rainfall and severity-based filtering
- State-level zooming and analysis
- Downloadable flood risk maps in CSV and PNG formats
🔧 Technology Stack
- Python
- Streamlit
- Google Earth Engine
- GeoPandas, Rasterio, Matplotlib
- GitHub and Streamlit Cloud
🎯 Key Features
- Interactive flood risk map with Nigeria’s boundary
- Rainfall threshold slider
- Flood severity filtering (Low, Medium, High)
- State filtering and zooming
- CSV and PNG download options
- Progress spinner for real-time feedback
📂 Project Structure
FloodGuardEdge/ ├── data/ ├── processed/ ├── shapefiles/ ├── pre-processing/ ├── streamlit_app.py ├── README.md └── requirements.txt
🔗 Demo
[Live Streamlit App](https://floodguardedgeai.streamlit.app)
🔗 GitHub
[GitHub Repository](https://github.com/Adam49-Tech/FloodGuardEdge)
🚀 Future Work
- Integration of real-time flood alerts via SMS or Email.
- Adding more predictive variables (drainage, land cover, soil type).
- Automated data updates from Google Earth Engine.
👤 Developed by Adam49-Tech
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
├── streamlit_app.py
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
