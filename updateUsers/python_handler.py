import json

import boto3


def update_users(event, context):
    """
    Updates a user in the DynamoDB table.

    Args:
        event (dict): The event that triggered the Lambda function.
        context (dict): The context of the Lambda function.

    Returns:
        dict: The response from the Lambda function.
    """

    userId = event["pathParameters"]["id"]
    body = json.loads(event["body"])

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    users_table = dynamodb.Table("usersTable")
    # params = {
    #     # "TableName": "usersTable",
    #     "Key": {"pk": userId},
    #     "UpdateExpression": "set #name = :name",
    #     "ExpressionAttributeNames": {"#name": "name"},
    #     "ExpressionAttributeValues": {":name": body["name"]},
    #     "ReturnValues": "ALL_NEW",
    # }

    response = users_table.update_item(
        Key={"pk": userId},
        UpdateExpression="set #name = :name",
        ExpressionAttributeNames={"#name": "name"},
        ExpressionAttributeValues={":name": body["name"]},
        ReturnValues="ALL_NEW",
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"user": response["Attributes"]}),
    }
