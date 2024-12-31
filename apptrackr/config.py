from apptrackr.db import DB


class Configuration:
    
    def getResume():
        recs = DB.retrieveResumes()
        return recs[0]
    
    def getSystemPrompt():
        recs = DB.retrieveSysPrompts()
        return recs[0]    