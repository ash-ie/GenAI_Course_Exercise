import tiktoken

encode = tiktoken.get_encoding("cl100k_base")

texts = [
    "cat",
    "developer",
    "development",
    "internationalization",
    "misunderstanding",
    "electromagnetism",
]

for text in texts:
    token = encode.encode(text)
    print(f"text: {text}")
    print(f"token ids: {token}")
    print(f"token count: {len(token)}")
    print("-" * 40)