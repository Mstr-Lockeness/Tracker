import json

SPECIAL_FILTERS = ["Horde", "Alliance", "Favorites", "Obtained", "Unobtained", "All Obtainable", "Unobtainable"]

def show_special_filters(mounts, special):
    filtered_list = []
    for mount in mounts:
        if special == "Obtained": 
            if mount["obtained"] == True:
                filtered_list.append(mount)
        elif special == "Unobtained": 
            if mount["obtained"] == False:
                filtered_list.append(mount)
        elif special == "Favorites": 
            if mount["favorite"] == True:
                filtered_list.append(mount)
        elif special == "Alliance":
            if mount["faction"] == "Alliance" or mount["faction"] == "Universal":
                filtered_list.append(mount)
        elif special == "Horde":
            if mount["faction"] == "Horde" or mount["faction"] == "Universal":
                filtered_list.append(mount)
        elif special == "Unobtainable":
            if mount["still_obtainable"] == False:
                filtered_list.append(mount)
        else:  #All Obtainable
            if mount["still_obtainable"] == True or mount["obtained"] == True:
                filtered_list.append(mount)
    return filtered_list

def filter_mounts_by_type(all_mounts, mount_type):
    filtered_list = []
    for mount in all_mounts:
        if mount["mount_type"] == mount_type:
            filtered_list.append(mount)
    return filtered_list

def filter_mounts_by_expansion(all_mounts, expansion):
    filtered_list = []
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

def get_stats(mounts):
    total = len(mounts)
    obtained = len([m for m in mounts if m["obtained"]])
    return{
        "total": total,
        "obtained": obtained,
        "percentage": round((obtained / total) * 100, 2) if total > 0 else 0
    }

def get_expansion_stats(mounts):
    stats = {}
    for mount in mounts:
        if not mount.get("expansion"):
            continue
        exp = mount["expansion"]
        if exp not in stats:
            stats[exp] = {"owned": 0, "total": 0}
        stats[exp]["total"] += 1
        if mount["obtained"]:
            stats[exp]["owned"] += 1
    return stats

def filter_out_expansions(mounts):
    filtered_list = []
    for mount in mounts:
        if mount["expansion"] not in filtered_list:
            filtered_list.append(mount["expansion"])
    return filtered_list

def filter_out_unique_models(mounts):
    filtered_list = []
    for mount in mounts:
        if mount["mount_type"] not in filtered_list:
            filtered_list.append(mount["mount_type"])
            filtered_list.sort()
    return filtered_list

def get_available_mounts(mounts):
    filtered_list = []
    if mount["still_obtainable"] == True or mount["obtained"] == True:
        filtered_list.append(mount)
    return filtered_list
    