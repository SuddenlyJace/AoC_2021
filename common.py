def get_input(filename):
    with open(filename) as file:
        data = file.read()
    return data