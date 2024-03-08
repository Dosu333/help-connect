from .file_storage import FileStorage
from decouple import config
import boto3
import os


class LocalFileStorage(FileStorage):
    def save_file(self, file, file_name):
        # Save the file to the local file system
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return file_path

    def get_file_url(self, file_name):
        # Return the URL of the file in the local file system
        return os.path.join(settings.MEDIA_URL, file_name)


class S3FileStorage(FileStorage):
    def save_file(self, file, file_name):
        # Save the file to AWS S3
        access_key = config('AWS_ACCESS_KEY_ID')
        secret_key = config('AWS_SECRET_ACCESS_KEY')
        bucket_name = config('AWS_S3_BUCKET_NAME')
        s3_client = boto3.client('s3', access_key, secret_key)
        s3_client.upload_file(file, bucket_name, file_name)
        return f'https://{bucket_name}.s3.amazonaws.com/{file_name}'

    def get_file_url(self, file_name):
        # Return the URL of the file in AWS S3
        return f'https://{bucket_name}.s3.amazonaws.com/{file_name}'