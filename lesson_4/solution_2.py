class FileHandler:
    def read():
        pass
    def write(data: str):
        pass

    @classmethod
    def save_data(handler: FileHandler, data: str):
        

class TextFileHandler(FileHandler):
    def read():
        print("Файл был прочитан")
    
    def write(data: str):
        print("Файл был записан")

class BinaryFileHandler(FileHandler):
    def read():
        print("Файл был прочитан")
    
    def write(data: str):
        print("Файл был записан")

