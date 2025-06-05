from flask import Flask, request, jsonify, render_template, send_file
from werkzeug.utils import secure_filename
import os
import subprocess
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file part'}), 400

    file = request.files['audio']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(input_path)

    output_filename = f"converted_{uuid.uuid4().hex}.wav"
    output_path = os.path.join(RESULT_FOLDER, output_filename)

    # 模擬聲音模仿處理流程 (此處用 ffmpeg 替代真實模型)
    # 替換成 so-vits-svc 推理命令
    subprocess.call(['ffmpeg', '-i', input_path, output_path])

    return jsonify({"output": f"/result/{output_filename}"})

@app.route('/result/<filename>')
def result(filename):
    return send_file(os.path.join(RESULT_FOLDER, filename), mimetype='audio/wav')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
