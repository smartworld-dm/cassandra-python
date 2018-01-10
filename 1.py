from dse.cluster import Cluster
from dse.auth import PlainTextAuthProvider

auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster(auth_provider=auth_provider, protocol_version=3)

print("Port: ", cluster.port)
print("Username: ", cluster.auth_provider.username)
print("Password: ", cluster.auth_provider.password)


try:
	session = cluster.connect()
	print("Connection succeeded!")
except:
	print("Connection failed!")