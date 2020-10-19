from wtforms import Form, StringField, FileField
from wtforms.validators import Length, EqualTo, InputRequired, ValidationError
from flask_wtf.file import FileRequired, FileAllowed


class RegisterFormValidate(Form):
    username = StringField(validators=[Length(min=3, max=25)])
    passwd = StringField(validators=[Length(min=6, max=50)])
    info = StringField(validators=[InputRequired()])
    pass_repeat = StringField(validators=[Length(min=6, max=50), EqualTo('passwd')])

    def validate_info(self, field):
        print(field.data)
        if len(field.data) == 5:
            print('why so simple.')
            raise ValidationError('5 word is not ok!')


class SettingValidate(Form):
    username = StringField(validators=[Length(min=3, max=25)])
    passwd = StringField(validators=[Length(min=6, max=50)])
    info = StringField(validators=[InputRequired()])
    pass_repeat = StringField(validators=[Length(min=6, max=50), EqualTo('passwd')])


class FileUploadValidate(Form):
    im_na = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'])])
    img_info = StringField(validators=[InputRequired()])