file_destination = input().split("\\")
file = file_destination[-1]
file_name = file.split('.')[0]
file_extension = file.split(".")[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")