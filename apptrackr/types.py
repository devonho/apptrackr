import json
from datetime import datetime
from google.cloud.firestore_v1.base_document import DocumentSnapshot

class BaseType:
    collection_name = ""

    def __init__(self, data, fields, collection_name):
        self.fields = ["owner_id", "date_of_creation", "date_of_update"]
        self.fields += fields
        self.setup(data)
        BaseType.collection_name = collection_name

    def setup(self, data):
        for f in self.fields:
            try:
                if type(data) == DocumentSnapshot:
                    val = data.get(f)
                    setattr(self, "document_id", data.reference.path.split("/")[1])
                else:
                    val = data[f]
            except KeyError: 
                val = None
            
            # if "date" == f[0:4]:
            #     try:
            #         val = datetime.strptime(val, "%Y%m%dT%H:%M:%SZ")
            #     except ValueError:
            #         val = None
            #     except TypeError:
            #         val = None

            setattr(self, f, val)


    def toDict(self):
        d = {}
        for f in self.fields:
            d[f] = getattr(self, f)
        return d

    def toJson(self):
        d = self.toDict()
        return json.dumps(d)


class JobApplication(BaseType):
    def __init__(self, data):
        super().__init__(data,
            ["job_description_title", 
            "job_description",
            "job_description_id", 
            "role_title",
            "role_organization",            
            "resume_contents", 
            "resume_id", 
            "cover_letter", 
            "system_prompt",
            "application_status",
            "date_of_application",
            "date_of_status_update"],
            "applications"
        )

class Resume(BaseType):
    def __init__(self, data):
        super().__init__(data, 
            ["content",
            "title"],
            "resumes"
        )

class CoverLetter(BaseType):
    def __init__(self, data):
        super().__init__(data, 
            ["content",
            "title"],
            "cover_letters"
        )

class JobDescription(BaseType):
    def __init__(self, data):
        super().__init__(data, 
            ["content",
            "role_title",
            "role_organization",
            "recruiter_organization"],
            "job_descriptions"
        )        

class SystemPrompt(BaseType):
    def __init__(self, data):
        super().__init__(data, 
            ["content",
            "title"],
            "system_prompts"
        )

class Username(BaseType):
    def __init__(self, data):
        super().__init__(data, 
            ["username",
            "email",
            "first_name",
            "last_name"],
            "usernames"
        )        