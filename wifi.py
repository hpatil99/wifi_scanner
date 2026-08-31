# scan_wifi.py
# Scan nearby Wi-Fi networks

import subprocess

def scan_wifi():
    # Run Windows command to get available networks
    command = "netsh wlan show networks mode=bssid"
    output = subprocess.check_output(command, shell=True)
    decoded = output.decode(errors="ignore")

    # Parse and display the results
    networks = []
    current = {}

    for line in decoded.splitlines():
        line = line.strip()

        if line.startswith("SSID "):
            if current:
                networks.append(current)
            current = {}
            current["ssid"] = line.split(":", 1)[1].strip()

        elif "Signal" in line:
            current["signal"] = line.split(":", 1)[1].strip()

        elif "Channel" in line:
            current["channel"] = line.split(":", 1)[1].strip()

        elif "Authentication" in line:
            current["security"] = line.split(":", 1)[1].strip()

    if current:
        networks.append(current)

    return networks


if __name__ == "__main__":
    networks = scan_wifi()
    print(f"\n{len(networks)} Nearby Wi-Fi Networks:\n")

    for i, net in enumerate(networks, 1):
        print(f"{i}. {net.get('ssid', 'N/A')}")
        print(f"   Signal: {net.get('signal', 'N/A')}")
        print(f"   Security: {net.get('security', 'N/A')}")
        print(f"   Channel: {net.get('channel', 'N/A')}\n")