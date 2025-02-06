import requests
import time

# Replace with your Render service URLs
urls = [
    "https://blaze-python-compiler-5uv6.onrender.com",
    "https://blaze-javascript-editor-jwvo.onrender.com",
    "https://blaze-php-compiler-2f37.onrender.com",
    "https://blaze-java-compiler-usro.onrender.com",
    "https://blaze-cpp-compiler-plbj.onrender.com",
    "https://blaze-c-compiler-25x7.onrender.com",
    "https://blaze-ruby-compiler-ymot.onrender.com",
    "https://blaze-csharp-compiler-0hxc.onrender.com"
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
