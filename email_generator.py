
from groq import Groq


def generate_email(
    api_key,
    recipient,
    purpose,
    email_type,
    tone,
    length,
    additional_info
):
    client = Groq(api_key=api_key)

    system_prompt = """
You are an expert professional email writing assistant.

Rules:
- Write clear and professional emails.
- Do not invent facts or achievements.
- Use only information provided by the user.
- Generate a suitable subject line.
- Return only the subject and email body.
"""

    user_prompt = f"""
Write a professional email using these details:

Recipient: {recipient}

Email Type: {email_type}

Purpose: {purpose}

Tone: {tone}

Length: {length}

Additional Information: {additional_info}

Format your response as:

Subject: <subject>

<email body>
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].message.content
