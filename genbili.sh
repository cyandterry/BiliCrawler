#!/bin/bash
clear

rm items.json
rm result.xls

scrapy crawl bili -o items.json -t json

./jsonConverter.py

read -p "Crawling is done! Result is store at result.xls. Press [Enter] key to Finish..."
