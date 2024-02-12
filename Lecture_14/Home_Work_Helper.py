# import os
# import json


# path = "Home_Work_14/Home_Work_jsons"
# try:
#     os.makedirs(path)
# except FileExistsError:
#     print(f"Folder '{path}' exists")
#     print("Continue working...\n")


# def create_json_file(path, file_name):
#     file_path = f"{path}/{file_name}.json"

#     try:
#         with open(file_path, mode='x', encoding='utf-8') as file:
#             file.write('Create a new json file!')
#     except FileExistsError:
#         print(f"File {file_path} Exists")
#         print("Keep working...\n")

#     return file_path

# def write_data_into_json_file(path, json_file):
#     with open(path, mode='w', encoding='utf-8') as file:
#         file.write(json.dumps(json_file))


# def read_json_file(path):
#     with open(path, mode='r', encoding='utf-8') as file:
#         return json.loads(file.read())


# def update_json_file(path,json_data):
#     Chess_Players_List = read_json_file(path)
#     Chess_Players_List.append(json_data)
#     write_data_into_json_file(path, Chess_Players_List)
