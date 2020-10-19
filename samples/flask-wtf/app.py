from flask import Flask, request, render_template, send_from_directory
from config import DevelopmentConfig
from forms import RegisterFormValidate, SettingValidate, FileUploadValidate
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict

UPLOAD_DIRECTORY = os.path.join(os.path.dirname(__file__), 'static', 'images')


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        print(request.form)
        form = RegisterFormValidate(request.form)
        if form.validate():
            return 'welcome, %s' % request.form.get('username')
        else:
            print(form.errors)
            return 'you got errors!'


@app.route('/register2/', methods=['POST', 'GET'])
def register_test():
    form = SettingValidate(request.form)
    if request.method == 'GET':
        return render_template('register.html', form = form)
    else:
        print(request.form)
        form = SettingValidate(request.form)
        if form.validate():
            return 'welcome, %s' % request.form.get('username')
        else:
            print(form.errors)
            return 'you got errors!'


@app.route('/file_up/', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        return render_template('upload_test.html')
    else:
        form = FileUploadValidate(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            img = request.files.get('im_na')
            # img = form.im_na.data   # the same as request.files.get('im_na')
            # info = form.info.data
            # print(dir(img))
            # print(img.stream)
            # print(UPLOAD_DIRECTORY)
            img.save(os.path.join(UPLOAD_DIRECTORY, secure_filename(img.filename)))
            return 'success'
        else:
            print(form.errors)
            return 'you may send some useful info.'


@app.route('/images/<image_name>')
def get_image(image_name):
    return send_from_directory(UPLOAD_DIRECTORY, image_name)


if __name__ == '__main__':
    app.run()
