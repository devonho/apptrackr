import json

class JobApplication:
    fields = [  "job_description_title", 
                "job_description", 
                "job_description_id", 
                "resume_contents", 
                "resume_id", 
                "cover_letter", 
                "system_prompt",
                "application_status",
                "date_of_application",
                "date_of_status_update"]
    def __init__(self, data):
        for f in JobApplication.fields:
            try:
                setattr(self, f, data[f])
            except KeyError: 
                setattr(self, f, None)

    def toJson(self):
        d = {}
        for f in JobApplication.fields:
            d[f] = getattr(self, f)
        return json.dumps(d)
        