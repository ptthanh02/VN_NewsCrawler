# VN_NewsCrawler (2023)

[VietNamNet](https://vietnamnet.vn/) news crawler is a Python-based web scraping tool designed to extract articles from [VietNamNet](https://vietnamnet.vn/) and store them in an organized manner. This project is intended for educational purposes and demonstrates how to scrape news articles from a website, categorize them, and save the content to separate text files.

## Installation

Requires Python 3.8 or higher.

- Clone this repository: 
```bash
$ git clone https://github.com/ptthanh02/VN_NewsCrawler.git
```
- Navigate to the project directory:
```bash
$ cd VN_NewsCrawler
```
- Create and active virtual environment:
```bash
$ python -m venv venv
$ venv\Scripts\activate 
```
- Install the required packages:
```bash
$ pip install -r requirements.txt
```

## Configuration
Modifying your crawler configuration file `config.py` to customize your crawling progress.

```python
categories = ['thoi-su', 'kinh-doanh', 'van-hoa', 'giao-duc', 'the-gioi'] 
number_of_articles = 10  # Number of articles to crawl for each category
```
By default, the configuration will crawl 10 articles for each category listed in the `categories` variable, resulting in a total of 50 crawled articles. You can adjust `number_of_articles` to crawl more articles or modify the `categories` variable to crawl specific categories.

#### Supported categories:
| **Categories**  | **Categories's Names**        |
| ----------- | ----------- |
| 'thoi-su'   | Thời Sự     |
| 'kinh-doanh'| Kinh Doanh  |
| 'van-hoa'   | Văn Hóa     |
| 'giao-duc'  | Giáo Dục    |
| 'the-gioi'  | Thế Giới    |
| 'the-thao'  | Thể Thao    |
| giai-tri'   | Giải Trí    |
| 'doi-song'  | Đời Sống    |
| 'suc-khoe'  | Sức Khỏe    |

## Usage
- Run the crawler:
```bash
$ python crawl.py
```
## Results

The crawler will automatically create a `result` folder and store the crawled articles in the following directory structure:

![Result](result/result.png)

- The `result` folder contains subdirectories for each news category.
- Each category folder stores articles related to that specific category.
- Each article is saved as an individual `.txt` file within its respective category folder.
- Articles are named uniquely to avoid overwriting existing content.

This structure ensures that the scraped articles are neatly organized and easily accessible, making it simple to locate and utilize the extracted information. Check the `result` folder for the [full example.](https://github.com/ptthanh02/VN_NewsCrawler/blob/main/result/50baibao.txt)

## Completed Code Available

Now, you can run [the crawler](https://github.com/ptthanh02/VN_NewsCrawler/blob/main/completed_code/crawler_full.ipynb) with [Jupyter Notebook](https://jupyter.org/) available in the `completed_code` folder and customize the crawler to your liking.
