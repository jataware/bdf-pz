# Define a class name
# Custom __repr__ to output detailed information about the class and its fields
name = "{{ schema_name }}"
schema = {"__doc__": "{{ schema_description }}",
          "__repr__": custom_repr}
for idx, field in enumerate({{ field_names }}):
    desc = {{ field_descriptions }}[idx]
    schema[field] = pz.Field(desc=desc)       
new_schema = type(name, (pz.Schema,), schema)

# Assign the dynamically created class to a variable using globals()
globals()[name] = new_schema
existing_schemas[name] = new_schema
new_class