from unittest import TestCase
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from apptrackr.types import JobApplication, Resume, CoverLetter
from datetime import datetime

class TestJobApplication(TestCase):
    def setUp(self):
        super().setUp()
        self.ja = JobApplication({"job_description_title":"foo", "owner_id":"foobaz", "date_of_creation": "20250101T12:00:00Z"})
        JobApplication

    def test_JobApplication_create(self):        
        assert(self.ja.job_description_title == "foo")
        assert(self.ja.owner_id == "foobaz")
        assert(self.ja.date_of_creation == datetime(2025,1,1,12,0,0))

    def test_JobApplication_toDict(self):
        assert(self.ja.toDict()["date_of_creation"] == datetime(2025,1,1,12,0,0))


class TestResume(TestCase):
    def test_Resume_create(self):
        ja = Resume({"content":"foo", "owner_id":"foobaz"})
        assert(ja.content == "foo")
        assert(ja.owner_id == "foobaz")

class TestCoverLetter(TestCase):
    def test_CoverLetter_DocumentSnapshot_create(self):
        data = DocumentSnapshot(None, {"content":"foo", "owner_id":"foobaz"}, True, None, None, None)
        ja = CoverLetter(data)
        assert(ja.content == "foo")
        assert(ja.owner_id == "foobaz")

