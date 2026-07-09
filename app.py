from flask import Flask, render_template, redirect, request
import logic
import json

app = Flask(__name__)

with open("mounts.json", "r") as f:
    all_mounts = json.load(f)

with open("settings.json", "r") as f:
    settings = json.load(f)

@app.route("/mount_index")
def mount_index():
    expansion = request.args.get("expansion")
    mount_type = request.args.get("mount_type")
    special = request.args.get("special")
    expansions = logic.filter_out_expansions(all_mounts)
    mount_types = logic.filter_out_unique_models(all_mounts)
    if expansion:
        mounts = logic.filter_mounts_by_expansion(all_mounts, expansion)
    elif mount_type:
        mounts = logic.filter_mounts_by_type(all_mounts, mount_type)
    elif special:
        mounts = logic.show_special_filters(all_mounts, special)
    else:
        mounts = logic.get_available_mounts(all_mounts)
    return render_template("index.html", mount_data=mounts, expansions=expansions, mount_types=mount_types, special_filters=logic.SPECIAL_FILTERS)

@app.route("/")
def dashboard():
    overall = logic.get_stats(all_mounts)
    expansions_stats = logic.get_expansion_stats(all_mounts)
    expansions = logic.filter_out_expansions(all_mounts)
    mount_type = logic.filter_out_unique_models(all_mounts)
    return render_template("dashboard.html", overall_stats=overall, expansion_stats=expansions_stats, expansions=expansions, mount_type=mount_type, special_filters=logic.SPECIAL_FILTERS)

if __name__ == "__main__":
    app.run(debug=True)