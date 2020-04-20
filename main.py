import requests
from bs4 import BeautifulSoup

url = "https://www.shipton-mill.com/queue"
exact_match = "Sorry, we don't have any delivery slots available at this time, please come back later."

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

sorry_messages = soup.body.find_all(text=exact_match)
if len(sorry_messages) == 0:
    # There is no sorry message! Alert me!
    print("SEND ALERT")
    exit(1) # Exit with an error
else:
    print("NO ALERT")
    exit(0) # Exit with no error code
