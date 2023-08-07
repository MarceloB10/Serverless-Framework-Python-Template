import json
import os

import boto3

# IS_OFFLINE = os.getenv("IS_OFFLINE", False)
# if IS_OFFLINE:
#     boto3.Session(
#         aws_access_key_id="<aws_access_key_id>",
#         aws_secret_access_key="<aws_secret_access_key>",
#     )
#     client = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")

# table = client.Table("usersTable")


def get_users(event, context):
    """
    This function retrieves a user from DynamoDB.

    Parameters
    ----------
    event: dict
        The event that triggered the function.
    context: dict
        The context in which the function is running.

    Returns
    -------
    dict
        The response body.
    """

    # userId = event["pathParameters"]["id"]
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    users_table = dynamodb.Table("usersTable")
    response = users_table.get_item(Key={"pk": event["pathParameters"]["id"]})

    return {
        "statusCode": 200,
        "body": json.dumps(response),
    }
