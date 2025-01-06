import os
from elevenlabs import stream
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('ELEVENLABS_API_KEY')  

print('API key:', api_key)

client = ElevenLabs(api_key=api_key,)

audio_stream = client.text_to_speech.convert_as_stream(
    text="FlightScope i4  Laser  rangefinder is smashing !",
    #voice_id="h91eQmD8oL4DYYdNax7e", # British Female Siobhan
    voice_id="Hhk4ghmoAIzf0c6b5zZg", # Madelein
)

# option 1: play the streamed audio locally
stream(audio_stream)

# option 2: process the audio bytes manually
#for chunk in audio_stream:
#    if isinstance(chunk, bytes):
#        print(chunk)
