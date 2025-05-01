import requests
from bs4 import BeautifulSoup

def extract_full_text(url):
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            content_div = soup.find('div', class_='article-text container-padding')

            if content_div:
                return content_div.get_text(separator='\n')
            else:
                return "Content couldn' find!!"
            

""" url = "https://www.hukukihaber.net/yargitay-1-ceza-dairesinin-20246057-e-2025420-k-sayili-karari"

text = extract_full_text(url)

if __name__ == "__main__":
     print(text)
"""
