from google.cloud.firestore import Client

class DB:
    db_name = "apptrackr-user-data"

    def _createRecord(collection, rec):      
        client = Client(database=DB.db_name)
        collection = client.collection(collection)
        collection.document().set(rec)
        client.close()            

    def _retrieveRecords(collection, userhash=None):
        client = Client(database=DB.db_name)
        collection = client.collection(collection)
        docs = []
        if userhash == None:
            docs = collection.stream()
        else:
            docs = collection.where(field_path="owner_id",op_string="==",value=userhash).stream()
        client.close()            
        return docs

    def createRecord(record):
        collection_name = record.collection_name
        d = record.toDict()
        DB._createRecord(collection_name, d)

    def retrieveRecords(recordType : type, userhash=None):
        collection_name = recordType({}).collection_name
        recs = [rec for rec in DB._retrieveRecords(collection_name, userhash)]
        recs = [recordType(rec) for rec in recs]
        return recs

 
