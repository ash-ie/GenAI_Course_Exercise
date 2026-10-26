import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

json_data = """
{
    "name": "Ash",
    "role": "Software Engineer",
    "skills": ["Python", "Django", "FastAPI", "React"]
}
"""

tokens = encoding.encode(json_data)

print("token count:",len(tokens))