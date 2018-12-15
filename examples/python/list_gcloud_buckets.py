from google.cloud import storage

# pip install --upgrade google-cloud-storage

storage_client = storage.Client()
for b in storage_client.list_buckets():
   print(b.name)
   print(b.labels)
