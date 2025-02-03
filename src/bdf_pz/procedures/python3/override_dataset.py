try:
    del dataset
except NameError:
    pass
dataset = pz.Dataset("{{ input_dataset }}", schema="{{input_schema}}")

dataset