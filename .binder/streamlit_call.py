from subprocess import Popen
import os

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    os.chdir('stransfer/')
    Popen(["streamlit", "run", "stransfer.py", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"])
