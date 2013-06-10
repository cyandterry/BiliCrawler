#!/bin/bash
echo $1
echo $2

date1=$(date +"%s")

clear

if [ -f items.json ];
then
    rm items.json
    echo "items.json exists and will be removed first"
fi

if [ -z "$1" ]
then
    scrapy crawl bili -o items.json -t json
else
    if [ -z "$2" ]
    then
        scrapy crawl bili -o items.json -t json -a end=$1
    else
        scrapy crawl bili -o items.json -t json -a begin=$1 -a end=$2
    fi
fi

./injectDB.py

date2=$(date +"%s")
diff=$(($date2-$date1))

read -p "Crawling is done! Total time used is $(($diff / 60)) minutes and $(($diff % 60)) seconds. Press [Enter] key to Finish..."
