"""Forms for playlist app."""


from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Name", validators=[InputRequired()])
    description = StringField("Style/Mode", validators=[InputRequired()])


class SongForm(FlaskForm):
    """Form for adding songs."""

    name = StringField("Song Name", validators=[InputRequired()])
    description = StringField("Band/Singer", validators=[InputRequired()])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField("Song To Add")
