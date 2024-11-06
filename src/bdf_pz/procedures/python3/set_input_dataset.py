try:
    schema = existing_schemas["{{input_schema}}"]
except KeyError:
    raise ValueError(f"Schema '{{input_schema}}' not found in existing schemas!")
dataset = pz.Dataset(source="{{ dataset }}", schema=schema)

dataset