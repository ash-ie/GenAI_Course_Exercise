import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

base_text = """
Python is a programming language.
FastAPI is a Python web framework.
PostgreSQL is a relational database.
React is a JavaScript library.
"""

for multiplier in [1,10,50,100,500]:
    text = base_text * multiplier
    token = encoding.encode(text)
    print("=" * 50)
    print(f"multiplier: {multiplier}")
    print(f"character count: {len(text)}")
    print(f"token count: {len(token)}")