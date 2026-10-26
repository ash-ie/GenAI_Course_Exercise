import tiktoken

encode = tiktoken.get_encoding("cl100k_base")

text = "Hello, how are you?"

token_ids = encode.encode(text)

for token_id in token_ids:
    token = encode.decode([token_id])
    print(token_id, repr(token))