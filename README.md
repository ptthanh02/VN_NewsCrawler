## VN_NewsCrawler

A crawler for Vietnamese news on [VietNamNet](https://vietnamnet.vn/), crawling title and content of news articles for each category.

<hr>

### Installation

Requires Python 3.8 or higher.

- Clone this repository: 
```bash
$ git clone https://github.com/ptthanh02/VN_NewsCrawler.git
```

- Navigate to the project directory:
```bash
$ cd VN_NewsCrawler
```

- Install the required packages:
```bash
$ pip install -r requirements.txt
```
<hr>

### Configuration
Modifying your crawler configuration file `config.py` to customize your crawling progress.

```python
categories = ['thoi-su', 'kinh-doanh', 'van-hoa', 'giao-duc', 'the-gioi'] # currently support 5 categories
number_of_articles = 10  # for each category
```


<hr>

### Usage
- Run the crawler:
```bash
$ python crawler.py
```
