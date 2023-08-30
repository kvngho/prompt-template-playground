"""
main.py

Draw the UI and connect event listeners to each component using gradio.
"""
import gradio as gr
from helper.helpers import test_crwal_func
from helper.ui_helpers import get_tokenizer_list
from playground import PlayGround


with gr.Blocks() as demo:
    gr.Markdown("# PromptTemplate Playground")
    api_key = gr.Textbox(placeholder="Enter the API key", label='APIKEY', show_label=True)
    with gr.Tab("URLs"):
        url_input = gr.Textbox(placeholder="Enter the URLs to crawl. (Separate with enter if multiple)", lines=2, label='URLs', show_label=True)
        crawl_button = gr.Button("Crawl Testing!")
        crawl_output = gr.Textbox(label='Crawl Output', show_label=True)
    with gr.Tab("Prompt Template"):
        prompt_input = gr.TextArea(placeholder="Enter your prompt", label='Prompt Template', show_label=True)
    tokenizer_name = gr.Dropdown(choices=get_tokenizer_list(), label='Tokenizer', show_label=True)
    first_sentence_num = gr.Number(label='Number of Sentences', show_label=True)
    testing_button = gr.Button("Total Testing!")
    with gr.Tab("Result"):
        result_output = gr.Textbox(label='Output', show_label=True)
    with gr.Accordion("Do you need Help?"):
        gr.Markdown("Contact to kvngho@gmail.com")

    # Add event listener
    testing_button.click(fn=PlayGround.start,
                         inputs=[url_input, prompt_input, tokenizer_name, first_sentence_num, api_key],
                         outputs=result_output)
    crawl_button.click(test_crwal_func, inputs=[url_input], outputs=crawl_output)

demo.launch(server_name="0.0.0.0", server_port=7861)