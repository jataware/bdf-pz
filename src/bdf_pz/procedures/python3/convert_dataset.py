convert_schema = existing_schemas["{{ schema_name }}"]

cardinality_str = "{{cardinality}}"

cardinality = pz.Cardinality.ONE_TO_MANY if cardinality_str == "one_to_many" else pz.Cardinality.ONE_TO_ONE

#assert dataset exists in scope
assert "dataset" in locals(), "Dataset should be defined in the current scope. Please set the input dataset first."
dataset = dataset.sem_add_columns(convert_schema, cardinality=cardinality)

dataset