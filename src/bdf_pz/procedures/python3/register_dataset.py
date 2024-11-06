import os
path = "{{ path }}".strip()
name = "{{ name }}".strip()

# register dataset
if os.path.isfile(path):     
    pz.DataDirectory().registerLocalFile(os.path.abspath(path), name)

elif os.path.isdir(path):
    pz.DataDirectory().registerLocalDirectory(os.path.abspath(path), name)

else:
    raise InvalidCommandException(
        f"Path {path} is invalid. Does not point to a file or directory."
    )

print(f"Registered {name}")