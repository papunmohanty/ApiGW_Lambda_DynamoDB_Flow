import boto3


dynamodb_resource = boto3.resource("dynamodb")
table = dynamodb_resource.Table('testUserTable')


first_item = {
    'username': 'rahulkumar',
    'lastname': 'Kumar',
    'first_name': 'Rahul',
    'account_type': 'standard_account',
    'age': 29
}


table.put_item(
    Item=first_item
)