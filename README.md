# XSS Battery Arsenal

A curated, advanced list of XSS payloads and automated fuzzing scripts for penetration testing, red teaming, and bug bounty research.  
**For educational, research, and authorized security testing only.**

---

## 📋 What’s Inside

- `XSS_PAYLOADS.txt` — Universal, filter-bypassing XSS payload arsenal  
- `xss_blast.py` — Python3 script to automate XSS testing against target URLs  
- (Optional) Add more scripts, payloads, or Burp/XSStrike configs

---

## 🚀 Usage

1. **Clone or Download Repo**
    - Download ZIP or use `git clone`

2. **Edit Your Target in the Script**
    - Edit `xss_blast.py` to match your target URL/parameter

3. **Run Your XSS Scan**
    ```bash
    python3 xss_blast.py
    ```

4. **Review Results**
    - Hits are printed to terminal; tune/fuzz as needed for deeper coverage

---

## 🧨 Example

```python
import requests

with open("XSS_PAYLOADS.txt") as f:
    payloads = [line.strip() for line in f if line.strip() and not line.startswith("#")]

for payload in payloads:
    r = requests.get("https://www.vulnweb.com/search", params={"search": payload}, verify=False)
    if payload in r.text:
        print(f"[+] Payload reflected: {payload}")

