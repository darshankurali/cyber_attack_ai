# 🛡️ Cyber Security AI SOC Dashboard  
### Real-Time Threat Detection using AI & Machine Learning

---

## 📌 Introduction
The **Cyber Security AI SOC Dashboard** is a real-time monitoring system designed to simulate a **Security Operations Center (SOC)** environment. It uses Machine Learning (ML) and Deep Learning (ANN) to detect cyber threats such as DDoS attacks, intrusions, and malware.

Built with Streamlit, this dashboard provides live packet monitoring, intelligent detection, and visual analytics similar to enterprise SOC tools.

---

## 🚀 Features

### 🔍 Real-Time Monitoring
- Live packet-by-packet analysis  
- Continuous traffic simulation  
- Instant attack detection  

### 🤖 AI + ML Detection
- Machine Learning classifier  
- Artificial Neural Network (ANN) validation  
- Dual-model comparison (ML vs ANN)  

### 🚨 Threat Detection
- DDoS Attack Detection  
- Intrusion Detection  
- Malware Detection  
- Normal Traffic Classification  

---

## 📊 SOC Dashboard Features
- 🟢 Real-time metrics (Total / Attack / Safe packets)  
- 📈 Live prediction trend chart  
- 📉 Attack timeline heatmap  
- 🌐 IP tracking system per packet  
- 📊 Final analytics table  
- 🧠 ML vs ANN accuracy comparison  

---

## 🎨 UI Features
- Dark Splunk-like theme  
- Color-coded alerts:
  - 🟢 Safe Traffic  
  - 🔴 Attack Detected  
- Chat-style packet logs  
- Responsive Streamlit layout  

---

## 🔊 Alerts System
- Voice alerts using pyttsx3  
- Beep sound for attack detection  
- AI-generated explanations for predictions  

---

## 📄 Reporting System
- Final SOC report dashboard  
- IP tracking table  
- Attack heatmap visualization  
- Export report as PDF  

---

## 🛠️ Tech Stack
- Python  
- Streamlit  
- Scikit-learn  
- TensorFlow / Keras  
- Pandas  
- Matplotlib  
- Seaborn  
- FPDF  
- Pyttsx3  

---

## 📁 Project Structure
```
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
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/darshankurali/cyber_attack_ai.git
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application
```bash
streamlit run app.py
```

---

## 📦 Requirements
Create a `requirements.txt` file:

```
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
tensorflow
pyttsx3
fpdf
```

---

## 📊 Output Preview
- Real-time packet monitoring dashboard  
- Attack detection alerts  
- AI explanation panel  
- Heatmap of attack timeline  
- Final SOC report with IP tracking  

---

## 🧠 Model Information
- ML Model: Trained classifier (Random Forest / SVM / etc.)  
- Deep Learning: ANN using TensorFlow/Keras  

### Features Used:
- Protocol  
- Packet Length  
- Packet Type  
- Traffic Type  
- Severity Level  
- Anomaly Score  

---

## 📌 Future Improvements
- 🌍 Real-time packet sniffing (Wireshark integration)  
- 🗺️ IP Geolocation map  
- 🔐 Login-based dashboard  
- 📡 Live WebSocket streaming  
- ☁️ Cloud deployment (AWS / Azure)  

---

## 👨‍💻 Author
**Darshan Kurali**  
Cyber Security & AI Project

---

## 📄 License
This project is licensed under the MIT License.
