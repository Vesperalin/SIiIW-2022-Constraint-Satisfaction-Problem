# reads data from file
def read_data_from_file(path_name: str):
    with open('data/' + path_name) as file:
        return file.read()
