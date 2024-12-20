import os
from peer import Peer
from tracker import Tracker
import argparse
import random
import json
from threading import Thread
from configs import CFG, Config
config = Config.from_json(CFG)



def generate_random_port():
    return random.randint(1024, 65535)
def main_menu():
    while True:
        print("""
=========== BitTorrent System ===========
1. Tracker Management
2. Peer Management
3. Exit
=========================================
Choose an option: """, end="")
        choice = input()
        if choice == "1":
            tracker_menu()
        elif choice == "2":
            peer_menu()
        elif choice == "3":
            print("Exiting the BitTorrent system. Goodbye!")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

def tracker_menu():
    tracker = Tracker()
    while True:
        print("""
=========== Tracker Management ==========
1. Start tracker
    ------------------ In tracker: ------------------
     Show all sended files:    torrent -mode list
    -------------------------------------------------

2. Exit
=========================================
Choose an option: """, end="")
        choice = input().strip()
        if choice == "1":
            print("Starting Tracker...")
            tracker.run()
        elif choice == "2":
            print("Exiting Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def peer_menu():
    try:
        # Step 1: Initialize Peer
        print("Enter your Peer ID: ", end="")
        peer_id = int(input().strip())
        peer = Peer(peer_id, generate_random_port(), generate_random_port())

        # Step 2: Register Peer in the Torrent Network
        peer.enter_torrent()

        # Step 3: Start periodic tracker notification
        timer_thread = Thread(target=peer.inform_tracker_periodically, args=(config.constants.PEER_TIME_INTERVAL,))
        timer_thread.setDaemon(True)
        timer_thread.start()

        while True:
            print(f"""
============ Peer Management ============
Peer ID: {peer.peer_id}
Files owned: {peer.files}
=========================================
1. List Owned Files
2. Download File
3. Send File
4. SCRAPE File Info
5. Back to Main Menu
=========================================
Choose an option: """, end="")
            choice = input().strip()

            # Step 4: Handle user options
            if choice == "1":
                # List all owned files
                print(f"Owned files: {peer.files}")

            elif choice == "2":
                # Download file
                print("Enter filename to download: ", end="")
                filename = input().strip()
                if filename:
                    try:
                        thread = Thread(target=peer.set_download_mode, args=(filename,))
                        thread.setDaemon(True)
                        thread.start()
                    except Exception as e:
                        print(f"Error during download: {e}")
                else:
                    print("Filename cannot be empty.")

            elif choice == "3":
                # Send file
                print("Enter filename to send: ", end="")
                filename = input().strip()
                if filename:
                    try:
                        peer.set_send_mode(filename)
                    except Exception as e:
                        print(f"Error during send: {e}")
                else:
                    print("Filename cannot be empty.")

            elif choice == "4":
                # SCRAPE file info
                print("Enter filename to scrape: ", end="")
                filename = input().strip()
                if filename:
                    try:
                        thread = Thread(target=peer.set_scrape_mode, args=(filename,))
                        thread.setDaemon(True)
                        thread.start()
                    except Exception as e:
                        print(f"Error during scrape: {e}")
                else:
                    print("Filename cannot be empty.")
            elif choice == "5":
                # Return to main menu
                print("Returning to Main Menu...")
                break

            else:
                print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid Peer ID. Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main_menu()
