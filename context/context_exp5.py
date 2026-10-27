import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

def count_tokens(text):
    token = encoding.encode(text)
    return len(token)

while True:
    text = input(str("Enter the text:"))
    if text.lower() == "exit":
        break

    print("characters:",len(text))
    print("tokens:",count_tokens(text))