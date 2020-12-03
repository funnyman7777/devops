import requests
import json

match = "db.t3"
url = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/20201128151805/ap-south-1/index.json"

response = requests.get(url)
result = json.loads(response.text)

for nn in result["terms"]["OnDemand"]:
    # print(nn)
    for ff in result["terms"]["OnDemand"][nn]:
        # print(ff)
        for mm in result["terms"]["OnDemand"][nn][ff]["priceDimensions"]:
            print("")
            for ww in result["terms"]["OnDemand"][nn][ff]["priceDimensions"][mm]["description"]:
                # print(result["terms"]["OnDemand"][nn][ff]["priceDimensions"][mm]["pricePerUnit"]["USD"])
               # if match in ww:
                    print(ww, end = '')
               # else:
                   # print("not found")
