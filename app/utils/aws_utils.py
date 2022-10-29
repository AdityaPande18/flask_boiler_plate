import boto3
import json

def get_secret(secret_id, region, is_json: bool = False):
    client = boto3.client("secretsmanager", region_name=region)
    secret_ = client.get_secret_value(SecretId=secret_id)
    if is_json:
        return json.loads(secret_.get("SecretString"))
    else:
        return secret_.get("SecretString")