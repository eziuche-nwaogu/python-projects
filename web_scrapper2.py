import requests
from bs4 import BeautifulSoup


def get_profile_image():
    web_site = input("Enter the URL of the website you wish to check: ")
    user_name = input("Enter the username of the user: ")
    html_tag = input("Enter the HTML tag that contains the profile image: ")
    attribute = input(
        "Enter the attribute of the HTML tag that contains the image URL: "
    )

    url = web_site + user_name
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    profile_image = soup.find(html_tag)[attribute]
    print(profile_image)


get_profile_image()
