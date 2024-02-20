from os import listdir

# TODO: Make it a variable available to the user in the terminal
models_path = "./pretrained_avgpool_minkownormal_features/fc3_avg"


# Get the names of the models, without the extension
def get_model_names(file_path):
    file_names = []
    for file_name in listdir(file_path):
        file_names.append(file_name.replace(".pth.tar", ""))
    return file_names


# Read the file and return the data
def read_file(file_path):
    with open(file_path, "r") as file:
        data = [l.strip() for l in file.readlines()]
    return data


# Write the file back again
def write_file(file_path, data):
    with open(file_path, "w") as file:
        file.writelines(data)


# Modify the file to only contain the models that are in the models folder
def modify_file(file_path):
    modified_data = []
    for line in read_file(file_path):
        if line in get_model_names(models_path):
            modified_data.append(line + "\n")
        else:
            print(f"Model {line} in {file_path} not found in the models folder")
    write_file(file_path, modified_data)


# Call the function to modify the files
modify_file("train.txt")
modify_file("test.txt")
modify_file("val.txt")
