import socket
import threading
import json
import sys
import time

# Global variables
active_peers = []
log_file = None

# Class to represent a connected peer
class PeerNode:
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address

    def __repr__(self):
        return f"{self.address[0]}:{self.address[1]}"

# Function to handle communication with a connected peer
def handle_peer(peer):
    global active_peers, log_file

    while True:
        try:
            message = peer.connection.recv(2048).decode()
            if not message:
                continue
        except:
            continue

        try:
            message = json.loads(message)
        except:
            print(f"Peer {peer.address[1]} sent invalid data: {message}")
            continue

        print(f"Peer {peer.address[1]}: {message}")

        if message.get("type") == "getData":
            current_peers = [str(p) for p in active_peers]
            active_peers.append(PeerNode(peer.connection, (message["ip"], message["port"])))
            peer.address = (message["ip"], message["port"])

            with open(log_file, "a") as log:
                print(f"Peer {peer.address[1]} registered: {peer.address}", file=log)

            response = {"type": "getData_reply", "Peers": current_peers}
            peer.connection.sendall(json.dumps(response).encode())

        elif message.get("type") == "Death":
            active_peers = [p for p in active_peers if p.address != (message["ip"], message["port"])]
            with open(log_file, "a") as log:
                print(f"Peer {peer.address[1]} disconnected", file=log)

# Function to handle incoming peer connections
def accept_connections(server_socket):
    global log_file

    while True:
        server_socket.listen()
        connection, address = server_socket.accept()
        new_peer = PeerNode(connection, address)

        with open(log_file, "a") as log:
            print(f"New peer connected: {address}", file=log)

        threading.Thread(target=handle_peer, args=(new_peer,)).start()

# Function to send a message to all peers except a given one
def broadcast_message(message, exclude_idx):
    global active_peers, log_file

    for i, peer in enumerate(active_peers):
        if i == exclude_idx:
            continue
        try:
            peer.connection.sendall(message.encode())
        except:
            with open(log_file, "a") as log:
                print(f"Peer {peer.address[1]} disconnected", file=log)
            active_peers.pop(i)

# Main function
def main(host, port, node_identifier):
    global log_file

    log_file = f"bin/servers/log_{node_identifier}.txt"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))

        with open(log_file, "w") as log:
            print(f"Server started at {host}:{port}", file=log)

        threading.Thread(target=accept_connections, args=(server,)).start()

        time.sleep(5)
        print(f"Server started at {host}:{port}")
        while True:
            time.sleep(15)
            print("Server is running...")

if __name__ == "__main__":
    main("127.0.0.1", int(sys.argv[1]), sys.argv[2])
