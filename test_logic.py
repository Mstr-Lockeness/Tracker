import json

def filter_mounts_by_expansion(expansion):
    filtered_list = []
    with open("mounts.json", "r") as f:
        all_mounts = json.load(f)
        for mount in all_mounts:
            if mount["expansion"] == expansion:
                filtered_list.append(mount)
                print(f"Mount: {mount['name']} | Drops from: {mount['dropped_from']}")
    return filtered_list

def filter_mounts_by_type(mount_type):
    filtered_list = []
    with open("mounts.json", "r") as f:
        all_mounts = json.load(f)
        for mount in all_mounts:
            if mount["mount_type"] == mount_type:
                filtered_list.append(mount)
                print(f"Mount: {mount['name']} | Drops from: {mount['dropped_from']}")
    return filtered_list

def filter_rep_by_expansion(expansion):
    filtered_list = []
    with open("reputation.json", "r") as f:
        all_reputation = json.load(f)
        for rep in all_reputation:
            if rep["expansion"] == expansion:
                filtered_list.append(rep)
                print(f"Name: {rep['name']} | Faction: {rep['faction']}")
    return filtered_list

def mark_mount_as_obtained(mount_name):
    with open("mounts.json", "r") as f:
        all_mounts = json.load(f)
    for mount in all_mounts:
        if mount["name"] == mount_name:
            if mount["obtained"] == True:
                mount["obtained"] = False
            else:
                mount["obtained"] = True
            print(f"{mount['name']} marked as {mount['obtained']}")
            break
    with open("mounts.json", "w") as f:
        json.dump(all_mounts, f, indent=4)

def increase_rank_of_reputation(reputation):
    with open("reputation.json", "r") as f:
        reps =  json.load(f)
    for rep in reps:
        if rep["name"] == reputation:
            ranks = rep["ranks"]
            current = rep["current_rank"]
            current_index = ranks.index(current)
            if current_index < len(ranks) -1:
                rep["current_rank"] = ranks[current_index + 1]
                print(f"Leveled up {reputation} to {rep['current_rank']}!")
            break
    with open("reputation.json", "w") as f:
        json.dump(reps, f, indent=4)


def decrease_rank_of_reputation(reputation):
    with open("reputation.json", "r") as f:
        reps =  json.load(f)
    for rep in reps:
        if rep["name"] == reputation:
            ranks = rep["ranks"]
            current = rep["current_rank"]
            current_index = ranks.index(current)
            if current_index > 0:
                rep["current_rank"] = ranks[current_index - 1]
                print(f"Whoops! We fixed {reputation} back to {rep['current_rank']}!")
            break
    with open("reputation.json", "w") as f:
        json.dump(reps, f, indent=4)

def show_requested_mounts():
    with open("settings.json", "r") as f:
        values = json.load(f)
        view = values["view"]
    with open("mounts.json", "r") as f:
        mounts = json.load(f)
    filtered_list = []
    view += 1
    if view == 7:
        view = 0
    for mount in mounts:
        if view == 1: #default, shows both owned and unowned (if obtainable)
            if mount["still_obtainable"] == True or mount["obtained"] == True:
                filtered_list.append(mount)
        elif view == 2: #only shows owned
            if mount["obtained"] == True:
                filtered_list.append(mount)
        elif view == 3: #only shows unowned
            if mount["obtained"] == False and mount["still_obtainable"] == True:
                filtered_list.append(mount)
        elif view == 4: #only shows favorites
            if mount["favorite"] == True:
                filtered_list.append(mount)
        elif view == 5: #only shows mounts available to Alliance
            if mount["faction"] == "Alliance" or mount["faction"] == "Universal":
                filtered_list.append(mount)
        elif view == 6: #only shows mounts available to Horde
            if mount["faction"] == "Horde" or mount["faction"] == "Universal":
                filtered_list.append(mount)
        else: # #only shows unobtainable mounts
            if mount["still_obtainable"] == False:
                filtered_list.append(mount)
    values["view"] = view
    for mount in filtered_list:
        print(f"Mount: {mount['name']} | Drops from: {mount['dropped_from']}")
    with open("settings.json", "w") as f:
        json.dump(values, f, indent=4)
    return filtered_list
    
def filter_mounts_by_source(source_type):
    filtered_list = []
    with open("mounts.json", "r") as f:
        mounts = json.load(f)
    for mount in mounts:
        if mount["source_type"] == source_type:
            filtered_list.append(mount)
            print(f"Mount: {mount['name']} | Drops from: {mount['dropped_from']}")
    return filtered_list

def mark_mount_as_favorite(mount_name):
    with open("mounts.json", "r") as f:
        mounts = json.load(f)
    for mount in mounts:
        if mount["name"] == mount_name:
            if mount["favorite"] == True:
                mount["favorite"] = False
                print(f"{mount["name"]} has been removed from your favorites.")
            else:
                mount["favorite"] = True
                print(f"{mount["name"]} has been added to your favorites.")
    with open("mounts.json", "w") as f:
        json.dump(mounts, f, indent=4) 


print("Test 1:")
mark_mount_as_favorite("Invincible")

