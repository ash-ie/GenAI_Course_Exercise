import tiktoken

encode = tiktoken.get_encoding("cl100k_base")

texts = [
     "Hello",
    "Hello world",
    "Python",
    "Python developer",
    "Django REST Framework",
    "Artificial Intelligence",
    "Generative Artificial Intelligence",
]

for text in texts:
    token = encode.encode(text)
    print(f"text: {text}")
    print(f"tokens: {token}")
    print(f"token ids: {len(token)}")
    print("-" * 40)