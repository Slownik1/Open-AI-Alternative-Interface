from wtforms import Form, StringField, validators

class PromptForm(Form):
    prompt = StringField('Username', [validators.Length(min=1, max=1000)])
