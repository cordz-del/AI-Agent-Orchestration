// src/context_manager.js
let conversationLog = [];

export function addToConversation(role, message) {
  conversationLog.push({ role, message });
}

export function getContextualPrompt(newUserInput) {
  const history = conversationLog.map(entry => `${entry.role}: ${entry.message}`).join("\n");
  const prompt = `You are Amie, a compassionate SEL assistant.
Conversation History:
${history}
User: ${newUserInput}
Provide a thoughtful, contextual response.`;
  return prompt;
}

// Example usage:
addToConversation("User", "I'm feeling overwhelmed today.");
addToConversation("Assistant", "I'm sorry to hear that. Can you tell me more?");
const prompt = getContextualPrompt("I have an important exam tomorrow.");
console.log("Contextual Prompt:\n", prompt);
