
#!/bin/bash

DATE=$(date --utc "+%Y-%m-%d")
FOLD="aws-prices"
AWS="aws-prices/$DATE"_rds.csv""

[[ -d ~/$FOLD ]] && echo "$FOLD dir already exist" || mkdir ~/$FOLD
[[ -e ~/$AWS ]] && echo "~/$AWS already exist" || curl https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/20201128151805/ap-south-1/index.json |grep "db.t3"> ~/aws-prices/$DATE"_rds".csv
