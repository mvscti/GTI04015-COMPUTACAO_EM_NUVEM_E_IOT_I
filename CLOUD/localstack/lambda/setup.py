import boto3
import zipfile
import json

# Configuração para o LocalStack
LOCALSTACK_URL = "http://localhost:4566"

s3 = boto3.client(
    "s3", 
    endpoint_url=LOCALSTACK_URL,
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test")
lmb = boto3.client(
    "lambda", 
    endpoint_url=LOCALSTACK_URL,
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test")
iam = boto3.client(
    "iam",
    endpoint_url=LOCALSTACK_URL,
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test")

def run_setup():
    print("Iniciando infraestrutura local...")

    # 1. Criando o Bucket
    bucket_name = "meu-bucket-de-testes"
    s3.create_bucket(Bucket=bucket_name)

    # 2. Preparar o código da Lambda (Zip)
    with zipfile.ZipFile("lambda.zip", "w") as z:
        z.write("lambda_handler.py")

    # 3. Criar a Função Lambda
    with open("lambda.zip", "rb") as f:
        zip_content = f.read()

    lmb.create_function(
        FunctionName="ProcessadorS3",
        Runtime="python3.9",
        Role="arn:aws:iam::000000000000:role/ignore-me",
        Handler="lambda_handler.handler",
        Code={'ZipFile': zip_content}
    )

    # 4. Adicionando Permissão para o S3 invocar a Lambda
    lmb.add_permission(
        FunctionName="ProcessadorS3",
        StatementId="1",
        Action="lambda:InvokeFunction",
        Principal="s3.amazonaws.com"
    )

    # 5. Configurar o Gatilho (Trigger)
    s3.put_bucket_notification_configuration(
        Bucket=bucket_name,
        NotificationConfiguration={
            'LambdaFunctionConfigurations': [{
                'LambdaFunctionArn': f"arn:aws:lambda:us-east-1:000000000000:function:ProcessadorS3",
                'Events': ['s3:ObjectCreated:*']
            }]
        }
    )
    print("Tudo pronto! O S3 agora avisa a Lambda quando um arquivo chega.")

if __name__ == "__main__":
    run_setup()