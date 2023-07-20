import os
import openai
from secretkey import apikey



openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a email for regignation\n\nSubject: Resignation\n\nDear [Name],\n\nI am writing to formally tender my resignation from my position as [Position], effective [date].\n\nI have thoroughly enjoyed my time with [Company], where I have been able to grow and hone my skills while developing meaningful relationships with my colleagues. I am extremely grateful for the opportunity to work here and for the guidance of my supervisors over the years.\n\nI am exceptionally proud of my contributions to [Company], and I have faith that I am leaving the team in capable hands. I wish [Company] and its staff all the best in their future endeavors.\n\nPlease let me know if I can assist in any way during this transition.\n\nSincerely,\n\n[Your Full name]",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)




'''
{
  "id": "cmpl-7Zbg3TVG5T8ZHFiecAOK0cwbNcDqK",
  "object": "text_completion",
  "created": 1688720667,
  "model": "text-davinci-003",
  
  "choices": [
    {
      "text": "",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 165,
    "total_tokens": 165
  }
}
'''

