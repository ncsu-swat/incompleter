#Source: https://stackoverflow.com/questions/76052537/attributeerror-clipvisionmodelwithprojection-object-has-no-attribute-get-ima
from pathlib import Path
from lambda_diffusers import StableDiffusionImageEmbedPipeline

from PIL import Image
import torch

#device = "cuda" if torch.cuda.is_available() else "cpu"
device = "cpu"
pipe = StableDiffusionImageEmbedPipeline.from_pretrained("lambdalabs/sd-image-variations-diffusers")
pipe = pipe.to(device)

im = Image.open("/home/cvpr/Desktop/bird.jpg")
num_samples = 4
image = pipe(num_samples*[im], guidance_scale=3.0)
image = image["sample"]

base_path = Path("outputs/im2im")
base_path.mkdir(exist_ok=True, parents=True)
for idx, im in enumerate(image):
    im.save(base_path/f"{idx:06}.jpg")