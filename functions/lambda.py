import boto3
import json

def lambda_handler( event, context ):
    favorites = []

    for roo in event:
        favorites.append( roo["name"] )

    favorites[len(favorites) - 1] = "and " + favorites[len(favorites) - 1]
    favorites = ', '.join( map( str, favorites ) ) 

    prompt = "Kangaroos I like include #. Tell me about each of them."
    prompt = prompt.replace( "#", favorites )

    client = boto3.client( service_name = "bedrock-runtime" )
    model_id = "anthropic.claude-3-5-haiku-20241022-v1:0"
    messages = [{"role": "user", "content": prompt}]

    # anthropic.claude-3-5-haiku-20241022-v1:0
    # anthropic.claude-3-5-sonnet-20241022-v2:0

    request = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "temperature": 1,
        "messages": messages
    }
    response = client.invoke_model( modelId = model_id, body = json.dumps( request ) )
    
    model_response = json.loads( response["body"].read() )

    response_text = model_response["content"][0]["text"]

    return {
        "favorites": event,
        "recommendations": json.loads( response_text )["recommendations"]
    }
