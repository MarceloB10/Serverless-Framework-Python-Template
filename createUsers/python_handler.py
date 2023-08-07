import json
import uuid

import boto3


def create_users(event, context):
    # Generate a random ID for the user.
    id = uuid.uuid4()

    # Convert the UUID to a string.
    id_str = str(id)

    # Get the user body from the event.
    user_body = json.loads(event["body"])

    # Add the ID to the user body.
    user_body["pk"] = id_str

    # Create the DynamoDB client.
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

    # Put the user in DynamoDB.
    users_table = dynamodb.Table("usersTable")
    users_table.put_item(Item=user_body)

    # Return the user.
    return {"statusCode": 200, "body": json.dumps({"user": user_body})}
