"""
main.py

Draw the UI and connect event listeners to each component using gradio.
"""
import gradio as gr
from helper.helpers import test_func

with gr.Blocks() as demo:
    gr.Markdown("# PromptTemplate Playground")
    with gr.Tab("URLs"):
        url_input = gr.Textbox(placeholder="Enter the URLs to crawl. (Separate with enter if multiple)", lines=2)
    with gr.Tab("Prompt Template"):
        prompt_input = gr.TextArea(placeholder="Enter your prompt")
    testing_button = gr.Button("Testing!")
    with gr.Tab("Result"):
        result_output = gr.Textbox()
    with gr.Accordion("Do you need Help?"):
        gr.Markdown("Contact to kvngho@gmail.com")

    testing_button.click(test_func, inputs=[url_input, prompt_input], outputs=result_output)

demo.launch(server_name="0.0.0.0", server_port=7861)