import tiktoken

def calculate_token_breakdown(
        system_prompt: str,
        conversation_history: str,
        user_prompt: str,
        retrieved_context: str
) -> None:
    encoding = tiktoken.get_encoding("cl100k_base")

    system_token = encoding.encode(system_prompt)
    history_token = encoding.encode(conversation_history)
    user_token = encoding.encode(user_prompt)
    retrieved_token = encoding.encode(retrieved_context)

    system_count = len(system_token)
    history_count = len(history_token)
    user_count = len(user_token)
    retrieved_count = len(retrieved_token)

    total_tokens = system_count + history_count + user_count + retrieved_count

    print(f"system tokens: {system_count}")
    print(f"history tokens: {history_count}")
    print(f"user tokens: {user_count}")
    print(f"retrieved tokens: {retrieved_count}")
    print("=" * 50)
    print(f"total tokens: {total_tokens}")

if __name__ == "__main__":
    sample_system = "You are an expert backend engineer assisting with Python and database architecture."
    sample_history = "User: How do I handle atomic transactions in Django?\nAssistant: You can use the transaction.atomic decorator or context manager."
    sample_user = "Can you show me an example using PostgreSQL?"
    sample_context = "[Context: Django's transaction.atomic ensures all database queries within the block succeed or rollback together.]"

    calculate_token_breakdown(
        system_prompt=sample_system,
        conversation_history=sample_history,
        user_prompt=sample_user,
        retrieved_context=sample_context
    )