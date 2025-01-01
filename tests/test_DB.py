from unittest import TestCase
from google.cloud.firestore_v1.base_document import DocumentSnapshot

from apptrackr.types import JobApplication, Resume, CoverLetter, SystemPrompt
from apptrackr.db import DB

class TestDB(TestCase):
    def test_create(self):
        rec = SystemPrompt({"owner_id":"abc", "content": "bar"})
        recs = DB.createRecord(rec)        

    def test_retrieve(self):
        recs = DB.retrieveRecords(SystemPrompt)

    def test_update(self):
        recs = DB.retrieveRecords(Resume)
        recs[0].title = "Strategy focused"
        DB.updateRecord(recs[0].document_id, recs[0])        
