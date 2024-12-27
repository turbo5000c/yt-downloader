# YouTube Channel Video Downloader Script

This Python script downloads the latest videos from specified YouTube channels, ensures only new videos are downloaded, and maintains a maximum of 5 videos per channel by automatically deleting the oldest ones.

## Features

- Downloads videos from multiple YouTube channels.
- Ensures no duplicate downloads using `yt-dlp`'s `--download-archive` feature.
- Maintains a maximum of 5 videos per channel by automatically deleting older videos.
- Allows specifying video quality (default: up to 1080p).

## Requirements

- Python 3.6 or later
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)

## Installation

1. Clone the repository or download the script.
2. Install `yt-dlp`:
```
pip install yt-dlp
```
3. Ensure you have write access to the folder where videos will be downloaded.

## Configuration

### 1. Set Your Download Folder
Update the `DOWNLOAD_FOLDER` variable in the script to the folder where videos should be saved. For example:
```
DOWNLOAD_FOLDER = "/path/to/smb/folder"
```

### 2. Add YouTube Channels
Update the `CHANNELS` dictionary with the YouTube channels you want to download videos from:
```
CHANNELS = {
    "ChannelName1": "https://www.youtube.com/c/YourChannelName1",
    "ChannelName2": "https://www.youtube.com/c/YourChannelName2"
}
```

### 3. Adjust Video Quality (Optional)
By default, the script downloads videos up to 1080p resolution. To change this, modify the `--format` option in the script:
```
"--format", "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
```

## Usage

Run the script using Python:
```
python video_downloader.py
```

### First Run
On the first run, the script will download up to 5 videos per channel (or fewer if less are available).

### Subsequent Runs
The script will:
- Download only new videos (those not already downloaded).
- Delete the oldest videos to maintain the 5 most recent ones in each channel folder.

## Troubleshooting

### Lower Quality Videos Are Downloaded
Check the available formats for a sample video:
```
yt-dlp -F https://www.youtube.com/watch?v=VIDEO_ID
```
Update the `--format` option in the script to match your desired quality.

### Script Does Not Download New Videos
Ensure the `downloaded_videos.txt` archive file is not corrupted or empty. This file is located in each channel's folder.

### Permission Issues with SMB Folder
Verify that the user running the script has write access to the download folder:
```
sudo chmod -R 755 /path/to/smb/folder
```

## License

This script is open-source and can be modified or redistributed under the [MIT License](LICENSE).
