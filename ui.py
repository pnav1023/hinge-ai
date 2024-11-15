import streamlit as st
from video_generator import generate_video_from_images, add_audio_to_video
import os

os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
st.title('Hinge AI')

video_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
if video_file is not None:
    st.video(video_file)

image_files = st.file_uploader("Upload pictures", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

options = ["Option 1", "Option 2", "Option 3", "Option 4"]
selected_option = st.selectbox("Choose a voice narrator for your video", options)
st.write(f"You selected: {selected_option}")

text_input = st.text_input("Enter a script for your voice narrator")
if text_input:
    st.write(f"Script: {text_input}")

if st.button("Generate video"):
    image_files = [image_file.read() for image_file in image_files]
    print("UI:", os.getcwd())
    generate_video_from_images(image_files)
    # add_audio_to_video("/mount/src/hinge-ai/output_video.mp4", "sample_audio.mp3","output_video_with_audio.mp4")
    video_bytes = open("/mount/src/hinge-ai/output_video.mp4", "rb").read()
    st.video(video_bytes)
    st.download_button(
        label="Download video",
        data=video_bytes,
        file_name="hinge_video.mp4",
        mime="video/mp4"
    )