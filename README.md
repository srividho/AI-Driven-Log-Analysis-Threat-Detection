# AI-Driven Log Analysis & Threat Detection

## 📌 Overview
This project focuses on **detecting suspicious activity in web server logs** using:
- **Rule-Based Detection** (404 flood detection, bot vs human classification)
- **AI-Powered Anomaly Detection** (using Isolation Forest)

The goal is to create a **simple yet effective threat detection pipeline** that can be extended for real-world security monitoring or SIEM integration.

---

## 🎯 Objectives
- Detect **directory enumeration attempts** by counting 404 errors per IP.
- Classify **bot vs human traffic** using User-Agent & Referrer.
- Detect **anomalous IPs automatically** using machine learning.
- Present results in a clean, reproducible format.

---

## 🛠 Methodology

### Part A – Directory Enumeration Detection
- Parsed Apache/Nginx logs using regex.
- Counted 404 errors per IP.
- Flagged IPs with ≥10 errors as **suspicious**.

### Part B – Bot vs Human Detection
- Parsed User-Agent and Referrer from logs.
- Classified as **bot** if:
  - User-Agent contained keywords (`curl`, `wget`, `python-requests`, `bot`, `spider`)
  - OR Referrer was missing
- Else → **human traffic**

### Part C – AI-Based Anomaly Detection
- Extracted features per IP:
  - `requests`, `errors`, `unique_urls`
- Trained **Isolation Forest** to detect outliers.
- Flagged anomalous IPs as suspicious.

---

## 📊 Findings

| Part | Key Findings |
|------|--------------|
| **Directory Enumeration** | High 404 counts indicate brute-force directory scanning. |
| **Bot Detection** | User-Agent and Referrer analysis catch automated requests. |
| **AI Anomaly Detection** | Isolation Forest flags suspicious IPs without fixed thresholds, useful for unknown attack patterns. |

---

## 🖼️ Screenshots & Visuals
> Add your screenshots here:
- **404 Detection Output** (terminal)
- **Bot vs Human Classification Output**
- **AI Anomaly Detection Output**
- **Scatter Plot Visualization** (requests vs errors)

---

## 📌 Conclusion
This project shows that **AI + rule-based detection** provides a strong and scalable log monitoring solution:
- Rule-based → catches known threats like 404 floods & bots
- AI-based → catches unknown, abnormal behavior
- Combined → better coverage and early-warning capability

---

## 🚀 Future Scope
- Real-time log monitoring & alerting
- Integration with SIEM tools (Splunk, ELK)
- GeoIP lookup for attacker attribution
- Dashboard visualization for SOC teams

---

## 📂 Repository Structure
