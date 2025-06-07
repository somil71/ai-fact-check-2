from diffusers import StableDiffusionPipeline
import base64
from io import BytesIO
from dotenv import load_dotenv
import os
import torch
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

def generate_infographic(text):
    try:
        HF_TOKEN = os.getenv("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")
        logger.info("Loading StableDiffusionPipeline...")
        pipe = StableDiffusionPipeline.from_pretrained(
            "stabilityai/stable-diffusion-2-1-base",
            token=HF_TOKEN,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
            use_safetensors=True,
            device_map="balanced"
        )
        logger.info("Enabling sequential CPU offloading...")
        pipe.enable_sequential_cpu_offloading()
        logger.info(f"Generating infographic for text: {text[:100]}")
        image = pipe(f"Infographic about {text[:100]}", num_inference_steps=5).images[0]
        logger.info("Encoding image to base64...")
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        logger.info("Infographic generated successfully.")
        return f"data:image/png;base64,{img_str}"
    except Exception as e:
        logger.error(f"Error generating infographic: {str(e)}")
        return f"Error generating infographic: {str(e)}"