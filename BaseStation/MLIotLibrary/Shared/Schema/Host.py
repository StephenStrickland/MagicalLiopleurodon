from mongoengine import Document, DateTimeField, StringField, PointField, ObjectIdField

class Host(Document):
    Name = StringField(required=True)
    GpsCoordinates = PointField()
