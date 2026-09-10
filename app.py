import streamlit as st
import time

st.set_page_config(page_title="Reeda AI Nollywood Maker", page_icon="🎬", layout="centered")

st.title("🎬 Reeda AI Nollywood Creator")
st.subheader("Turn your Nollywood story into AI video - 100% Free")
st.write("---")

prompt = st.text_area(
    "Describe your scene:", 
    placeholder="Example: Nollywood woman crying, finds magic pot, thunder, dramatic music, 9:16",
    height=150
)

col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("Video Style", ["Nollywood Drama", "Comedy", "Action", "Romance"])
with col2:
    duration = st.selectbox("Length", ["8 seconds", "15 seconds"])

if st.button("✨ Generate Video", use_container_width=True):
    if prompt == "":
        st.warning("⚠️ Please type a story first")
    else:
        with st.spinner("Generating your AI video... Please wait 30 seconds"):
            time.sleep(4)
        st.success("✅ Video is ready!")
        st.video("https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")
        st.info("This is a demo video. Real AI generation will connect here later.")

st.write("---")
st.caption("Built by Reeda | Powered by Streamlit | Made in Nigeria 🇳🇬")
