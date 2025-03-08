# pip install pytube moviepy
import os
from pytube import YouTube
from moviepy import AudioFileClip

def download_youtube_audio(url, output_path="output.mp3"):
    try:
        # Download the YouTube video
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        downloaded_file = video.download(output_path=".")

        # Convert the downloaded file to MP3
        audio_clip = AudioFileClip(downloaded_file)
        audio_clip.write_audiofile(output_path)

        # Clean up the original downloaded file
        audio_clip.close()
        os.remove(downloaded_file)

        print(f"Audio successfully downloaded and saved as {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the YouTube URL from the user
    youtube_url = input("Enter the YouTube URL: ")

    # Specify the output file name (optional)
    output_file = input("Enter the output file name (default: output.mp3): ") or "output.mp3"

    # Download and convert the audio
    download_youtube_audio(youtube_url, output_file)