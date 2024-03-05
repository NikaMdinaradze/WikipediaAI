import argparse
import socket
import time

parser = argparse.ArgumentParser(description="Check if port is open")
parser.add_argument("--service-name", required=True)
parser.add_argument("--ip", required=True)
parser.add_argument("--port", required=True)

args = parser.parse_args()

# Get arguments
SERVICE_NAME = str(args.service_name)
IP = str(args.ip)
PORT = int(args.port)

# Infinite loop
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((IP, PORT))
    if result == 0:
        print(f"Port is open! Bye! Service:{SERVICE_NAME} Ip:{IP} Port:{PORT}")
        break
    else:
        print(
            f"Port is not open! I'll check it soon! Service:{SERVICE_NAME} Ip:{IP} Port:{PORT}"
        )
        time.sleep(3)
