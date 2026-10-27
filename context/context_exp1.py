import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

texts = [
    "Hello",
    "Hello " * 10,
    "Hello " * 100,
    "Hello " * 500,
    "Hello " * 1000,
    "Hello " * 5000,
]

for text in texts:
    token = encoding.encode(text)
    print("=" * 50)
    print(f"character count: {len(text)}")
    print(f"token count: {len(token)}")
