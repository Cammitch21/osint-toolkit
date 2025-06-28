import requests

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
            if response.status_code == 200:
                found[site] = url
            else:
                found[site] = None
        except requests.RequestException:
            found[site] = None
    return found

if __name__ == "__main__":
    username = input("Enter Username to check: ").strip()
    results = check_username(username)

    print(f"\n Results found for '{username}':\n")
    for site, url in results.items():
        if url:
            print(f"{site}: {url}")
        else:
            print(f"{site}: Not Found")