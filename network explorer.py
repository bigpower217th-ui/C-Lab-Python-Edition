import socket
import sys

# Target setup
target = "127.0.0.1"

print("------------------------------------------------------------")
print(" Scanning Target: " + target)
print(" Status: Scanning ports 1-1024...")
print("------------------------------------------------------------")

try:
    for port in range(1, 1025):
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set timeout to 0.3 for faster scan
        s.settimeout(0.3)
        
        # Try to connect
        result = s.connect_ex((target, port))
        
        if result == 0:
            print("[+] Port " + str(port) + ": OPEN 🛡️")
        
        s.close()

except KeyboardInterrupt:
    print("\n[!] Stopped by user.")
    sys.exit()
except:
    print("\n[!] Unexpected error occurred.")
    sys.exit()

print("------------------------------------------------------------")
print(" Scan Completed.")
print("------------------------------------------------------------")