import os

def list_files(path: str) -> list:
    """列出指定路径下的所有文件"""
    return os.listdir(path)

def read_file(file_path: str) -> str:
    """读取指定文件的内容"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def rename_file(old_name: str, new_name: str) -> None:
    """重命名文件"""
    os.rename(old_name, new_name)    