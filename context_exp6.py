import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

with open("dummy.txt", "r", encoding="utf-8") as file:
    text = file.read()

token = encoding.encode(text)

print("character count:",len(text))
print("token count:",len(token))