import boto3
#Utilzando biblioteca BOTO3 da AWS. 
# É possível simular upload, download, listagem, presigned URL do serviço de PaaS S3, da AWS

def conecta():
    s3 = boto3.client(
        "s3",
        endpoint_url="http://localhost:4566",
        region_name="us-east-1",
        aws_access_key_id="test",
        aws_secret_access_key="test",
    )
    return s3

''' Simula a criação de um bucket S3'''
def cria_bucket(s3_obj, nome_bucket):
    s3_obj.create_bucket(Bucket=nome_bucket)
    print(f"Bucket {nome_bucket} criado!")

''' Simula a criação de um arquivo em um bucket s3'''
def upload(s3_obj, nome_bucket):
    #Criando um arquivo simples de texto chamado exemplo.txt
    with open("exemplo.txt", "w") as f:
        f.write("Olá, Estou testando localstack")
    # Fazendo o Upload
    s3_obj.upload_file("exemplo.txt", nome_bucket, "exemplo.txt")    

''' Simula a leitura de arquivo de um bucket'''
def ler(s3_obj, nome_bucket, nome_arquivo):
    obj = s3_obj.get_object(Bucket=nome_bucket, Key=nome_arquivo)
    print(obj["Body"].read().decode())


''' Simula a remoção de um arquivo de um bucket'''
def remove(s3_obj, nome_bucket, nome_arquivo):
    s3_obj.delete_object(Bucket=nome_bucket, Key=nome_arquivo)


''' Obtém a URL de um arquivo'''
def get_url(s3_obj, nome_bucket, nome_arquivo):
    url = s3_obj.generate_presigned_url(
        "get_object",
        Params={"Bucket": nome_bucket, "Key": nome_arquivo},
        ExpiresIn=3600
    )
    print(url)

s3=conecta()
cria_bucket(s3, "meu-bucket")
upload(s3, "meu-bucket")
ler(s3, "meu-bucket", "exemplo.txt")
get_url(s3, "meu-bucket", "exemplo.txt")

