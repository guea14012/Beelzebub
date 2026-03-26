import os
import json
import requests
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

CHUNK_SIZE = 1024 * 512

NODES = [
    "http://127.0.0.1:9000",
    "http://127.0.0.1:9001",
    "http://127.0.0.1:9002"
]

METADATA_FILE = "metadata.json"


# -------------------------
# Metadata functions
# -------------------------

def load_metadata():

    if not os.path.exists(METADATA_FILE):
        return {}

    with open(METADATA_FILE) as f:
        return json.load(f)


def save_metadata(data):

    with open(METADATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


# -------------------------
# Check alive nodes
# -------------------------

def alive_nodes():

    alive = []

    for node in NODES:

        try:
            r = requests.get(node + "/list", timeout=2)

            if r.status_code == 200:
                alive.append(node)

        except:
            pass

    return alive


# -------------------------
# Split file
# -------------------------

def split_file(path):

    chunks = []

    with open(path, "rb") as f:

        i = 0

        while True:

            data = f.read(CHUNK_SIZE)

            if not data:
                break

            name = f"chunk_{i}.bin"

            with open(name, "wb") as c:
                c.write(data)

            chunks.append(name)

            i += 1

    return chunks


# -------------------------
# Upload chunk to node
# -------------------------

def upload_chunk(node, chunk):

    try:

        files = {"file": open(chunk, "rb")}

        r = requests.post(node + "/upload", files=files)

        if r.status_code == 200:
            return True

    except Exception as e:

        print("Upload error:", e)

    return False


# -------------------------
# Upload file
# -------------------------

@app.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:
        return {"error": "no file"}, 400

    file = request.files["file"]

    temp = "temp_upload"

    file.save(temp)

    chunks = split_file(temp)

    nodes = alive_nodes()

    if not nodes:
        return {"error": "no nodes available"}, 500

    metadata = load_metadata()

    metadata[file.filename] = []

    i = 0

    for chunk in chunks:

        stored_nodes = []

        node = nodes[i % len(nodes)]

        print("Uploading", chunk, "to", node)

        success = upload_chunk(node, chunk)

        if success:
            stored_nodes.append(node)

        metadata[file.filename].append({
            "chunk": chunk,
            "nodes": stored_nodes
        })

        os.remove(chunk)

        i += 1

    os.remove(temp)

    save_metadata(metadata)

    return {"status": "uploaded"}


# -------------------------
# Download file
# -------------------------

@app.route("/download/<filename>")
def download(filename):

    metadata = load_metadata()

    if filename not in metadata:
        return {"error": "file not found"}, 404

    output_name = "recovered_" + filename

    with open(output_name, "wb") as out:

        for chunk in metadata[filename]:

            node = chunk["nodes"][0]

            url = node + "/chunk/" + chunk["chunk"]

            r = requests.get(url)

            out.write(r.content)

    return send_file(output_name, as_attachment=True)


# -------------------------
# List files
# -------------------------

@app.route("/files")
def files():

    return jsonify(list(load_metadata().keys()))


# -------------------------
# Start server
# -------------------------

if __name__ == "__main__":

    app.run(port=8000)
