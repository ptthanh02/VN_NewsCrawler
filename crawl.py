from tqdm import tqdm
import crawlers.crawler as crawler
from crawlers.crawler import file_name
from config import categories, number_of_articles

def main():
    progress_bar = tqdm(total=len(categories), desc='Progress', unit=' categories')
    
    for category in categories:
        progress_bar.set_description(f'Processing category: {category}')
        crawler.crawl_and_save_articles([category], file_name, number_of_articles)
        progress_bar.update(1)
    progress_bar.close()
    print("Done!")

if __name__ == "__main__":
    main()
