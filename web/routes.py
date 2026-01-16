from flask import Blueprint, request, jsonify, render_template
from logic.csv_processor import process_csv
from flask import send_file
import io
import pandas as pd
routes = Blueprint("routes", __name__)


@routes.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@routes.route("/upload", methods=["POST"])
def upload_csv():
    # Check if file is present
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    # Check filename
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Validate CSV extension
    if not file.filename.lower().endswith(".csv"):
        return jsonify({"error": "Please upload a .csv file"}), 400

    try:
        result = process_csv(file)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes.route("/download/csv", methods=["POST"])
def download_csv():
    file = request.files.get("file")
    if not file:
        return {"error": "No file uploaded"}, 400

    original_name = file.filename.rsplit(".", 1)[0]
    download_name = f"{original_name}_cleaned.csv"

    file.seek(0)
    df = pd.read_csv(file).drop_duplicates()

    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)

    return send_file(
        io.BytesIO(buffer.getvalue().encode("utf-8")),
        mimetype="text/csv",
        as_attachment=True,
        download_name=download_name
    )


@routes.route("/download/excel", methods=["POST"])
def download_excel():
    file = request.files.get("file")
    if not file:
        return {"error": "No file uploaded"}, 400

    original_name = file.filename.rsplit(".", 1)[0]
    download_name = f"{original_name}_cleaned.xlsx"

    file.seek(0)
    df = pd.read_csv(file).drop_duplicates()

    output = io.BytesIO()
    df.to_excel(output, index=False, engine="openpyxl")
    output.seek(0)

    return send_file(
        output,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name=download_name
    )
