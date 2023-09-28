import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import categories, number_of_articles
import os

base_url = 'https://git init.vn/'
number_of_all_articles = len(categories) * number_of_articles
file_name = f"{number_of_all_articles}baibao.txt"
categories_mapping = {
    'thoi-su': 'Thời Sự',
    'kinh-doanh': 'Kinh Doanh',
    'van-hoa': 'Văn Hóa',
    'giao-duc': 'Giáo Dục',
    'the-gioi': 'Thế Giới'
}

def get_article_links(base_url, url, max_articles):
    """
    Returns a list of article links from the given url.
    """
    links = []
    while len(links) < max_articles:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('div', class_='horizontalPost__main'):
            find_h3 = link.find_next('h3', class_='horizontalPost__main-title vnn-title title-bold')
            find_a = find_h3.find_next('a')
            article_link = urljoin(base_url, find_a['href'])
            links.append(article_link)
        page_list = soup.find('ul', class_='pagination__list')
        link_next_page = page_list.find_next('li', class_='pagination__list-item').find_next('a')
        if link_next_page is None:
            break
        url = urljoin(url, link_next_page.get('href'))
    return links[:max_articles]

def get_article_content(links):
    """
    Returns a list of article content from the given links.
    """
    articles = []
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        find_content = soup.find('div', class_='main-v1 bg-white')
        title = find_content.find('h1', class_='content-detail-title').get_text()
        content = find_content.find('div', class_='maincontent main-content')
        if content is None:
            content = find_content.find('div', class_='maincontent main-content content-full-image content-full-image-v1')
        if content:
            content_text = content.get_text()
        else:
            content_text = "Can't get content"
        article = {
            "title": title,
            "content": content_text
        }
        articles.append(article)
    return articles

def crawl_and_save_articles(categories, file_name, number_of_articles):
    result_directory = "result"
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)
    
    result_file_path = os.path.join(result_directory, file_name)
    with open(result_file_path, 'a', encoding='utf-8') as f:
        for category in categories:
            count = 1
            mapped_category = categories_mapping.get(category, category)
            f.write(f"------------------------ Thể loại: {mapped_category} --------------------------\n")
            url = urljoin(base_url, category)
            links = get_article_links(base_url, url, number_of_articles)
            articles = get_article_content(links)
            for article in articles:
                f.write(f"Bài báo thứ {count}: \n")
                f.write(f"Tiêu đề: {article['title']}\nNội dung: {article['content']}\n")
                f.write('--------------------------------------------------\n')
                count += 1