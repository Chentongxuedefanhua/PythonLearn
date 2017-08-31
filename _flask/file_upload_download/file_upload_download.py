#coding: utf-8
from werkzeug.utils import secure_filename
from flask import Flask,render_template,jsonify,request,send_from_directory
import os

"""
@file: index.py
@time: 2017/8/31 
@author: chenfan
"""

app = Flask(__name__)
upload_dir = 'upload'
app.config['UPLOAD_FOLDER'] = upload_dir
basedir = os.path.abspath(os.path.dirname(__file__)) #当前文件的上层文件夹，e:\file_upload_down
ALLOWED_EXTENSIONS = ('txt','png','jpg','xls','JPG','PNG','xlsx','gif','GIF')

@app.route('/test/upload')
def upload_test():
    return render_template('file.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file_dir = os.path.join(basedir,app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    print os.path.isdir(file_dir)
    f = request.files['myfile'] #从表单file字段中获取文件，myfile为name的值
    if f :
        fname = secure_filename(f.filename)
        f.save(os.path.join(file_dir,fname))
        return jsonify({"status_code":0, "msg":"upload success"})
    else:
        return jsonify({  "status_code":1, "msg":"upload error"})

@app.route("/download/<filename>")
def down_load(filename):
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if request.method == "GET":
        if os.path.isfile(os.path.join(file_dir,filename)):
            return send_from_directory(file_dir, filename,as_attachment=True)
        else:
            return jsonify({"status_code":404,"msg":"file not found"}),404

if __name__ == '__main__':
    app.run(debug=True,threaded=True,host='0.0.0.0')