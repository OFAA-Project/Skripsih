from wtforms import Form
from wtforms.fields import BooleanField, TextField


class LocationForm(Form):
    name = TextField()
    address = TextField()


class EventForm(Form):
    name = TextField()
    is_public = BooleanField()


json = {
    'name': 'First Event',
    'location': {'name': 'some location'},
}

form = EventForm.from_json(json)

