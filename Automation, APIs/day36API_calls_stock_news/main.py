import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

parameters = {
"function":"TIME_SERIES_DAILY_ADJUSTED",
"symbol": "TSLA",
"apikey": "ABCDEF"

}
response = requests.get(url = "https://www.alphavantage.co/query", params = parameters)
data = response.json()
timed_data = data["Time Series (Daily)"]
lst_timed_data = [value for (key,value) in timed_data.items()]
yesterday_closing = float(lst_timed_data[0]['4. close'])
day_before_yesterday_closing =  float(lst_timed_data[1]['4. close'])

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
if abs(yesterday_closing - day_before_yesterday_closing)/day_before_yesterday_closing > 0.05:
    print("Get News")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
