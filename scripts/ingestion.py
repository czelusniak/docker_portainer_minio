import boto3
import pandas as pd
from io import StringIO
from datetime import datetime
from faker import Faker

def generate_data(number_of_rows):
    fake = Faker() 
    
    # List Comprehension para criar X linhas
    data = [
        {
            'name': fake.name(),     # Qual método gera nome?
            'city': fake.city(),     # Qual método gera cidade?
            'email': fake.email(),    # Tente descobrir o método de email
            'amount': fake.random_int(min=10, max=1000), # Valor da venda
            'date': fake.date_this_year()
        } 
        for i in range(number_of_rows) 
    ]
    return data

s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='minio',
    aws_secret_access_key='minio123'
)

bucket_name = 'raw-data'

answer = s3_client.list_buckets()

bucket_list = [b['Name'] for b in answer['Buckets']]

print(bucket_list)

if bucket_name in bucket_list:
    print(f"✅ Bucket {bucket_name} found!")
else:
    print(f"❌Bucket {bucket_name} not found!. Creating 'raw-data' bucket...")
    s3_client.create_bucket(Bucket='raw-data')
    print(f"Bucket {bucket_name} created!")


df = pd.DataFrame(generate_data(100))

csv_buffer = StringIO()

df.to_csv(csv_buffer, index=False)

file_name = f'generic_example_{datetime.now().strftime("%Y-%m-%d_%H-%M")}.csv'

s3_client.put_object(
    Bucket='raw-data',
    Key=file_name, 
    Body=csv_buffer.getvalue()   
)

print("Upload completed!")