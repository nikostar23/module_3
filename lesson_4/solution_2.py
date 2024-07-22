class FileHandler:
    def read():
        pass
    def write(data: str):
        pass

class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        print(f"Текстовый файл {self.filename} был прочитан.")
    
    def write(self, data: str):
        print(f"Данные \"{data}\" были записаны в текстовый файл {self.filename}.")

class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        print(f"Бинарный файл {self.filename} был прочитан.")
    
    def write(self, data: str):
        print(f"Данные \"{data}\" были записаны в бинарный файл {self.filename}.")

def save_data(handler: FileHandler, data: str):
    handler.read()
    handler.write(data)

# Пример использования
text_handler = TextFileHandler("example.txt")
binary_handler = BinaryFileHandler("example.bin")

save_data(text_handler, "Hello, World!")
save_data(binary_handler, "0101010101")