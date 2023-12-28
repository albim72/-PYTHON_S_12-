class FileManager:
    def __init__(self,filename,mode,encode):
        self.filename = filename
        self.mode = mode
        self.encode = encode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"strumień: {self.file}")
        self.file.close()

with FileManager('testowy.txt','w','utf-8') as f:
    f.write('to jest istotny komunikat\n')

print(f.closed)

with open("abc.txt","a",encoding="utf-8") as gh:
    gh.write("to jest drugi plik -> open\n")

print(gh.closed)

with FileManager("abc.txt","r","utf-8") as f:
    print(f.read())


