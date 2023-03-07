import os
import webbrowser

def play_music():
    # Get the path of the music directory
    music_path = "/path/to/music/folder"

    # Get a list of all music files in the directory
    music_files = [file for file in os.listdir(music_path) if file.endswith(".mp3")]

    # Check if there are any music files in the directory
    if len(music_files) == 0:
        print("No music files found.")
        return

    # Play a random music file
    random_music = music_files[random.randint(0, len(music_files) - 1)]
    music_file = os.path.join(music_path, random_music)

    # Open the music file in the default media player
    os.startfile(music_file)

def open_media(media):
    # Open the media in the default web browser
    url = f"https://www.youtube.com/results?search_query={media}"
    webbrowser.open_new_tab(url)
