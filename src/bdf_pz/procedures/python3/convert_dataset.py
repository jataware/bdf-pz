dataset = {{ input_dataset }}
convert_schema = {{ schema }}

caridinality_str = "{{cardinality}}"

cardinality = pz.Cardinality.ONE_TO_MANY if caridinality_str == "one_to_many" else pz.Cardinality.ONE_TO_ONE

dataset = dataset.convert({{ schema }}, desc={{ schema }}.__doc__, cardinality=cardinality)

dataset