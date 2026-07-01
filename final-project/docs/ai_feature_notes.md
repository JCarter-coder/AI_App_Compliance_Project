# AI Feature Notes

In this SOT app, I'm using OpenAI via a an API key. To add this feature I installed the 'openai' library.

```
python3 openai
```

Once you create a secret key on the OpenAI platform. Change the `.env.template` file name to `.env` and ensure `.env` is referenced in your `.gitignore` file. Then replace `<YOUR KEY>` to your secret key wrapped in parentheses.

**WARNING** DO NOT EXPOSE YOUR SECRET KEY! 
If you set up your `.gitignore` correctly, your `.env` filename should be grayed out compared to the project filenames in white font.

```python
AI_API_KEY=<YOUR KEY>
```

You can run a simple example file such as this to ensure you are getting a response in your console.

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

AI_API_KEY = os.getenv("AI_API_KEY")

client = OpenAI(
  api_key=AI_API_KEY
)

response = client.responses.create(
  model="gpt-5.4-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text)
```

Currently, my AI App Compliance Project summarizes the filtered personnel table for those in upgrade training.