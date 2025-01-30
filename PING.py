import requests
import time

# Replace with your Render service URLs
urls = [
    "https://blaze-python-compiler-nmbe.onrender.com",
    "https://blaze-javascript-editor-v8r0.onrender.com",
    "https://blaze-php-compiler-2iwl.onrender.com",
    "https://blaze-java-compiler-hz4k.onrender.com",
    "https://blaze-cpp-compiler-iwgl.onrender.com",
    "https://blaze-c-compiler-pysc.onrender.com",
    "https://blaze-ruby-compiler-u64z.onrender.com"
]

while True:
    for url in urls:
        try:
            # Send a GET request
            response = requests.get(url)
            print(f"Pinged {url} - Status Code: {response.status_code}")
        except Exception as e:
            print(f"Failed to ping {url}: {e}")

    time.sleep(60)
