import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import datetime

# 1. Simulate Network & System Logs
def generate_synthetic_logs():
    data = {
        'timestamp': [datetime.datetime.now() for _ in range(100)],
        'login_attempts': np.random.randint(1, 5, 100).tolist(),
        'data_transfer_mb': np.random.uniform(10, 500, 100).tolist(),
        'remote_connections': np.random.randint(1, 10, 100).tolist()
    }
    
    # Injecting Anomalies (Simulated Attacks)
    data['login_attempts'][15] = 45          # Brute Force Scenario
    data['data_transfer_mb'][72] = 8500      # Data Exfiltration Scenario
    data['remote_connections'][33] = 95      # Unusual Remote Access
    
    return pd.DataFrame(data)

# 2. AI Engine for Anomaly Detection
def detect_threats(df):
    # Using Isolation Forest for unsupervised outlier detection
    model = IsolationForest(contamination=0.05, random_state=42)
    features = df[['login_attempts', 'data_transfer_mb', 'remote_connections']]
    
    df['anomaly_score'] = model.fit_predict(features)
    
    # -1 represents an anomaly detected by the model
    detected_threats = df[df['anomaly_score'] == -1]
    return detected_threats

# 3. Execution & Reporting
if __name__ == "__main__":
    print("--- Starting AI-Cloud-Sentinel Forensic Analysis ---")
    
    logs_df = generate_synthetic_logs()
    threats = detect_threats(logs_df)
    
    print(f"[*] Analysis Complete.")
    print(f"[*] Total Events Scanned: {len(logs_df)}")
    print(f"[!] Critical Anomalies Detected: {len(threats)}")
    
    if not threats.empty:
        print("\n--- Detailed Threat Report ---")
        print(threats[['timestamp', 'login_attempts', 'data_transfer_mb', 'remote_connections']])
