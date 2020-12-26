from main import ma
from models.Audio import Audio
from marshmallow.validate import Length


class AudioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Audio

    # validate by checking file exists???
    audio_file = ma.String(required=True, validate=Length(min=4))


audio_schema = AudioSchema()
audios_schema = AudioSchema(many=True)
