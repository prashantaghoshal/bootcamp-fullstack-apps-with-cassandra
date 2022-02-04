#!/usr/bin/env python3
# THIS FILE WILL BE OVERWRITTEN. DO NOT MAKE ANY CHANGES HERE

import atexit
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# This is the Zip file you downloaded
SECURE_CONNECT_BUNDLE = '/workspace/bootcamp-fullstack-apps-with-cassandra/secure-connect-workshops.zip'
# This is the "Client Id" value you obtained earlier
USERNAME = "lRcMWccXybYmellPvXhKrrTF"
# This is the "Client Secret" value you obtained earlier
PASSWORD = "B93npiGZaLMpXUqPOol3,j9UWJ--D+g8p2CcRMqHWX9q4SKlo1vB3Gv+PdQ7lSc-sA.KY7g5HD,0mjPgBf7AsZZXJm,m14EDchDHsiLwJnn,WNDro1bDyrFKF.nvN+Gt"
# This is the keyspace name
KEYSPACE = "todos"


secure_connect_bundle = SECURE_CONNECT_BUNDLE
path_to_creds = ''
cluster = Cluster(
    cloud={
        'secure_connect_bundle': SECURE_CONNECT_BUNDLE
    },
    auth_provider=PlainTextAuthProvider(USERNAME, PASSWORD)
)
session = cluster.connect(KEYSPACE)


@atexit.register
def shutdown_driver():
    cluster.shutdown()
    session.shutdown()
