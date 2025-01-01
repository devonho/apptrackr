import anthropic


class LLMClient:

    def write(cv, jd, sys):
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
        
        return cover_letter