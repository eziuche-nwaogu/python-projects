# This is an improvement on the original one. This takes the user input, modifies it and gets the profile image of the user
# This was tried on Windows. It has not been tried on other operating systems
import requests
from bs4 import BeautifulSoup

print("This app only works for github. It doesnt work for any other site for now")
github_user = input("Enter the username of the github user: ")
url = "https://github.com/" + github_user
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
profile_image = soup.find("img", {"alt": "Avatar"})["src"]
print(profile_image)
