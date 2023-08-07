import json


def hello(event, context):
    """
    This function returns a simple hello world message.

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

    message = "Hola mundo - bienvenidos al curso de serverless framework en aws"
    return {
        "statusCode": 200,
        "body": json.dumps({"message": message}),
    }
