from unittest import TestCase

from apptrackr.types import JobApplication

class TestTypes(TestCase):
    def test_JobApplication_create(self):
        ja = JobApplication({"job_description_title":"foo"})
        assert(ja.job_description_title == "foo")

    def test_JobApplication_dict(self):
        ja = JobApplication({"job_description_title":"foo"})
        assert(ja.toJson().find('"job_description_title": "foo"') > 0)