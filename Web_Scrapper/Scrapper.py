import requests
url = "https://gasprices.aaa.com"
page = requests.get(url)

def Verify_request(page):
    if page.status_code == 200:
        print("Successfully fetched the page!")
    else:
        print(f"Failed to retrieve data. Status code: {page.status_code}")
    
Verify_request(page)
