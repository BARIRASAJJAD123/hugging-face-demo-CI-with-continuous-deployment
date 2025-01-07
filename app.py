from transformers import pipeline
import gradio as gr

# Load the summarization model
model = pipeline("summarization")

def predict(prompt):
    return model(prompt)[0]['summary_text']

# Define the Gradio interface
with gr.Blocks() as demo:
    textbox = gr.Textbox(lines=5, placeholder="Enter text to summarize here...")
    output = gr.Textbox(lines=5, placeholder="Summary will appear here...")
    button = gr.Button("Summarize")

    button.click(predict, inputs=textbox, outputs=output)

demo.launch()
