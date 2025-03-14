# context_injection_example.py
conversation_log = []

def add_to_conversation(role, message):
    conversation_log.append(f"{role}: {message}")

def build_contextual_prompt(new_user_input):
    history = "\n".join(conversation_log)
    prompt = (
        "You are Amie, a compassionate SEL assistant.\n"
        "Conversation History:\n" + history + "\n"
        f"User: {new_user_input}\n"
        "Provide a supportive and coherent response."
    )
    return prompt

# Example usage:
add_to_conversation("User", "I'm feeling overwhelmed with my workload.")
add_to_conversation("Assistant", "I'm here to help. What specifically is causing you stress?")
prompt = build_contextual_prompt("I have a major exam tomorrow and feel unprepared.")
print("Contextual Prompt:\n", prompt)
