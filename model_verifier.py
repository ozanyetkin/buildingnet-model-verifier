from os import listdir

# TODO: Make it a variable available to the user in the terminal
models_path = "./pretrained_avgpool_minkownormal_features/fc3_avg"
file_names = []

# Iterate directory
for file_name in listdir(models_path):
    file_names.append(file_name)

print(file_names)
