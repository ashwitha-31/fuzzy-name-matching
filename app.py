from flask import Flask, request, render_template, jsonify
from rapidfuzz import fuzz
from indic_transliteration.sanscript import transliterate, ITRANS, DEVANAGARI
import pandas as pd

app = Flask(__name__)

names_db = [
    "राजेश", "सुरेश", "मुकेश", "mahesh", "ramesh",
    "raj", "rajeshwar", "rajeshwari", "rakesh", "reshma"
]

def get_matches(input_name, threshold=70):
    is_devanagari = any('\u0900' <= c <= '\u097F' for c in input_name)
    translit_name = input_name if is_devanagari else transliterate(input_name, ITRANS, DEVANAGARI)
    matches = []
    for name in names_db:
        score = fuzz.ratio(translit_name.lower(), name.lower())
        if score >= threshold:
            matches.append({"name": name, "score": score})
    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        name = request.form.get("name")
        result = get_matches(name)
    return render_template("index.html", result=result)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if file and file.filename.endswith(".csv"):
        df = pd.read_csv(file)
        results = []
        for index, row in df.iterrows():
            input_name = str(row["Full Name"])
            matches = get_matches(input_name)
            best = matches[0] if matches else {"name": "No match", "score": 0}
            results.append({
                "id": row["ID"],
                "input": input_name,
                "match": best["name"],
                "score": best["score"],
                "remarks": row["Remarks"]
            })
        return render_template("upload_result.html", results=results)
    return "Invalid file"

@app.route("/api/match", methods=["POST"])
def api_match():
    data = request.json
    name = data.get("name", "")
    return jsonify(get_matches(name))

if __name__ == "__main__":
    app.run(debug=True)
