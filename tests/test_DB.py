from unittest import TestCase
from google.cloud.firestore_v1.base_document import DocumentSnapshot

from apptrackr.types import JobApplication, Resume, CoverLetter, SystemPrompt
from apptrackr.db import DB

class TestDB(TestCase):
    def test_retrieve(self):
        recs = DB.retrieveRecords(SystemPrompt)

    def test_create(self):
        rec = SystemPrompt({"owner_id":"abc", "content": "bar"})
        recs = DB.createRecord(rec)        