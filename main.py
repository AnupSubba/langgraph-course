from dotenv import load_dotenv
import os

load_dotenv()


if __name__ == "__main__":
    print("Hello World, from langgraph")
    print(os.getenv("OPENAI_API_KEY"))