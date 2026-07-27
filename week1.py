import os
import pandas as pd
from langchain_community.chat_models import ChatOllama

# Load CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "sample_data.csv")

df = pd.read_csv(csv_path)

# Create Local LLM
llm = ChatOllama(
    model="mistral",
    temperature=0
)

print("📊 StatBot Pro - Week 1 (Stable Local Version)")
print("Type 'exit' to quit\n")

while True:
    query = input("Ask a question about the data: ")

    if query.lower() == "exit":
        print("👋 Exiting...")
        break

    try:
        # Create prompt manually
        prompt = f"""
You are a data analyst.
Here is the dataframe preview:

{df.head().to_string()}

User question:
{query}

Answer clearly and directly using the dataframe.
"""

        response = llm.invoke(prompt)

        print("\n✅ Answer:", response.content)
        print("-" * 50)

    except Exception as e:
        print("❌ Error:", str(e))
