system_message = """You are a highly skilled career assistant and expert resume writer.
Your task is to generate two different versions of a professional, well-structured Cover 
Letter based on a given Job Description and Resume.
Each Cover Letter must be tailored to the Job Description, highlight the candidate's 
relevant skills and experiences, and maintain a formal, enthusiastic, and confident tone.
Ensure that the two versions differ in wording, structure, or style while both remaining professional
and appropriate for job applications."""

def generate_prompt(job_desc, resume):
    prompt = f"""
You are tasked with writing two different professional Cover Letters based on the provided information.

Here is the Job Description:
\"\"\"
{job_desc}
\"\"\"

Here is the Candidate's Resume:
\"\"\"
{resume}
\"\"\"

Instructions:
- Create two different versions of a Cover Letter.
- Each Cover Letter must be tailored specifically to the Job Description.
- Highlight the candidate’s most relevant skills, experience, and achievements that match the Job Description.
- Use a formal, confident, and enthusiastic tone.
- Ensure that the structure includes a professional greeting, an engaging introduction, a detailed body section focusing on skills and experiences, and a polite and strong closing statement.
- Make sure the two versions are distinct in terms of writing style, wording, or structure while both being suitable for job applications.
- The cover letter should include the candidate's name, address, email, and phone number as found in the resume (if provided).
- If any field such as the name is missing, generate a placeholder and ensure that it is filled in correctly in the output.
- Keep each Cover Letter concise (preferably between 250 to 350 words).
- Avoid generic phrases; focus on personalization based on the job description.
- If possible, incorporate keywords from the Job Description naturally into the content.

Format the output clearly:
- Start each Cover Letter with **Cover Letter 1:** and **Cover Letter 2:** labels.

Begin when ready.
"""
    return prompt
