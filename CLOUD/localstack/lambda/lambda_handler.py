import boto3

def handler(event, context):
    s3 = boto3.client('s3', endpoint_url="http://localhost:4566") # Dentro do container
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print(f"Processando arquivo: {key} do bucket: {bucket}")
        
        # Exemplo: Lendo o conteúdo do arquivo
        obj = s3.get_object(Bucket=bucket, Key=key)
        conteudo = obj['Body'].read().decode('utf-8')
        print(f"Conteúdo lido: {conteudo}")

    return {"status": "processado"}