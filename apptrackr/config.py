from apptrackr.db import DB
from apptrackr.types import Resume, SystemPrompt

import hashlib

class Configuration:
    
    
    def getUserHash(username):
        md5 = hashlib.md5()
        md5.update(username.encode())
        return md5.hexdigest()