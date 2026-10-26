import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

texts = [
    "Hello, how are you?",
    "നിങ്ങൾക്ക് സുഖമാണോ?",
    "Bonjour, comment allez-vous?",
    "¿Cómo estás?",
    "こんにちは",
]

for text in texts:
    tokens = encoding.encode(text)
    print(f"text: {text}")
    print(f"token count: {len(tokens)}")
    print("-" * 40)