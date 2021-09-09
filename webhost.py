import http.server
import socketserver

# Sets the Port for the website. By default(here) the website goes to localhost:8000
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print('Serving at port', PORT)
    httpd.serve_forever()

# Please note, I'm not very experienced with the "httpx" module. 
# To get this working, simply `pip install httpx`, and put a basic `index.html` file in the same directory(and run this, then go to localhost:YourPortHere). 
# If you need more help with this, documentation should do the trick.