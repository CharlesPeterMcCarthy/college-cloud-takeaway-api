import boto3
import datetime
import random
import json
import helpers.common as help

def handler(event, context):
    """ Lambda function entrance """
    data = json.loads(event['body'])
    items = data['items']
    order_total = data['orderTotal']

    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table("Takeaway_Orders")
    except:
        return help.create_response(403, {'error': 'Can\'t connect to DB!'})

    res = table.put_item(Item={
        'orderID': str("%032x" % random.getrandbits(128)),      # Generate random ID
        'orderTime': datetime.datetime.now().isoformat(),
        'items': items,
        'orderTotal': order_total
    })

    return help.create_response(200, res)
