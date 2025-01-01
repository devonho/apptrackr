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
    
    def chat(messages):
        system_prompt = """ You are an assistant that gives feedback to users about their resume with reference to a job description. """

        client = anthropic.Anthropic()

        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            system=system_prompt,
            messages=messages
        )
        return response.content[0].text
