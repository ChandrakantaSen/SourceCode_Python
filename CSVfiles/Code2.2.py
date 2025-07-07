# File Handling - Read BINARY file (AUDIO File) in read mode
fh = open('E:\\StudyWorkspace - I\\Source_Code (Python)\\CSVfiles\\Files\\audio.mp3','rb')
data = fh.read()
print(data)