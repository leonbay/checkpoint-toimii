import argparse

parser = argparse.ArgumentParser()
parser.add_argument("rivit", help="syöta tulostettavien rivien määrä", type=int)
args = parser.parse_args()


def download_blob(bucket_name, source_blob_name, destination_file_name):
    from google.cloud import storage

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)


download_blob("checkpoint-buketti", "checkpoint.txt", r"C:\Users\Leo1\Downloads\KOULUTUSMATERIAALIT\3.viikko\checkpoint\projekti\vko3-2\checkpoint.txt")


sanalista = []

with open ("checkpoint.txt", "r") as tiedosto:
    for line in tiedosto:
        for word in line.split():
            sanalista.append(word)


jarkatty = sorted(sanalista)

open("checkpoint.txt", "w").close()

x = 0
while args.rivit > 0:
    
    with open ("checkpoint.txt", "a") as f:
        f.write(jarkatty[x])
        f.write("\n")
    x += 1
    args.rivit -= 1
