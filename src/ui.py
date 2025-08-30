import streamlit as st
from src.preprocessing import denoise_image, enhance_contrast, detect_edges
from src.utils import load_image



def run_app():
    st.set_page_config(
        page_title="MedImage Enhancer", layout="wide"
    )  # Wide layout for responsiveness
    st.title("🩺 MedImage Enhancer 🔍")

    uploaded = st.file_uploader(
        "Upload a medical image",
        type=[
            "png",
            "jpg",
            "jpeg",
        ],
    )

    if uploaded:
        image = load_image(uploaded)
        st.image(image, caption="Original", width="stretch", channels="GRAY")

        # Mobile-friendly collapsible controls
        with st.expander("Enhancement Settings"):
            blur_ksize = st.slider(
                "Gaussian Blur Kernel Size",
                min_value=1,
                max_value=15,
                step=2,
                value=5,
                help="Adjust kernel size for noise removal",
            )
            canny_low = st.slider(
                "Canny Edge - Low Threshold",
                min_value=50,
                max_value=200,
                value=100,
                help="Lower threshold for edge detection",
            )
            canny_high = st.slider(
                "Canny Edge - High Threshold",
                min_value=100,
                max_value=300,
                value=200,
                help="Higher threshold for edge detection",
            )

        # Processing
        denoised = denoise_image(image, ksize=blur_ksize)
        enhanced = enhance_contrast(denoised)
        edges = detect_edges(enhanced, low_thresh=canny_low, high_thresh=canny_high)

        # Display results in columns (stacked automatically on mobile)
        cols = st.columns(3)
        cols[0].image(denoised, caption="Denoised", width="stretch", channels="GRAY")
        cols[1].image(
            enhanced, caption="Contrast Enhanced", width="stretch", channels="GRAY"
        )
        cols[2].image(edges, caption="Edges", width="stretch", channels="GRAY")
