import os
from tqdm import tqdm
from urllib.parse import urljoin
from crawlers.crawler import *
from config import categories, number_of_articles

def main(categories, number_of_articles, progress_bar):
    result_directory = "result"
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)

    for category in categories:
        category_directory = os.path.join(result_directory, category)
        if not os.path.exists(category_directory):
            os.makedirs(category_directory)

        url = urljoin(base_url, category)
        links = get_article_links(base_url, url, number_of_articles)
        articles = get_article_content(links)

        for count, article in enumerate(articles, start=1):
            article_file_name = f"{count}.txt"
            article_file_path = os.path.join(category_directory, article_file_name)
            while os.path.exists(article_file_path):
                count += 1
                article_file_name = f"{count}.txt"
                article_file_path = os.path.join(category_directory, article_file_name)

            with open(article_file_path, 'w', encoding='utf-8') as f:
                f.write(f"{article['title']}\n{article['content']}")
            progress_bar.update(1)
            progress_bar.refresh()
            
if __name__ == "__main__":
    print(f"Crawling {number_of_all_articles} articles from {len(categories)} categories...")
    progress_bar = tqdm(total=number_of_all_articles, desc='Articles', unit=' articles',dynamic_ncols=True)
    main(categories, number_of_articles, progress_bar)
    progress_bar.close()
    print("Done!")