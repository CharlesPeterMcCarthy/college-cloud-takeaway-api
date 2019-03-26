import boto3
import helpers.common as help

def handler(event, context):
    """ Lambda function entrance """
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table("Takeaway_Orders")
    except:
        return help.create_response(403, {'error': 'Can\'t connect to DB!'})

    orders = table.scan() # Get all rows from table

    return help.create_response(200, orders['Items'])
