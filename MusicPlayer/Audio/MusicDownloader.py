# Import the pytube library
import pytube

# Set the URL of the YouTube video
url = "https://youtube.com/playlist?list=PLeZl_MM2q5nEkTmqm7cnDZzIZEEF0NPdP"

# Create a Playlist object using the URL
playlist = pytube.Playlist(url)

# Iterate through the videos in the playlist
for video in playlist:
    # Create a YouTube object using the video's URL
    yt = pytube.YouTube(video)

    # Get the first audio stream for the video
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio file to the current directory
    audio_stream.download(output_path="C:\Users\James\Music\MusicPlayer\Audio\MusicDownloader\Audio")