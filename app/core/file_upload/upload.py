from django.conf import settings
from .storage_backends import LocalFileStorage, S3FileStorage

def file_upload(file):
    if settings.USE_LOCAL_FILE_STORAGE:
        storage_backend = LocalFileStorage()
    else:
        storage_backend = S3FileStorage()

    # Save the file and get the file URL using the injected storage backend
    file_name = f"{uuid.uuid4()}-{file.name}"
    file_path_or_url = storage_backend.save_file(file, file_name)
    url = storage_backend.get_file_url(file_name)

    return url