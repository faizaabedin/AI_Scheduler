import configparser


# read config details from .properties file
config = configparser.RawConfigParser()
config.read('../resources/dbconfig.properties')

# retrieve db authentication credentials from .properties file
db_username = config.get('DBConfig', 'database.user')
db_password = config.get('DBConfig', 'database.password')
db_name = config.get('DBConfig', 'database.name')

db_connection_string = "mongodb://" + db_username + ":" + db_password + "@cluster0-shard-00-00-eeyy0.mongodb.net:27017,cluster0-shard-00-01-eeyy0.mongodb.net:27017,cluster0-shard-00-02-eeyy0.mongodb.net:27017/" + db_name + "?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"

