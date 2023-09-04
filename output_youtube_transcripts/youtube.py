import os

video_url = "https://youtu.be/IQefdkl8PfY"
output_path = "transcripts/"
output_name = "_transcript.txt"

INCLUDE_TIMESTAMPS = True  
INCLUDE_FULL_SENTENCES = False

from youtube_transcript_api import YouTubeTranscriptApi

def fetch_youtube_transcript(video_id):

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    formatted_transcript = ""
    current_sentence = ""
    for entry in transcript:
        text = entry['text']
        
        if INCLUDE_FULL_SENTENCES:
            if text.endswith((".", "!", "?")):
                current_sentence += text
                if INCLUDE_TIMESTAMPS:
                    start = entry['start']
                    formatted_transcript += f"[{start:.2f}] {current_sentence}\n"
                else:
                    formatted_transcript += f"{current_sentence}\n"
                current_sentence = ""
            else:
                current_sentence += " " + text
        else:
            if INCLUDE_TIMESTAMPS:
                start = entry['start']
                formatted_transcript += f"[{start:.2f}] {text}\n"
            else:
                formatted_transcript += f"{text}\n"

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    with open(f"{output_path}/{video_id}{output_name}", "w") as f:
        f.write(formatted_transcript)

if __name__ == "__main__":
    video_id = video_url.split("/")[-1].split("=")[-1]
    fetch_youtube_transcript(video_id)