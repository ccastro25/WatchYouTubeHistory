from youtube_transcript_api import YouTubeTranscriptApi
from ytmusicapi import YTMusic
import openai
#pip3 install youtube-transcript-api
#pip3 install --upgrade openai
#pip3 install ytmusicapi
openai.api_key = ''


   
    
    # Log into YouTube Music using the file you created before
ytmusic = YTMusic("headers_auth.json")
    
    # Now, fetch your history:
history = ytmusic.get_history()


url = 'https://www.youtube.com/watch?v=UCGaKvZpJYc'
print(url)

video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {"role": "system", "content": "You are a database computer"},
    {"role": "assistant", "content": "data is stored in JSON {text:'', start:'', duration:''}"},
    {"role": "assistant", "content": str(transcript)},
    {"role": "user", "content": "what are the topics discussed in this video. Provide start time codes in seconds and also in minutes and seconds"}
    #are there any sexual and violent topics disscussed in this video. Provide a list of the topics.
  ]
)
timecode = response["choices"][0]["message"]["content"]

print(timecode)
