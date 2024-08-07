import numpy as np

import gradio as gr

def snap(image):
    return np.flipud(image)

demo = gr.Interface(snap, gr.Image(sources=["webcam"]), "image")

if __name__ == "__main__":
    demo.launch()
