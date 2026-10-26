import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

code = """
class UserService:
    def get_user(self, user_id):
        return User.objects.get(id=user_id)
"""

token = encoding.encode(code)

print("token count:",len(token))

