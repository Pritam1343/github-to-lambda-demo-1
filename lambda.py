import json
import requests
import pandas as pd

def lambda_handler(event, context):
    print("Event: ", event)
    response=requests.get("https://www.google.com/")
    print(response.txt)

    d={'col1':[1,2,3],'col2':[4,5,6]}
    df=pd.DataFrame(data=d) 
    print(df)
    print("demo completed")