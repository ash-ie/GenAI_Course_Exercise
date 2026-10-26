import tiktoken

encoding = tiktoken.get_encoding('cl100k_base')

code = """
def calculate_sum(a, b):
    return a+b
"""

tokens = encoding.encode(code)

print("token count:",len(tokens))

for token_id in tokens:
    decoding = encoding.decode([token_id])
    print(repr(decoding))