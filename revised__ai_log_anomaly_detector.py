#AI-Based Anomaly Detection

#!/usr/bin/env python3
"""
ai_log_anomaly_detector.py
Detects anomalous IPs using Isolation Forest (unsupervised ML).
"""

import re
import pandas as pd
from collections import defaultdict
from sklearn.ensemble import IsolationForest

LOG_FILE = "access.log"

log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+).+?"[A-Z]+\s+(?P<url>.+?)\s+HTTP.*?"\s+(?P<status>\d{3})'
)

ip_data = defaultdict(lambda: {"requests": 0, "errors": 0, "unique_urls": set()})

with open(LOG_FILE, "r") as f:
    for line in f:
        match = log_pattern.search(line)
        if match:
            ip = match.group("ip")
            url = match.group("url")
            status = match.group("status")

            ip_data[ip]["requests"] += 1
            ip_data[ip]["unique_urls"].add(url)
            if status.startswith("4") or status.startswith("5"):
                ip_data[ip]["errors"] += 1


# Convert to DataFrame
df = pd.DataFrame([
    {"ip": ip,
     "requests": d["requests"],
     "errors": d["errors"],
     "unique_urls": len(d["unique_urls"])}
    for ip, d in ip_data.items()
])

if df.empty:
    print("\n⚠ No log data found to analyze.")
else:
    # Train Isolation Forest
    model = IsolationForest(contamination=0.2, random_state=42)
    df["anomaly"] = model.fit_predict(df[["requests", "errors", "unique_urls"]])
    df["status"] = df["anomaly"].map({1: "Normal", -1: "Suspicious"})

    print("\n🤖 AI-Based Log Anomaly Detection:\n")
    print(df[["ip", "requests", "errors", "unique_urls", "status"]]
          .sort_values(by="requests", ascending=False)
          .to_string(index=False))

    print("\n✔ AI Analysis Complete.")

