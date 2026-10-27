import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

question = """
What database does the application use?
"""

context = """
The application is built using FastAPI and React.
The backend uses PostgreSQL as the primary database.
Redis is used for caching.
The application uses JWT authentication.
"""

prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{question}
"""

tokens = encoding.encode(prompt)
print("Prompt tokens:",len(tokens))