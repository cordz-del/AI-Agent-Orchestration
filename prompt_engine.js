// src/prompt_engine.js
export function buildDynamicPrompt(context, userInput) {
  const basePrompt = `You are Amie, a compassionate SEL assistant.
User context: ${JSON.stringify(context)}
User said: "${userInput}"
Provide supportive and actionable advice.`;
  return basePrompt;
}

// Example usage:
const userContext = { mood: "anxious", previousMessages: ["I have many deadlines."] };
const userInput = "I'm worried about my exam tomorrow.";
const prompt = buildDynamicPrompt(userContext, userInput);
console.log("Dynamic Prompt:", prompt);
