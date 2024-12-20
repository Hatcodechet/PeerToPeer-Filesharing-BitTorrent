BitTorrent System

Overview

This project implements a simplified BitTorrent system that mimics the behavior of trackers, peers, and file sharing using UDP sockets. It supports functionalities like peer registration, file seeding, downloading, scraping, and tracker management.

Features

Tracker

Maintains a list of files and their associated peers.

Handles requests from peers, including registration, file seeding, downloading, and scraping.

Tracks alive peers and removes inactive ones.

Stores metadata in JSON files for persistence.

Peer

Allows peers to register and interact with the tracker.

Supports file seeding, downloading, and chunk-based file sharing.

Enables parallel downloading of file chunks from multiple peers.

Provides functionality to scrape file information like the number of seeders and leechers.

Configurations

Configurable constants (e.g., chunk size, tracker address, buffer size) defined in the configs module.

Installation

Clone the repository:

git clone https://github.com/Hatcodechet/PeerToPeer-Filesharing-BitTorrent.git
cd PeerToPeer-Filesharing-BitTorrent

Install dependencies:

Python 3.x is required.

Install any additional Python modules if necessary.

Configure the system:

Modify configs.py to set constants such as tracker address and buffer size.

Usage

Running the Tracker

Start the tracker:

python tracker.py

Use commands to manage the tracker:

list: List all files tracked by the system.

fileinfo <filename>: Show details about a specific file, including its seeders and leechers.

peerinfo: Show details about all peers in the system.

Running a Peer

Start a peer by specifying a unique peer ID:

python peer.py <peer_id>

Use commands to manage the peer:

send <filename>: Seed a file to the network.

download <filename>: Download a file from the network.

scrape <filename>: Scrape file information like the number of seeders and leechers.

exit: Exit the torrent network.

Project Structure

PeerToPeer-Filesharing-BitTorrent/
├── tracker.py       # Implements the tracker functionality
├── peer.py          # Implements the peer functionality
├── configs.py       # Configuration file
├── utils.py         # Utility functions
├── HTTPCommunication.py # Implements message encoding/decoding
├── request.py       # Data packet structure
├── logs/            # Logs for tracker and peers
└── db/              # JSON database files for tracker persistence

Key Classes and Functions

Tracker

Tracker: Handles peer registration, file tracking, and requests from peers.

listen: Listens for incoming UDP messages.

check_peer_periodically: Periodically checks the status of peers.

save_db_as_json: Saves the tracker database to JSON files.

Peer

Peer: Manages file sharing, seeding, downloading, and interacting with the tracker.

set_send_mode: Enables file seeding mode.

set_download_mode: Downloads a file by splitting it into chunks and reassembling.

inform_tracker_periodically: Sends periodic updates to the tracker.

Configuration Details

Tracker Address: Configured in configs.py as TRACKER_ADDR.

Buffer Size: Configured in configs.py as BUFFER_SIZE.

Chunk Size: Configured in configs.py as CHUNK_PIECES_SIZE.

Logs and Debugging

Logs are saved in the logs/ directory.

Debugging information is printed to the console for both tracker and peer processes.

Future Enhancements

Add support for file encryption during transmission.

Implement NAT traversal for peers behind firewalls.

Extend the system for multi-file torrenting.

License

This project is licensed under the MIT License. Feel free to use and modify as needed.

