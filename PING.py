import requests
import time

# Updated Render service URLs
urls = [
    "https://blaze-cpp-compiler-zjrt.onrender.com",
    "https://blaze-c-compiler-h9gk.onrender.com",
    "https://blaze-php-compiler-273e.onrender.com",
    "https://blaze-typescript-compiler-y2mz.onrender.com",
    "https://blaze-rust-compiler-xqj0.onrender.com",
    "https://blaze-python-compiler-w2ta.onrender.com",
    "https://blaze-r-compiler-hq0l.onrender.com",
    "https://blaze-javascript-editor-z7fn.onrender.com",
    "https://blaze-java-compiler-3kza.onrender.com",
    "https://blaze-swift-compiler-1a3l.onrender.com",
    "https://blaze-golang-compiler-445c.onrender.com",
    "https://blaze-csharp-compiler-lxap.onrender.com",
    "https://blaze-ruby-compiler-diro.onrender.com"
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
