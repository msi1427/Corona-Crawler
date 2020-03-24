# Corona Crawler
This is a solution to crawl news articles from https://www.theguardian.com/au about **coronavius**. <br/>
Headlines, Bylines, News Publishing times, News labels and Article Links are extracted from the target website and stored in a **CSV** file.
<br/>**Language :** Python 3
<br/>**Used Libraries :** Scrapy(to crawl), BeautifulSoup(to cleanse), Pydrive(to store)  

<br/><br/>**Command Lines to run spider:**
<br/> cd crawler
<br/> scrapy crawl quotes -o items.csv

<br/> We have to run the storing file independently to store them in hosted storage after generating CSV file.