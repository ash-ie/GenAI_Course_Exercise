import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

conversation = """
User: I am building a CRM application.
Assistant: What technology are you using?
User: FastAPI and React.
Assistant: Which database?
User: PostgreSQL.
User: The application will support multiple firms.
Assistant: Then you should consider multi-tenant architecture.
"""
conversation += """
User: We also need authentication.
Assistant: You can use JWT authentication.
"""

conversation += """
User: We need role-based access control.
Assistant: You can implement RBAC.
"""

token = encoding.encode(conversation)

print(f"character count: {len(conversation)}")
print(f"token count: {len(token)}")