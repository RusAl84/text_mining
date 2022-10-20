import requests
from bs4 import BeautifulSoup


def open_site(url):
    return requests.get(url).text


def scraping_page(url, pages):
    print(pages, ' страница')
    html = open_site(url)
    soup = BeautifulSoup(html, "html.parser")
    for card in soup.find_all('div', class_='quote'):
        description = card.find('span', class_='text').text
    author = card.find('small', class_='author').text
    about_author = card.find('a').get('href')
    tags = [tag.text for tag in card.find_all('a', class_='tag')]
    print({'description': description, 'author': author, 'about_author': about_author, "tags": tags})


if __name__ == "__main__":
    pages = 10
    for i in range(1, pages + 1):
        url = f'https://quotes.toscrape.com/page/{i}/'
        scraping_page(url, i)
