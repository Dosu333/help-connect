class FileStorage:
    def save_file(self, file, file_name):
        raise NotImplementedError()

    def get_file_url(self, file_name):
        raise NotImplementedError()