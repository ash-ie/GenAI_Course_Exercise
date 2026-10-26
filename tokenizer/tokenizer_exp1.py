import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

text = "Hello, how are you?"

tokens = encoding.encode(text)

print("Token IDs:",tokens)
print("Token count:",len(tokens))

decoded = encoding.decode(tokens)

print("Decoded:",decoded)
