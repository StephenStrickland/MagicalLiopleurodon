from mongoengine import Document, DateTimeField, StringField, PointField, ObjectIdField, BooleanField, IntField

class Host(Document):
    meta = {'collection': 'Hosts'}
    Name = StringField(required=True)
    GpsCoordinates = PointField()
    EnableApi = BooleanField(required=True)
    Port = IntField(required=True, default=8080)
    BaudRate = IntField(required=True,default=9600)
    XBeePort = StringField(required=True, default='')
    UsbPort = StringField(required=True, default='')
    LogMode = 0
# [database]
# UseMongo = True
# MongoConnectionString = mongodb://admin:g0KTAY6MrcIj2KBPO2jq@cluster0-shard-00-00-f2uhz.mongodb.net:27017,cluster0-shard-00-01-f2uhz.mongodb.net:27017,cluster0-shard-00-02-f2uhz.mongodb.net:27017/Lio?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin


def get_host_by_id(id):
    return Host.objects(id=id)

def get_hosts():
    return Host.objects()

def create_host(host):
    host = Host(**host)
    host.save()
    return host.id

