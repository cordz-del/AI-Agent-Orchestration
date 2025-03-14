# prompt_chaining_example.py
def build_dynamic_prompt(context, user_input):
    context_str = " | ".join([f"{key}: {value}" for key, value in context.items()])
    base_prompt = (
        "You are Amie, a compassionate SEL assistant.\n"
        f"Context: {context_str}\n"
        f"User says: '{user_input}'\n"
        "Provide clear, empathetic, and actionable advice."
    )
    return base_prompt

# Example usage:
context = {"mood": "anxious", "prior_message": "I have too many deadlines."}
user_input = "I'm nervous about my upcoming exam."
prompt = build_dynamic_prompt(context, user_input)
print("Dynamic Prompt:\n", prompt)
