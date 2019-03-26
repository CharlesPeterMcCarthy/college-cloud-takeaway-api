import json
import decimal

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
