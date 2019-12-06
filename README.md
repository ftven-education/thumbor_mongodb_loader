# thumbor_mongodb_loader
Thumbor MongoDB GridFS loader


```
LOADER = 'thumbor_mongodb_loader.loader' #loader calling
MONGO_ORIGIN_SERVER_HOST = 'localhost' #host
MONGO_ORIGIN_SERVER_PORT = 27017 #port
MONGO_ORIGIN_READ_PREFERENCE = 'primaryPreferred' #for from slave in replicaSet put there 'secondaryPreferred'
MONGO_ORIGIN_SERVER_DB = 'images' #MongoDB database name, inside it will be created collections fs.files and fs.chunks
MONGO_ORIGIN_SERVER_USER = '' # user
MONGO_ORIGIN_SERVER_PASSWORD = '' # password
MONGO_ORIGIN_SERVER_AUTH = '' # credential stored in this db
MONGO_ORIGIN_SERVER_REPLICASET = 'myReplica' # name of the replicaset - option
```

Url type: https://thumbor-server.domain/[secret|unsafe]/[params]/XXXXXXXXXXXXXXXXXXXXXX[/.../..../.xxx  <= all is facultative after id ]
where `XXXXXXXXXXXXXXXXXXXXXX` is a GridFS `file_id`


##### Configuration example for varnish (recv) with AUTO_WEBP ####
if (req.http.Accept ~ "image/webp") {
  set req.http.Accept = "image/webp";
} else {
  # not present, and we don't care about the rest
  unset req.http.Accept;
}
##################################################################


Tested on Debian 9 with:
- Thumbor (pip) 6.5
- MongoDB 4.0.4
- PyMongo 3.4