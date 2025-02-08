import requests
import time

# Replace with your Render service URLs
urls = [
    "https://blaze-python-compiler-31c2.onrender.com",
    "https://blaze-javascript-editor-jwvo.onrender.com",
    "https://blaze-php-compiler-2f37.onrender.com",
    "https://blaze-java-compiler-grhj.onrender.com",
    "https://blaze-cpp-compiler-plbj.onrender.com",
    "https://blaze-c-compiler-25x7.onrender.com",
    "https://blaze-ruby-compiler-odsb.onrender.com",
    "https://blaze-golang-compiler.onrender.com",
    "https://blaze-csharp-compiler-0hxc.onrender.com",
    "https://blaze-swift-compiler.onrender.com",
    "https://blaze-r-compiler.onrender.com"

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
