# Defense Against CI Intrusions

**Course:** CSCI 5743 – Cyber Infrastructure & Defense  
**Semester:** Fall 2025  
**Student:** Deeksha Reddy Patlolla  


---

##  Overview
This repository contains the complete submission for **Assignment 4: Defense against Critical Infrastructure (CI) Intrusions**.  
The assignment combines **conceptual cyber defense analysis** with **hands-on technical implementation**, covering firewall enforcement, machine-learning–based anomaly detection, and secure file exchange using hybrid cryptography.

##  Assignment Components

### **Part 1 – Conceptual Analysis**
- Real-world breach analysis (Capital One, Equifax, Target, SolarWinds, Colonial Pipeline)
- Mapping **MITRE ATT&CK → MITRE D3FEND**
- Mapping **NIST CSF 2.0 → NIST SP 800-53 Rev. 5**

### **Part 2 – Hands-On Labs**
1. **Host-Based Firewall (iptables)**
   - Stateful filtering
   - Attack surface minimization
   - Least privilege & fail-safe defaults

2. **Login Anomaly Detection with Machine Learning**
   - Decision Tree classifier
   - Metrics: Accuracy, Precision, Recall, F1-Score
   - Analysis of false positives vs false negatives

3. **Secure File Exchange (Hybrid Cryptography)**
   - AES-CTR for confidentiality
   - HMAC-SHA256 for integrity
   - RSA-OAEP for key protection
   - Tamper and wrong-key validation tests

---

##  Environment & Tools
- **OS:** Kali Linux (Attack & Defense VMs)
- **Python:** 3.11
- **Libraries:** pandas, scikit-learn, cryptography
- **Network Tools:** iptables, Wireshark, nmap

