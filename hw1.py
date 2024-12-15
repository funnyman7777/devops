import requests
import json
import re

url = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/20201128151805/ap-south-1/index.json"

response = requests.get(url)
result = json.loads(response.text)

for nn in result["terms"]["OnDemand"]:
    
    for ff in result["terms"]["OnDemand"][nn]:

        for mm in result["terms"]["OnDemand"][nn][ff]["priceDimensions"]:

            for ww in result["terms"]["OnDemand"][nn][ff]["priceDimensions"][mm]["description"].split('\n'):

                if re.search("db.t3", ww.strip()):
                    print("")
                    print(ww.strip()[13:])
                    print("PRICE ", result["terms"]["OnDemand"][nn][ff]["priceDimensions"][mm]["pricePerUnit"]["USD"].split('\n'), "USD")
