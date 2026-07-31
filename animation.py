import streamlit as st
import time


def scanner():

    progress = st.progress(0)

    txt = st.empty()

    stages = [

        "Loading Image",

        "Enhancing",

        "Reading Text",

        "Finding Expiry Date",

        "Checking Print",

        "Detecting Tampering",

        "Generating Report"

    ]

    for i in range(101):

        progress.progress(i)

        if i < 15:
            txt.info(stages[0])

        elif i < 30:
            txt.info(stages[1])

        elif i < 45:
            txt.info(stages[2])

        elif i < 60:
            txt.info(stages[3])

        elif i < 75:
            txt.info(stages[4])

        elif i < 90:
            txt.info(stages[5])

        else:
            txt.success(stages[6])

        time.sleep(0.02)
