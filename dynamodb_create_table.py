import boto3


dynamodb_resource = boto3.resource("dynamodb")

table = dynamodb_resource.create_table(
    TableName='testUserTable',
    
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'    # Partition Key
        },
        {
            'AttributeName': 'lastname',
            'KeyType': 'RANGE'      
        }
    ],
    
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'lastname',
            'AttributeType': 'S'
        }
    ],
    
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)


table.meta.client.get_waiter('table_exists').wait(TableName='testUserTable')

print(table.item_count)