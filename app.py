import streamlit as st
import requests
import time

st.set_page_config(page_title="Reeda AI Nollywood Maker", page_icon="🎬")
st.title("🎬 Reeda AI Nollywood Creator")

LUMA_API_KEY = "luma-api-YE-I4xSTXcLlE5c-Xo6FkY3CUGrvRFM41pr3ZmNs-dY"

prompt = st.text_area("Describe your scene:", placeholder="Nollywood woman crying in rain", height=150)

def generate_luma_video(prompt_text):
    headers = {"Authorization": f"Bearer {LUMA_API_KEY}", "Content-Type": "application/json"}
    data = {"prompt": prompt_text + ", nollywood movie style, 9:16", "aspect_ratio": "9:16"}
    response = requests.post("https://api.lumalabs.ai/dream-machine/v1/generations", headers=headers, json=data)
    if response.status_code == 200:
        generation_id = response.json()["id"]
        with st.spinner("Generating REAL AI video... 1-2 mins"):
            while True:
                status = requests.get(f"https://api.lumalabs.ai/dream-machine/v1/generations/{generation_id}", headers=headers).json()
                if status["state"] == "completed": return status["assets"]["video"]
                if status["state"] == "failed": return None
                time.sleep(5)
    return None

if st.button("✨ Generate REAL Video"):
    if prompt: 
        video_url = generate_luma_video(prompt)
        if video_url: st.video(video_url)
        else: st.error("Failed")
    else: st.warning("Type a story first")
