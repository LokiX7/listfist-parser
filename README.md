# ListFist table parser 
____

A simple parser that will allow you to get tables with anime episodes from this wonderful site.

____

## How to use?

Import "parser" function from parser.py and pass arguments to it: 
1. url = page url with episodes table.
2. headers = your request headers dict {user-agent: ~, 'accept': ~}. 
   How to view HTTPS headers https://mkyong.com/computer-tips/how-to-view-http-headers-in-google-chrome/ 
3. file_name = name a json dict file where data will be stored 
4. path_to_save = json file save path. By default saves to the working directory. 

### or

Just run the app and pass url table page. The data file will be saved to the same directory

____

## Data structure: [{Number: (Episode number), Name: (Episode name), Date: (Release date)}, {}]

___

## Requirements:

The requirement is not strict so you can work with older versions, however I can not vouch for the functionality.

- beautifulsoup4=4.10.0
- requests=2.22.0
- python=3.8
