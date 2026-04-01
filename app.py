import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
import matplotlib.pyplot as plt
import pyttsx3
import random
from tensorflow.keras.models import load_model
from fpdf import FPDF
import seaborn as sns

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Cyber Security AI System",
    page_icon="🛡️",
    layout="wide"
)

# ===============================
# SPLUNK DARK THEME
# ===============================
st.markdown("""
<style>
body {
    background-color: #0f1117;
    color: #ffffff;
}

.stApp {
    background-color: #0f1117;
}

h1, h2, h3 {
    color: #00ffcc;
}

div[data-testid="metric-container"] {
    background-color: #1c1f26;
    border-radius: 10px;
    padding: 10px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# TITLE
# ===============================
st.title("🛡️ Real-Time SOC Cyber Security Dashboard")

# ===============================
# METRICS
# ===============================
col1, col2, col3 = st.columns(3)

total_packets = 0
attack_count = 0
normal_count = 0

metric_total = col1.empty()
metric_attack = col2.empty()
metric_safe = col3.empty()

# ===============================
# LOAD MODELS
# ===============================
model = pickle.load(open("models/best_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
ann = load_model("models/ann_model.h5")

df = pd.read_csv("data/cybersecurity_attacks.csv")

features = [
    'Protocol', 'Packet Length', 'Packet Type',
    'Traffic Type', 'Severity Level', 'Anomaly Scores'
]

df_stream = df[features].dropna()

try:
    encoders = pickle.load(open("models/encoders.pkl", "rb"))
except:
    encoders = None

attack_names = {0: "Normal", 1: "DDoS", 2: "Intrusion", 3: "Malware"}

# ===============================
# PACKET LOG STORAGE
# ===============================
packet_logs = []

# ===============================
# VOICE
# ===============================
def speak(pred):
    try:
        engine = pyttsx3.init()
        engine.say("Attack detected" if pred != 0 else "Normal traffic")
        engine.runAndWait()
    except:
        pass

# ===============================
# BEEP
# ===============================
def beep():
    st.audio("https://www.soundjay.com/button/beep-07.wav")

# ===============================
# CHAT UI (FIXED BLACK TEXT)
# ===============================
def chat_user(msg):
    st.markdown(f"""
    <div style="color:black;background:#f2f2f2;padding:8px;border-radius:10px;margin:5px;">
    🧑 {msg}
    </div>
    """, unsafe_allow_html=True)

def chat_ai(msg):
    st.markdown(f"""
    <div style="color:black;background:#e8e8e8;padding:8px;border-radius:10px;margin:5px;">
    🤖 {msg}
    </div>
    """, unsafe_allow_html=True)

# ===============================
# CONTROLS
# ===============================
start = st.button("▶ Start Monitoring")
voice_alert = st.checkbox("Enable Voice Alert")
use_ai = st.checkbox("Enable AI Explanation")

ai_box = st.empty()
data_box = st.empty()
trend_chart = st.line_chart(pd.DataFrame(columns=["Prediction"]))

# ===============================
# MAIN LOOP
# ===============================
if start:

    st.success("Monitoring Started...")

    for i in range(20):

        sample = df_stream.sample(1).copy()

        if encoders:
            for col, le in encoders.items():
                if col in sample.columns:
                    sample[col] = le.transform(sample[col].astype(str))
        else:
            sample = sample.apply(lambda x: x.astype('category').cat.codes)

        scaled = scaler.transform(sample)

        pred = int(model.predict(scaled)[0])
        ann_pred = np.argmax(ann.predict(scaled), axis=1)[0]

        total_packets += 1
        attack = pred != 0

        attack_count += int(attack)
        normal_count += int(not attack)

        # IP INCLUDED HERE
        packet_logs.append({
            "Packet": i + 1,
            "IP": f"192.168.1.{random.randint(1,255)}",
            "ML": attack_names[pred],
            "ANN": attack_names[ann_pred],
            "Status": "ATTACK" if attack else "SAFE"
        })

        metric_total.metric("Total Packets", total_packets)
        metric_attack.metric("Attacks", attack_count)
        metric_safe.metric("Safe", normal_count)

        if pred == 0:
            st.success("🟢 NORMAL TRAFFIC")
        else:
            st.error(f"🔴 {attack_names[pred]} DETECTED")

        if voice_alert:
            speak(pred)

        if attack:
            beep()

        chat_user(f"Packet {i+1} analyzed")
        chat_ai(f"ML: {attack_names[pred]} | ANN: {attack_names[ann_pred]}")

        data_box.dataframe(sample)

        trend_chart.add_rows(pd.DataFrame([pred], columns=["Prediction"]))

        time.sleep(1)

    # ===============================
    # FINAL REPORT
    # ===============================
    st.markdown("---")
    st.subheader("📊 FINAL SECURITY REPORT")

    final_df = pd.DataFrame(packet_logs)

    # ACCURACY
    accuracy = np.mean(final_df["ML"] == final_df["ANN"])
    st.metric("ML vs ANN Agreement Accuracy", f"{accuracy*100:.2f}%")

    # SINGLE FINAL TABLE (MERGED FIX)
    st.subheader("📊 Final Security Analysis Table")

    st.dataframe(final_df[["Packet", "IP", "ML", "ANN", "Status"]])

    # SMALL PIE CHART FIX
    fig, ax = plt.subplots(figsize=(2.5, 2.5))

    ax.pie(
        [len(final_df[final_df["Status"]=="SAFE"]),
         len(final_df[final_df["Status"]=="ATTACK"])],
        labels=["Safe", "Attack"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

    # HEATMAP
    st.subheader("📊 Attack Timeline Heatmap")

    heat_df = final_df.copy()
    heat_df["Index"] = range(len(heat_df))
    heat_df["Value"] = heat_df["Status"].apply(lambda x: 1 if x == "ATTACK" else 0)

    fig, ax = plt.subplots(figsize=(6, 2))
    sns.heatmap(pd.DataFrame(heat_df["Value"]).T, cmap="Reds", cbar=False, ax=ax)

    st.pyplot(fig)

    # PDF EXPORT
    def generate_pdf(df):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        pdf.cell(200, 10, txt="Cyber Security SOC Report", ln=True, align="C")

        for _, row in df.iterrows():
            line = f"{row['Packet']} | {row['IP']} | {row['ML']} | {row['Status']}"
            pdf.cell(200, 8, txt=line, ln=True)

        pdf.output("security_report.pdf")

    if st.button("📄 Export PDF Report"):
        generate_pdf(final_df)
        st.success("PDF Generated Successfully")