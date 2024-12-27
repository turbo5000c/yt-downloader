import os
import subprocess
from datetime import datetime

# Configuration
DOWNLOAD_FOLDER = "/folder/for/youtube-shows"  # Replace with your Jellyfin media directory
CHANNELS = {
    "Channel-1": "https://www.youtube.com/@Channel-1", # replace with youtube Channel URL
    "Channel-2": "https://www.youtube.com/@Channel-2", # replace with youtube Channel URL
    "Channel-2": "https://www.youtube.com/@Channel-3", # replace with youtube Channel URL
}
MAX_VIDEOS = 5  # Number of latest videos to download per channel
YT_DLP_PATH = "yt-dlp"  # Path to yt-dlp binary

def download_latest_videos(channel_name, channel_url, download_folder, max_videos):
    """
    Downloads videos from the specified YouTube channel, ensuring only the latest max_videos are kept.
    """
    try:
        # Create a subfolder for the channel
        channel_folder = os.path.join(download_folder, channel_name)
        if not os.path.exists(channel_folder):
            os.makedirs(channel_folder)

        # Archive file to track downloaded videos
        archive_file = os.path.join(channel_folder, "downloaded_videos.txt")

        # Count existing files in the folder
        existing_files = [
            f for f in os.listdir(channel_folder) if os.path.isfile(os.path.join(channel_folder, f))
        ]
        num_existing_videos = len(existing_files)

        # Calculate how many videos need to be downloaded
        num_to_download = max(0, max_videos - num_existing_videos)
        if num_to_download == 0:
            print(f"No new videos needed for {channel_name}.")
            return

        # yt-dlp command to download the required number of videos
        command = [
            YT_DLP_PATH,
            "--max-downloads", str(num_to_download),  # Download only the required number of videos
            "--output", f"{channel_folder}/%(title)s.%(ext)s",
            "--format", "bestvideo+bestaudio/best",
            "--no-overwrites",  # Avoid overwriting existing files
            "--download-archive", archive_file,  # Prevent redownloading
            channel_url
        ]

        print(f"Running command: {' '.join(command)}")
        subprocess.run(command, check=True)

        # Manage the folder to ensure only the latest max_videos are kept
        manage_folder(channel_folder, max_videos)

    except Exception as e:
        print(f"Error processing channel {channel_name}: {e}")

def manage_folder(folder, max_videos):
    """
    Deletes the oldest videos in the folder to ensure only max_videos are kept.
    """
    try:
        # Get a list of all files in the folder, sorted by creation time
        files = sorted(
            [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))],
            key=os.path.getctime
        )

        # Remove files if there are more than max_videos
        while len(files) > max_videos:
            oldest_file = files.pop(0)
            os.remove(oldest_file)
            print(f"Deleted oldest file: {oldest_file}")

    except Exception as e:
        print(f"Error managing folder {folder}: {e}")

if __name__ == "__main__":
    print(f"Starting download at {datetime.now()}")

    for channel_name, channel_url in CHANNELS.items():
        print(f"Processing channel: {channel_name}")
        download_latest_videos(channel_name, channel_url, DOWNLOAD_FOLDER, MAX_VIDEOS)

    print(f"Finished download at {datetime.now()}")
