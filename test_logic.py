import json

def filter_mounts_by_expansion(expansion):
    filtered_list = []
    with open("mounts.json", "r") as f:
        all_mounts = json.load(f)
        for mount in all_mounts:
            if mount["expansion"] == expansion:
                filtered_list.append(mount)
                print(f"Mount: {mount['name']} | Drops from: {mount['dropped_from']}")
    #print(filtered_list)

def filter_mounts_by_type(mount_type):
    filtered_list = []
    with open("mounts.json", "r") as f:
        all_mounts = json.load(f)
        for mount in all_mounts:
            if mount["mount_type"] == mount_type:
                filtered_list.append(mount)
                print(f"Mount: {mount['name']} | Drops from: {mount['dropped_from']}")
    #print(filtered_list)


print("\nTesting a different one:")
filter_mounts_by_type("Horse")