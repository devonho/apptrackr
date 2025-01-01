from apptrackr.db import DB
from apptrackr.types import Resume, SystemPrompt

class Configuration:
    
    def getResume():
        recs = DB.retrieveRecords(Resume)
        return recs[0]
    
    def getSystemPrompt():
        recs = DB.retrieveRecords(SystemPrompt)
        return recs[0]    