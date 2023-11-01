from fastcore.all import *
from fastai.vision.all import *
import io
import random
import requests
import pandas as pd
import gradio as gr
import duckduckgo_search as ddg
import PIL

learn = load_learner('./model.pkl')


def predictor(img):
    item, _, probs = learn.predict(img)
    response = requests.get(ddg.ddg_images(
        f"{item} pokemon")[random.randint(0, 9)]["image"])
    rand_img = PIL.Image.open(io.BytesIO(response.content))
    df = pd.DataFrame(data=probs.numpy()*100, columns=["%"])
    df.insert(0, "Pokemon", learn.dls.vocab)
    df.sort_values(inplace=True, by="%", ascending=False)
    return f"It's a: {item}!", rand_img, df.head()


gr.Interface(fn=predictor, inputs="image", outputs=[
             "text", gr.Image(height=256), gr.DataFrame(show_label=True)], allow_flagging="never", title="Who's That Pokemon?", live=True).launch()
