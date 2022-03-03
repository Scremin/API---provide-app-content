# control

import pymongo
from pymongo import MongoClient


def get_a():

    try:

        pwd_mongo = process.env.PWD_MONGO #
        path_db = f"mongodb+srv://mmmmm1:{pwd_mongo}@cluster0.8tcnc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        
        # atlas.
        #client = MongoClient(path_db)
        #db = client.app_a
        #collection = db["mmmmm_a"] #

        # -- varrer toda a coleção mmmmm_a.
        #results = collection.find({})
        #li = list()
        
        #for x in results:
        #    li.append(x) # receber todas os elems da coleção mmmmm_a.

        #return li
        return pwd_mongo

    except:

        return 'get failed'

