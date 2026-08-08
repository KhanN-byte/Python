"""
Chat with a local Ollama model.
"""

from ollama import chat, list as list_models, pull


class LocalAI:
    def __init__(self, model):
        self.model = model
        self.messages = []

    def ask(self, prompt):
        """Send a prompt and retain the chat history."""
        prompt = prompt.strip()
        if not prompt:
            raise ValueError("Prompt cannot be empty.")

        self.messages.append({"role": "user", "content": prompt})

        try:
            response = chat(model=self.model, messages=self.messages)
        except Exception:
            self.messages.pop()
            raise

        answer = response.message.content
        self.messages.append({"role": "assistant", "content": answer})
        return answer

    def clear(self):
        """Clear the chat history."""
        self.messages.clear()


def ensure_model_installed(model):
    """Download the selected model if it is missing."""
    try:
        installed_models = {
            installed.model for installed in list_models().models
        }
    except Exception as error:
        print(f"\nCould not connect to Ollama: {error}")
        print("Start Ollama, then run this program again.")
        return False

    if model in installed_models:
        return True

    print(f"\nThe model '{model}' is not installed in Ollama.")
    answer = input(f"Download it with 'ollama pull {model}'? (y/n)\n> ").strip()
    if answer.lower() not in {"y", "yes"}:
        print("Model download cancelled.")
        return False

    try:
        print(f"Downloading {model}. Large models may take a while...")
        pull(model)
        print(f"Model '{model}' installed successfully.")
        return True
    except Exception as error:
        print(f"Could not install model: {error}")
        return False


def main():
    available_models = {
        "1": "qwen3.5:9b",
        "2": "qwen3:14b",
        "3": "deepseek-r1:14b",
        "4": "gemma3:12b",
        "5": "gpt-oss:20b",
    }

    print("\nAvailable Models:")
    print("1. Qwen 3.5 9B")
    print("2. Qwen 3 14B")
    print("3. DeepSeek R1 14B")
    print("4. Gemma 3 12B")
    print("5. GPT-OSS 20B")

    while True:
        choice = input(
            "\nEnter a menu number or an exact Ollama model name:\n> "
        ).strip()
        if choice:
            model = available_models.get(choice, choice)
            break
        print("Please enter a model number or model name.")

    if not ensure_model_installed(model):
        return

    ai = LocalAI(model)

    print(f"\nChatting with Ollama model: {ai.model}")
    print("Ask anything. Enter /clear to reset or /exit to quit.")

    while True:
        try:
            prompt = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if prompt.lower() in {"/exit", "exit", "quit"}:
            print("Goodbye!")
            break

        if prompt.lower() == "/clear":
            ai.clear()
            print("Conversation cleared.")
            continue

        if not prompt:
            continue

        try:
            print(f"\nAI: {ai.ask(prompt)}")
        except Exception as error:
            print(f"\nError: {error}")
            print("Make sure Ollama is running and the model is installed.")


if __name__ == "__main__":
    main()
