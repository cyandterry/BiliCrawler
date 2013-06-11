<h2>BiliCrawler</h2>

<p>This is a crawler for the site http://www.bilibili.tv.</p>

<p>The intention to build this app is to learn Scrapy and gather video informations from bilibili.tv.</p>

<p>BiliCrawler is build on <a href="http://scrapy.org/">Scrapy</a>. For installation and documentation about Scrapy, please click <a href="http://doc.scrapy.org/en/latest/intro/install.html">HERE</a>.</p>

<p><s>In order to generate Excel crawling result, you should install python excel package <a href="http://www.python-excel.org/">xlwt</a>. Please downloadand install it <a href="https://pypi.python.org/pypi/xlwt"> HERE</a>.</s></p>

<p>The latest version of BiliCrawler has switched from using excel as the output of result to use sqlite3 as result output. To install sqlite3, please use <code>sudo apt-get install sqlite3</code>. For other OS users, please see <a href="http://www.sqlite.org/download.html">HERE</a>. Type <code>import sqlite3</code> in your python shell to make sure you have the correct library in python. result will be stored in result.db. Use <code>sqlite3 result.db</code> to open the SQL and TABLE NAME is Bilibili.</p>

<p>Or if you want to view it in csv file, you can also generate csv file by typing: <br /><code>scrapy crawl bili -o result.csv -t csv</code></p>

<h3>Usage:</h3>

<p>Install all the required packages and run the script genbili.sh by typing:<br /><code>./genbili.sh</code></p>

<hr />

<p>这是一个针对哔哩哔哩的爬虫工具，主要目的是用于爬虫学习和对哔哩哔哩视频网的分析</p>
