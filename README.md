# coin

## Installation Instructions
Install prerequisites
```
sudo apt install python3-pip python3-tk
pip3 install setuptools numpy matplotlib
```

### GDAX API
```
git clone https://github.com/danpaquin/gdax-python.git
cd gdax
python3 setup.py install
```
Install pull request #197 for some performance increases to the realtime order book.
This step will likely be removed in later versions if the the pull request is merged into gdax-master.
```
git pull origin pull/197/head
python3 setup.py install
```
### Bittrex API
```
pip3 install python-bittrex
```
### Twitter Scraper
```
pip3 install twitterscraper
```
