import requests

# Define query parameters for the API request
arguments = {
    "amount": 10,
    "type": "boolean",
    "category":18
}
# Send GET request to the API with specified parameters
response = requests.get(url="https://opentdb.com/api.php", params=arguments)

# Raise an exception if the request returned an unsuccessful status code
response.raise_for_status()

# Parse the JSON response and extract the list of questions
# Raise an exception if the request returned an unsuccessful status code
question_data = response.json()["results"]

