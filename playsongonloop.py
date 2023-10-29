import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import os
import tempfile
from pytube import YouTube
import pygame

import cv2
import moviepy

from moviepy.editor import *


def download_youtube_video(url):
    """Download the YouTube video and return the file path."""
    yt = YouTube(url)
    stream = (
        yt.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
    )
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        stream.download(
            output_path=temp_file.name.rsplit(os.sep, 1)[0],
            filename=temp_file.name.rsplit(os.sep, 1)[1],
        )
        return temp_file.name


def play_video_on_repeat(video_path, repeats=1):
    """Play the video on repeat using moviepy."""
    clip = VideoFileClip(video_path)
    for _ in range(repeats):
        clip.preview()


if __name__ == "__main__":
    # Provide your YouTube video URL here
    YOUTUBE_URL = (
        "https://www.youtube.com/watch?v=-vpFdJbPkYY&ab_channel=TheLatestSounds"
    )
    video_file = download_youtube_video(YOUTUBE_URL)
    play_video_on_repeat(video_file, repeats=10)
    os.remove(video_file)  # remove the downloaded file after playing
