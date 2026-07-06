from flask import Flask, render_template, redirect
import logic

app = Flask(__name__)

@app.route("/")
def home():
    print("HELLO FROM THE BACKEND!")
    mounts = logic.show_requested_mounts()
    print(f"MOUNT COUNT: {len(mounts)}")
    return render_template("index.html", mount_data=mounts)

@app.route("/cycle_view")
def cycle():
    logic.show_requested_mounts()
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    overall = logic.get_stats()
    expansions = logic.get_expansion_stats()
    return render_template("dashboard.html", overall_stats=overall, expansion_stats=expansions)

if __name__ == "__main__":
    app.run(debug=True)