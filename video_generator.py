import cv2
import os

import numpy as np
import moviepy.editor as mp

def add_audio_to_video(video_path, audio_path, output_path):
    video = mp.VideoFileClip(video_path)
    audio = mp.AudioFileClip(audio_path)
    final_video = video.set_audio(audio)
    final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Parameters
def generate_video_from_images(image_folder, video_name='output_video.mp4', fps=1):
    # Check if there are any images
    # if not image_folder:
    #     raise ValueError("No images found. Make sure to provide raw image data.")

    # Load the first image to get dimensions
    first_image = cv2.imdecode(np.frombuffer(image_folder[0], np.uint8), cv2.IMREAD_COLOR)
    height, width, _ = first_image.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'H264')  # Codec for .mp4 format
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    # Write each image to the video
    for image_data in image_folder:
        img = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

        # Check if the image was loaded successfully
        if img is None:
            print("Could not load image, skipping.")
            continue

        # Resize the image if needed (optional)
        img = cv2.resize(img, (width, height))

        # Write the image to the video
        video.write(img)

    # Release the video writer
    video.release()
    print(f"Video saved as {video_name}")

if __name__ == "__main__":
    image_folder = '/Users/pranavnarahari/Documents/hinge-ai/sample-images'
    generate_video_from_images(image_folder)
    add_audio_to_video('output_video.mp4', '/Users/pranavnarahari/Documents/hinge-ai/sample-audio.mp3', 'output_video_with_audio.mp4')
