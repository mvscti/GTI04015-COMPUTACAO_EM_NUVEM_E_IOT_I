import boto3
import zipfile

endpoint = "http://localhost:4566"

s3 = boto3.client("s3", endpoint_url=endpoint,
    aws_access_key_id="test", aws_secret_access_key="test", region_name="us-east-1")

sqs = boto3.client("sqs", endpoint_url=endpoint,
    aws_access_key_id="test", aws_secret_access_key="test", region_name="us-east-1")

lambda_client = boto3.client("lambda", endpoint_url=endpoint,
    aws_access_key_id="test", aws_secret_access_key="test", region_name="us-east-1")



# Fila do SQS
queue_url = sqs.create_queue(QueueName="fila-imagens")["QueueUrl"]
queue_arn = sqs.get_queue_attributes(
    QueueUrl=queue_url,
    AttributeNames=["QueueArn"]
)["Attributes"]["QueueArn"]
print(queue_arn)
# Criando buckets no S3
s3.create_bucket(Bucket="imagens")
s3.create_bucket(Bucket="thumbnails")

# Zip Lambda
with zipfile.ZipFile("lambda.zip", "w") as z:
    z.write("handler.py", "handler.py")

# Criar Lambda
try:
    lambda_client.create_function(
        FunctionName="gerar-thumbnail",
        Runtime="python3.9",
        Role="arn:aws:iam::000000000000:role/lambda-role",
        Handler="handler.handler",
        Code={"ZipFile": open("lambda.zip", "rb").read()},
    )
except:
    lambda_client.update_function_code(
        FunctionName="gerar-thumbnail",
        ZipFile=open("lambda.zip", "rb").read(),
    )


lambda_client.create_event_source_mapping(
    EventSourceArn=queue_arn,
    FunctionName="gerar-thumbnail",
    BatchSize=1
)

# Recebe mensagens da fila
resp = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10)
for msg in resp.get("Messages", []):
    # Invoca a Lambda manualmente
    lambda_client.invoke(
        FunctionName="gerar-thumbnail",
        Payload=json.dumps({"Records": [json.loads(msg["Body"])]}).encode()
    )
    # Apaga a mensagem da fila
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg["ReceiptHandle"])

# S3 → SQS (ESTÁVEL)
s3.put_bucket_notification_configuration(
    Bucket="imagens",
    NotificationConfiguration={
        "QueueConfigurations": [
            {
                "QueueArn": queue_arn,
                "Events": ["s3:ObjectCreated:*"]
            }
        ]
    }
)

print("Ambiente pronto!")