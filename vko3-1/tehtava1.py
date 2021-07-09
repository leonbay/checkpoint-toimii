
import requests

response = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")

dataframe = response.json()

items_data = dataframe["items"]

arvot = []

for i in items_data:
    arvot.append(f"{i['parameter']}")

arvot_str = "\n".join(map(str, arvot))


with open ("checkpoint.txt", "w") as tiedosto:
    tiedosto.write(arvot_str)
    tiedosto.close()

""" Get authenticated to GCP
Serviceaccount: servunakki@able-inn-317511.iam.gserviceaccount.com
Get Key
Run: $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
Verify auth: def implicit():
    from google.cloud import storage
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    print(buckets) """


def create_bucket(bucket_name):
    from google.cloud import storage

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    new_bucket = storage_client.create_bucket(bucket, location="us")

    return new_bucket

create_bucket("checkpoint-buketti")


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    from google.cloud import storage

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

upload_blob("checkpoint-buketti", r"C:\Users\Leo1\Downloads\KOULUTUSMATERIAALIT\3.viikko\checkpoint\projekti\vko3-1\checkpoint.txt", "checkpoint.txt")












