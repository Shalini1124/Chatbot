import requests
from bs4 import BeautifulSoup

def fetch_documentation(url, query):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return f"Failed to retrieve documentation. Status Code: {response.status_code}"

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')

        for para in paragraphs:
            if query.lower() in para.text.lower():
                return para.text

        return "No relevant information found."
    
    except Exception as e:
        return f"Error occurred: {str(e)}"
