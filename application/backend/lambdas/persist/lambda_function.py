import json

def lambda_handler(event, context):
    for record in event['Records']:
        print('Record received in PersistBuyStocksInfo: ', record)
        stock_buy = json.loads(record['body'])
        stock_buy_info = json.loads(stock_buy['Message'])

        buy_date = stock_buy_info['buy_date']
        ticker = stock_buy_info['ticker']
        buy_price = stock_buy_info['buy_price']
        stop_price = stock_buy_info['stop_price']
        number_shares = stock_buy_info['number_shares']
        print(f'Trade received in second Lambda: {number_shares} shares of {ticker} bought on {buy_date} for ${buy_price} with stop ${stop_price}')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
