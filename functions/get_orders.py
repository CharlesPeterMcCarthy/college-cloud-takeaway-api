import json
import decimal
import boto3

def handler(event, context):
    """ Lambda function entrance """
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table("Takeaway_Orders")
    except:
        return create_response(403, {'error': 'Can\'t connect to DB!'})

    orders = table.scan() # Get all rows from table

    return create_response(200, orders['Items'])

def to_decimal(obj):
    """ Turn any decimal values into string to prevent breaking response """
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    raise TypeError

def create_response(code, data):
    """ Form JSON response """
    return {
        'statusCode': code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data, default=to_decimal)
    }
