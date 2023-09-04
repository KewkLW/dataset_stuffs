
# YouTube Transcript Fetcher

## Description

This script fetches transcripts from a given YouTube video URL and saves it as a text file. It utilizes the `youtube_transcript_api` to accomplish this task.

## Requirements

- Python 3.x
- `youtube_transcript_api` package

## Configuration Options

- `video_url`: The URL of the YouTube video for which you want to fetch the transcript.  
  Example: "https://youtu.be/IQefdkl8PfY"
  
- `output_path`: The directory where the transcript text file will be saved.  
  Example: "transcripts/"

- `output_name`: The name of the output text file.  
  Example: "_transcript.txt"

- `INCLUDE_TIMESTAMPS`: Whether to include timestamps in the transcript or not.  
  Options: True or False

- `INCLUDE_FULL_SENTENCES`: Whether to include full sentences in the transcript or not.  
  Options: True or False
  This options is lame right now. I'm working on something better tho. So, like... just don't use it. :) 

## Usage

1. Install the required package by running
```bash
pip install youtube_transcript_api 
```
2. Modify the configuration options according to your needs.
3. Run the script by executing `python youtube.py`.
