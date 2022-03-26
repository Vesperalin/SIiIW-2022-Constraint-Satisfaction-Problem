def read_data_from_file(path_name):
    with open('data/' + path_name) as file:
        return file.read()
