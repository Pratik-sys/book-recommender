from wtforms import Form, StringField, SubmitField, TextField, validators

class GetField(Form):
    title = TextField('title', [validators.data_required()])
    submit = SubmitField('search')
