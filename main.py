import ollama
import gradio as gr


def generate(input_text):
    response = ollama.chat(model='codellama', messages=[
  {
    'role': 'user',
    'content': input_text,
  },
],)
    print  (response['message']['content'])
    return(response['message']['content'])
   

iface = gr.Interface(fn=generate, 
                      inputs=gr.Textbox(lines=5, label="enter your query"), 
                      outputs="text")  
iface.launch()

