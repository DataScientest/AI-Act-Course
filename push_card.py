from huggingface_hub import ModelCard
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_TOKEN")

card = ModelCard.load("model_card.md")
card.push_to_hub(
    repo_id="anamvg/exo-chap2",
    token=token
)

print("Model Card successfully published on the Hugging Face Hub!")