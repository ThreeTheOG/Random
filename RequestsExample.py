import requests

# The URL to the API
url = 'https://randomfox.ca/floof'

# Make the API call using the GET method
response = requests.get(url)

# Convert to a more usable format (JSON(Json conversion is built into the Requests module))
fox = response.json()

# Print the response (In JSON)
print(fox)

# Parse the JSON to get the direct Image Link
print(fox['image'])
