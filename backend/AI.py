from openai import OpenAI
from dotenv import load_dotenv
import os

#Practices for API Key Safety in powershell
#Enter the following request in powershell with your key:  setx OPENAI_API_KEY your_api_key_here
# api_key=os.environ.get("OPENAI_API_KEY"),

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key = os.getenv("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
            # "content": "I will send you an array of the X circle game. I would be happy if you could play with me and return to me each time an array with an additional circle that you chose to insert into the array",
            # "content": "['X', 'O', '', '', 'X', '', '', '', '']"
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)
