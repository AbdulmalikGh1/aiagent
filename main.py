import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompt import system_prompt


def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY is missing")

    # Create a client pointed at OpenRouter so the request goes to the right API.
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    

    # Take the prompt from the user using argparse.
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Ask the model using the prompt the user actually passed on the command line.
    messages=[
            {"role": "system", "content": system_prompt},
            { "role": "user", "content": args.user_prompt},
        ]
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
    )

    # The API should return usage data; if it doesn't, the request likely failed.
    if response.usage is None:
        raise RuntimeError("Chat completion did not include usage information")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    else:
        print(response.choices[0].message.content)



if __name__ == "__main__":
    main()
