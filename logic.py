import json

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
    with open("settings.json", "w") as f:
        json.dump(values, f, indent=4)
    return filtered_list

def filter_mounts_by_type(mount_type):
    filtered_list = []
    with open("mounts.json", "r") as f:
        all_mounts = json.load(f)
        for mount in all_mounts:
            if mount["mount_type"] == mount_type:
                filtered_list.append(mount)
    return filtered_list

def filter_mounts_by_expansion(expansion):
    filtered_list = []
    with open("mounts.json", "r") as f:
        all_mounts = json.load(f)
        for mount in all_mounts:
            if mount["expansion"] == expansion:
                filtered_list.append(mount)
    return filtered_list

def filter_rep_by_expansion(expansion):
    filtered_list = []
    with open("reputation.json", "r") as f:
        all_reputation = json.load(f)
        for rep in all_reputation:
            if rep["expansion"] == expansion:
                filtered_list.append(rep)
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
            break
    with open("reputation.json", "w") as f:
        json.dump(reps, f, indent=4)

def filter_mounts_by_source(source_type):
    filtered_list = []
    with open("mounts.json", "r") as f:
        mounts = json.load(f)
    for mount in mounts:
        if mount["source_type"] == source_type:
            filtered_list.append(mount)
    return filtered_list

def mark_mount_as_favorite(mount_name):
    with open("mounts.json", "r") as f:
        mounts = json.load(f)
    for mount in mounts:
        if mount["name"] == mount_name:
            if mount["favorite"] == True:
                mount["favorite"] = False
            else:
                mount["favorite"] = True
    with open("mounts.json", "w") as f:
        json.dump(mounts, f, indent=4) 

def get_stats():
    with open("mounts.json", "r") as f:
        mounts = json.load(f)
    total = len(mounts)
    obtained = len([m for m in mounts if m["obtained"]])
    return{
        "total": total,
        "obtained": obtained,
        "percentage": round((obtained / total) * 100, 2) if total > 0 else 0
    }

def get_expansion_stats():
    with open("mounts.json", "r") as f:
        mounts = json.load(f)
    stats = {}
    for mount in mounts:
        exp = mount["expansion"]
        if exp not in stats:
            stats[exp] = {"owned": 0, "total": 0}
        stats[exp]["total"] += 1
        if mount["obtained"]:
            stats[exp]["owned"] += 1
    return stats