try:
    del dataset
except NameError:
    pass
dataset_path = registered_datasets["{{ dataset_name }}"]
dataset = pz.Dataset(dataset_path)

dataset