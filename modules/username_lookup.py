import requests

# Add or remove sites here to customise the websites you want to search
sites = {
    "Github": "https://github.com/{}",
    "Linkedin": "https://www.linkedin.com/in/{}",
    "Instagram": "https://www.instagram.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
}

def check_username(username):
    found = {}

    for site, url_template in sites.items():
        url = url_template.format(username)
        try:
            response = requests.get(url, timeout = 2)
            # Status code 200 will add the url to the list
            if response.status_code == 200:
                found[site] = url
            # All other codes are disregarded and not added to the list
            else:
                found[site] = None
        except requests.RequestException:
            found[site] = None
    return found