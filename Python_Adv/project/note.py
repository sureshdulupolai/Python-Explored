"""

Web Scraping
Python libraries (BeautifulSoup, Selenium) se aap websites se information nikal sakte ho (jaise Flipkart/Amazon ka price check karna).
Networking / Internet Protocols
Python se TCP/UDP sockets bana ke aap apna chat server, file transfer system, multiplayer game bana sakte ho.


"""

import requests
from bs4 import BeautifulSoup

# Step 1: Website ko request bhejna
url = "https://quotes.toscrape.com/"
response = requests.get(url)

# Step 2: HTML ko parse karna
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Quotes nikalna
quotes = soup.find_all("span", class_="text")

print("📌 First 5 Quotes:")
for i, quote in enumerate(quotes[:5], 1):
    print(f"{i}. {quote.text}")


import socket

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))   # localhost, port 12345
server.listen(1)

print("✅ Server started, waiting for connection...")

conn, addr = server.accept()
print("Connected with:", addr)

while True:
    msg = conn.recv(1024).decode()
    if not msg:
        break
    print("Client:", msg)
    reply = input("You: ")
    conn.send(reply.encode())

conn.close()


import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

while True:
    msg = input("You: ")
    client.send(msg.encode())
    reply = client.recv(1024).decode()
    print("Server:", reply)
