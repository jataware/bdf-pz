import os

path = "{{ path }}".strip()
name = "{{ name }}".strip()

# register dataset
if os.path.exists(path):
    registered_datasets[name] = path

else:
    raise Exception(
        f"Path {path} is invalid. Does not point to a file or directory."
    )

print(f"Registered {name}")