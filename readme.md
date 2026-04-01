#🛡️ Cyber Security AI SOC Dashboard (Real-Time Threat Detection)

A real-time AI-powered Cyber Security Monitoring System built using Machine Learning, Deep Learning (ANN), and Streamlit, designed like a SOC (Security Operations Center) dashboard similar to Splunk.

🚀 Features
🔍 Real-Time Monitoring
Live packet-by-packet analysis
Continuous traffic simulation from dataset
Instant attack detection
🤖 AI + ML Detection
Machine Learning model (Best classifier)
Artificial Neural Network (ANN) validation
Dual-model comparison (ML vs ANN)
🚨 Threat Detection
DDoS Attack Detection
Intrusion Detection
Malware Detection
Normal Traffic Classification
📊 SOC Dashboard Features
🟢 Real-time metrics (Total / Attack / Safe packets)
📈 Live prediction trend chart
📉 Attack timeline heatmap
🌐 IP tracking system per packet
📊 Final security analytics table
🧠 ML vs ANN accuracy comparison
🎨 UI Features
Dark Splunk-like SOC theme
Color-coded alerts:
🟢 Safe Traffic
🔴 Attack Detected
Clean chat-style packet logs
Responsive Streamlit layout
🔊 Alerts System
🔊 Voice alerts using pyttsx3
🔔 Beep sound for attack detection
AI-generated explanations for predictions
📄 Reporting System
📊 Final security report dashboard
🌐 IP tracking table
📉 Attack heatmap visualization
📄 Export report as PDF file
🛠️ Tech Stack
Python 🐍
Streamlit 🎨
Scikit-learn 🤖
TensorFlow / Keras 🧠
Pandas 📊
Matplotlib 📈
Seaborn 📉
FPDF 📄
Pyttsx3 🔊
📁 Project Structure
Cyber-Security-SOC-Dashboard/
│
├── app.py
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   ├── ann_model.h5
│   └── encoders.pkl
│
├── data/
│   └── cybersecurity_attacks.csv
│
├── security_report.pdf (generated)
└── README.md
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/cyber-security-soc-dashboard.git
cd cyber-security-soc-dashboard
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
streamlit run app.py
📦 Requirements

Create requirements.txt:

streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
tensorflow
pyttsx3
fpdf
📊 Output Preview
Real-time packet monitoring dashboard
Attack detection alerts
AI explanation panel
Heatmap of attack timeline
Final SOC report with IP tracking
🧠 Model Information
ML Model: Trained classifier (Random Forest / SVM / etc.)
Deep Learning: ANN model using TensorFlow/Keras
Features used:
Protocol
Packet Length
Packet Type
Traffic Type
Severity Level
Anomaly Score
📌 Future Improvements
🌍 Real-time packet sniffing (Wireshark integration)
🗺️ IP Geolocation map
🔐 Login-based SOC dashboard
📡 Live WebSocket streaming
☁️ Cloud deployment (AWS / Azure)
👨‍💻 Author

Darshan Kurali
Cyber Security & AI Project