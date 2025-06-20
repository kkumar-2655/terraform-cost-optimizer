import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def suggest_alternatives(cost_report):
    prompt = "You are a cloud cost optimization expert. Suggest cheaper alternatives:\n"
    for item in cost_report:
          rtype = item.get("resource", "unknown")
          label = item.get("instance_type", rtype)  # fallback to resource type
          prompt += f"- {item['name']} ({label}): ${item['monthly_cost']:.2f}\n"


    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

