# Peer-to-Peer Network: Seed and Peer Nodes

This project implements a basic peer-to-peer (P2P) network using seed nodes and peer nodes.

## Overview

In a P2P network, nodes communicate directly with each other without relying on a central server. This implementation features two types of nodes:

### Seed Node

Seed nodes serve as initial points of contact in the network. They maintain a list of active peers and help new nodes discover existing connections, allowing them to join the network seamlessly.

### Peer Node

Peer nodes are the main participants in the network. They retrieve and store data while maintaining connections with other peers.

## How Seed and Peer Nodes Interact

1. When a peer node starts, it connects to at least `n/2 + 1` seed nodes to obtain a list of active peers in the network.
2. Once connected, the peer node establishes communication with these peers and begins exchanging data.

## Message Exchange Between Nodes

Seed nodes and peer nodes communicate using specific message types:

- **Get Peer List** – A peer requests the list of active nodes from a seed node.
- **Peer List** – The seed node responds with the list of active peers in the network.

Peer nodes also communicate with each other using these messages:

- **Peer Request** – A peer node requests a connection with another peer.
- **Peer Reply** – The receiving peer node accepts the connection request.
- **Liveliness** – A peer checks if another peer is still active.
- **Liveliness Reply** – A peer responds to confirm its presence.
- **getData** – A peer requests data from another peer.
- **Message** – A peer sends data to another peer.
- **Death** – A peer informs the seed node that it is disconnecting from the network.

## Viewing Active Peers and Messages

To check network activity, run the following commands in the peer node terminal:

- Press `1` to display the active peer connections.
- Press `2` to view the list of messages exchanged between peer nodes.

## Running the Program

1. Install dependencies:
   ```sh
   pip install colorlog
   ```
2. Start a seed node:
   ```sh
   python3 seed.py
   ```
3. Launch peer nodes:
   ```sh
   python3 peer.py
   ```
4. To clean up logs and output files after stopping nodes:
   ```sh
   python3 logRemover.py
   ```

## Stopping a Peer Node

To stop a peer node, either:

- Press `Ctrl + C`
- Enter any input other than `1` or `2`

## Log Files and Output

- Logs are stored in the `logs` directory under `seeds/` (for seed nodes) and `peers/` (for peer nodes).
- Logs contain details about messages sent/received, liveliness checks, and connection closures.
- Different log levels are highlighted in various colours for easy identification.

## Contributors

- [Dishit Sharma (B22CS082)](https://github.com/sharmajii7)
- [Kiran S (B22CS100)](https://github.com/Kiran-velan)
