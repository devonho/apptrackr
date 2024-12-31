import anthropic

from apptrackr.db import DB

class LLMClient:

    def write(cv, jd, sys, save_to_DB=False):
        client = anthropic.Anthropic()

        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system=sys,
            messages=[
            {"role": "user", "content": f"Resume:\n {cv} "},
            {"role": "user", "content": f"Job Description\n {jd}"}],
        )

        cover_letter = {
            "resume": cv,
            "job_description": jd,
            "system_prompt": sys,
            "cover_letter": response.content[0].text
        }

        if ( save_to_DB):
            DB.createApplication(cover_letter)
        
        return cover_letter