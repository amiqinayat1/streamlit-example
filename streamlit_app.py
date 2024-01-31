import streamlit as st
import cv2
import tempfile
import os

def main():
    st.title("Video Uploader App")
    
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        temp_location = save_uploaded_file(uploaded_file)

        # Display the uploaded video
        display_video(temp_location)

def save_uploaded_file(uploaded_file):
    temp_location = os.path.join(tempfile.gettempdir(), uploaded_file.name)

    with open(temp_location, 'wb') as f:
        f.write(uploaded_file.read())

    return temp_location

def display_video(video_path):
    st.video(video_path)
st.write("this is")

if __name__ == "__main__":
    main()
