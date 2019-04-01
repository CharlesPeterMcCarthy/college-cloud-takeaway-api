import boto3
import json
import helpers.common as help

def handler(event, context):
    """ Lambda function entrance """
    data = json.loads(event['body'])
    product = data['product']

    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table("Takeaway_Products")
    except:
        return help.create_response(403, {'error': 'Can\'t connect to DB!'})

    res = table.put_item(Item=product)

    return help.create_response(200, res)
