import os

dataset_path = os.path.join(DATA_PATH, "{{ dataset_name }}")
files = os.listdir(dataset_path)

files