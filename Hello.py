import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    x = st.slider("Select a value")
    st.write(x, "squared is", x * x)


if __name__ == "__main__":
    run()
