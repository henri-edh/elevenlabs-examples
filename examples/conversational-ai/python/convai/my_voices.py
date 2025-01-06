import os
from elevenlabs import stream
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('ELEVENLABS_API_KEY')  

print('API key:', api_key)

client = ElevenLabs(api_key=api_key,)

response = client.voices.get_all()
audio = client.generate(text="Hello there!", voice=response.voices[0])
print(response.voices)