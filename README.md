# AI-Powered Cloud Sentinel: Real-Time Log Forensics

An advanced AI-driven cybersecurity tool designed for real-time log analysis and threat hunting. This project utilizes Machine Learning to identify sophisticated attacks like Stealthy Brute Force and Data Exfiltration within system logs.

## 🚀 Features
* **AI Anomaly Detection:** Uses `Isolation Forest` to detect deviations from normal system behavior.
* **Multi-Vector Analysis:** Monitors login attempts, data transfer volume, and remote connection frequency.
* **Automated Forensic Reporting:** Identifies and flags suspicious activities with precise timestamps.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **ML Library:** Scikit-learn
* **Data Handling:** Pandas & NumPy

## 📂 Project Structure
* `sentinel_ai.py`: The core AI engine and log processing script.
* `.gitignore`: Configured for Python environments.
* `LICENSE`: MIT License.

## ⚙️ How It Works
The system ingests log data and applies unsupervised learning to score each event. Events with an `anomaly_score` of -1 are flagged as high-risk threats that require immediate investigation by a SOC Analyst.

---
*Developed as part of my Cybersecurity & AI Portfolio.*
