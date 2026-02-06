import json
import boto3
client = boto3.client('sns')

def lambda_handler(event, context):
    print('Received event in BuyStocks function:', event)
    if 'body' in event and event['body'] is not None:
        body = event['body']
        parameters = body.split('&')
        for parameter in parameters:
            key, value = parameter.split('=')
            if key == 'date':
                buy_date = value
            elif key == 'ticker':
                ticker = value
            elif key == 'buyPrice':
                buy_price = value
            elif key == 'stopPrice':
                stop_price = value
            elif key == 'numShares':
                number_shares = value
    else:
        parameters = event
        buy_date = parameters['date']
        ticker = parameters['ticker']
        buy_price = parameters['buyPrice']
        stop_price = parameters['stopPrice']
        number_shares = parameters['numShares']

    message = f'Buy {number_shares} shares of {ticker} on {buy_date} at ${buy_price} with a stop of ${stop_price}'
    response = client.publish(
        TopicArn='arn:aws:sns:us-east-1:069233348309:Stocks',
        Message=json.dumps({
            "txn_type": 'buy',
            "buy_date": buy_date,
            "ticker": ticker,
            "buy_price": buy_price,
            "stop_price": stop_price,
            "number_shares": number_shares
        })
    )
    print(f'Response from SNS.publish was: {response}')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f'Trade received: {message}'
        }),
        "headers": {
            "Content-Type": "application/json",
        }
    }
