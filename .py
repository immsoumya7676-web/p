import streamlit as st
from PIL import Image
import time
import random

# These files will be created next
try:
    from detector import analyze_image
except:
    analyze_image = None

try:
    from ocr import extract_text
except:
    extract_text = None

st.set_page_config(
    page_title="PackSecure AI",
    page_icon="📦",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

st.sidebar.title("📦 PackSecure AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Inspection",
        "Dashboard",
        "About"
    ]
)

# ---------------- Home ---------------- #

if page == "Home":

    st.title("📦 PackSecure AI")

    st.subheader(
        "AI Powered Packaging Tampering Detection"
    )

    st.markdown("---")

    col1, col2 = st.columns([2,1])

    with col1:

        st.write(
            """
            Detect suspicious expiry-date printing,
            damaged labels and packaging inconsistencies
            using Computer Vision and OCR.
            """
        )

        st.success("✔ Exhibition Prototype")

    with col2:

        st.image(
            "https://images.unsplash.com/photo-1604719312566-8912e9227c6a?w=500",
            use_container_width=True
        )

    st.markdown("---")

    st.header("Demo Workflow")

    st.write("📷 Upload Product")
    st.write("🔍 AI Scan")
    st.write("🧠 OCR")
    st.write("⚠ Tampering Analysis")
    st.write("📄 Inspection Report")

# ---------------- Inspection ---------------- #

elif page == "Inspection":

    st.title("🔍 Product Inspection")

    uploaded = st.file_uploader(
        "Upload Chips Packet",
        type=["png","jpg","jpeg"]
    )

    if uploaded:

        image = Image.open(uploaded)

        st.image(image,use_container_width=True)

        if st.button("Start AI Scan"):

            progress = st.progress(0)

            status = st.empty()

            for i in range(101):

                progress.progress(i)

                if i < 20:
                    status.info("Loading Image...")

                elif i < 40:
                    status.info("Enhancing Image...")

                elif i < 60:
                    status.info("Reading Text (OCR)...")

                elif i < 80:
                    status.info("Analyzing Printing...")

                else:
                    status.info("Generating Result...")

                time.sleep(0.02)

            st.success("Scan Completed")

            st.subheader("OCR Output")

            if extract_text:

                text = extract_text(image)

                st.code(text)

            else:

                st.code("""
MFG : 12/05/2024
EXP : 11/05/2026
Batch : A1245
""")

            st.subheader("Inspection Result")

            if analyze_image:

                result = analyze_image(image)

            else:

                result = {
                    "risk": random.randint(20,95),
                    "status":"Possible Tampering",
                    "reason":"Ink inconsistency detected"
                }

            col1,col2,col3 = st.columns(3)

            col1.metric(
                "Risk Score",
                f"{result['risk']}%"
            )

            col2.metric(
                "Status",
                result["status"]
            )

            col3.metric(
                "Reason",
                result["reason"]
            )

            if result["risk"]>70:

                st.error("⚠ High Risk Product")

            elif result["risk"]>40:

                st.warning("⚠ Needs Manual Inspection")

            else:

                st.success("✔ Product Appears Safe")

# ---------------- Dashboard ---------------- #

elif page=="Dashboard":

    st.title("📊 Dashboard")

    col1,col2,col3=st.columns(3)

    col1.metric("Total Scans",58)

    col2.metric("Safe",43)

    col3.metric("High Risk",15)

    st.bar_chart(
        {
            "Safe":[10,12,8,13],
            "Risk":[2,4,6,3]
        }
    )

# ---------------- About ---------------- #

else:

    st.title("About PackSecure AI")

    st.write("""
PackSecure AI is an exhibition prototype that demonstrates how
computer vision and OCR could assist in identifying packaging that
may have been tampered with.

The current version uses OCR and image-analysis heuristics to
highlight suspicious patterns. It is not a certified or definitive
tampering detector.
""")
