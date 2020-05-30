import json
import boto3


def create_dynamo_entry(username, lastname, first_name, account_type, age):
    dynamodb_resource = boto3.resource("dynamodb")
    table = dynamodb_resource.Table('testUserTable')
    item = {
        'username': username,
        'lastname': lastname,
        'first_name': first_name,
        'account_type': account_type,
        'age': age
    }
    table.put_item(
        Item=item
    )


def lambda_handler(event, context):
    print("Creating DynamoDB entry...")
    try:
        create_dynamo_entry(
            event['username'],
            event['lastname'],
            event['first_name'],
            event['account_type'],
            event['age']
        )
    except Exception as err:
        print("Something wrong with the user creation: {}".format(err))
    print("Entry created for user: {}".format(event['username']))
    return {
        'statusCode': 201,
        'message': 'Entry created for user: {}'.format(event['username'])
    }
