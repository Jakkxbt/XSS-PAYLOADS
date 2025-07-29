import requests

TARGET_URL = "https://www.vulnweb.com/search"  # Default classic demo endpoint
PARAM_NAME = "search"  # Typical reflected XSS param

def main():
    with open("XSS_PAYLOADS.txt") as f:
        payloads = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    total = len(payloads)
    print(f"[+] Loaded {total} XSS payloads")

    for idx, payload in enumerate(payloads, 1):
        try:
            resp = requests.get(TARGET_URL, params={PARAM_NAME: payload}, timeout=10, verify=False)
            # You may want to refine matching, depending on target echo behavior:
            if payload in resp.text:
                print(f"[{idx}/{total}] [+] Payload reflected: {repr(payload)}")
            else:
                print(f"[{idx}/{total}] [-] Not reflected.")
        except Exception as e:
            print(f"[{idx}/{total}] [!] Error for payload: {repr(payload)} -- {e}")

if __name__ == "__main__":
    main()
