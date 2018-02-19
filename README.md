# Steam Data Crawler

CSCE 470 Team project - A crawler program to retrieve essential information from Steam.com

## Authors

* **Juan Duran** - *Contributor* - [Juan's Github](https://github.com/hueytlatoani)
* **Anh Nguyen** - *Contributor* - [Anh's Github](https://github.com/harryluffy)
* **Han Hong** - *Contributor* - [Hong's Github](https://github.com/hongsolos)


## Background

This project's goal is to build a data crawler program to retrieve data from Steam website. These data will be kept in our form of a database, and will be used by another program to build a search engine. 

## Installation Instructions

What things you need to install the software and how to install them


The crawler is stored in Steam Crawler folder
Step 1: Download crawler directory into your system, and cd into this folder.
Step 2: Setup python 3.6 environment: 
```
virtualenv -p python3.6 env
env/bin/activate
```
Step 3: Install listed package requirements
```
pip install -r requirements.txt
```
Step 4: Create a folder named 'output' <- this folder will contain the crawled data
Step 5: Crawl the data using this command. All crawled will be retrieved in real time and stored in products_all.ij with the format listed in steam/spider/product_spirder.py
```
scrapy crawl products -o output/products_all.jl --logfile=output/products_all.log --loglevel=INFO -s JOBDIR=output/products_all_job -s HTTPCACHE_ENABLED=False
```

## Timeline

* 02/05/2018 - Project Initiated
* 02/18/2018 - Project Proposal Submitted
* 02/18/2018 - Data Crawler Completed - Data Retrieved

## Built With

* [Python 3.6](https://www.python.org/) - Python Development and Environment

## Acknowledgments

* Big thanks to [ANDRE PERUNICIC](https://github.com/prncc/steam-scraper) for making the crawler available for reference. 
* Scrapy Tool
* Steam


