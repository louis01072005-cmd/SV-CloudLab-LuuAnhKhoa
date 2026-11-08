import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Thực hành PaaS - Render & Flask</title>
</head>
<body style="font-family: Arial, sans-serif; max-width: 720px; margin: 50px auto; padding: 20px; border: 2px solid #2E5B88; border-radius: 8px;">
<h2 style="color: #1F4E79;">Triển khai ứng dụng Python Flask trên PaaS (Render) thành công!</h2>
<p><b>Họ và tên sinh viên:</b> Lưu Anh Khoa</p>
<p><b>Mã số sinh viên (MSSV):</b> 2324802010255</p>
<p><b>Mô hình dịch vụ:</b> Platform as a Service (PaaS) - Render Cloud</p>
</body>
</html>
'''

@app.route('/health')
def health():
    return jsonify(status="UP", platform="Render PaaS", framework="Flask")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
