import json

copy_json = {}


def iterate_over_list(val, mappings):
    for item in val:
        if isinstance(item, dict):  
            object_inside_list = iterate_over_dict(item, {})
            mappings.append(object_inside_list)
        else:
            mappings.append(item)
    return mappings


def iterate_over_dict(val, mappings):
    for key, val in val.items():
        if isinstance(val, dict):
            mappings[key] = iterate_over_dict(val, {})
        elif isinstance(val, list):
            mappings[key] = iterate_over_list(val, [])
        else:
            """
                We can do any sort of operations on normal key:value pair before storing it in object
            """
            mappings[key] = val
    return mappings


def iterate_over_json():
    with open("random.json", "r") as f:
        data = json.loads(f.read())
    for key, val in data.items():
        if isinstance(val, list):
            copy_json[key] = iterate_over_list(val, [])
        elif isinstance(val, dict):
            copy_json[key] = iterate_over_dict(val, {})
        else:
            """
                We can do any sort of operations on normal key:value pair before storing it in object
            """
            copy_json[key] = val

    print("The two json are equal = ", json.dumps(data)==json.dumps(copy_json))

iterate_over_json()

print(json.dumps(copy_json, indent=4, sort_keys=True))
