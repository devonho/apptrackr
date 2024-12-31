from google.cloud.firestore import Client

class DB:
    db_name = "apptrackr-user-data"

    def _createRecord(collection, rec):      
        client = Client(database=DB.db_name)
        collection = client.collection(collection)
        collection.document().set(rec)
        client.close()            

    def _retrieveRecords(collection):
        client = Client(database=DB.db_name)
        collection = client.collection(collection)
        docs = collection.stream()
        client.close()            
        return docs

    def createApplication(rec):      
        DB._createRecord("applications", rec)

    def retrieveApplications():      
        def marshal(rec):
            res = {}
            fields = ["job_title", "job_description", "resume", "cover_letter", "system_prompt",]
            for f in fields:
                try:                    
                    res[f] = rec.get(f)
                except Exception:
                    res[f] = None
            return res

        recs = [marshal(rec) for rec in DB._retrieveRecords("applications")]



        return recs

    def createResume(rec):      
        DB._createRecord("resumes", rec)

    def retrieveResumes():      
        return [{"content": rec.get("content")} for rec in DB._retrieveRecords("resumes")]
    
    def createSysPrompt(rec):      
        DB._createRecord("system_prompts", rec)

    def retrieveSysPrompts():      
        return [{"content": rec.get("content")} for rec in DB._retrieveRecords("system_prompts")]

if __name__ == "__main__":
    # with open("system.txt") as f:
    #     text = f.read()
    #     DB.createSysPrompt({"content": text})

    res = DB.retrieveApplications()
    print(res)

