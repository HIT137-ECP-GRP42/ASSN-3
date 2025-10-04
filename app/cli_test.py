from model import text_model, image_model
from PIL import Image
from pathlib import Path

print("=== Text generation ===")
print(text_model.run("Write a short poem about the Darwin wet season:", max_new_tokens=20))

print("\n=== Image classification ===")
img_path = Path("test.jpg")
if img_path.exists():
    preds = image_model.run(Image.open(img_path).convert("RGB"))
    for p in preds:
        print(f"{p['label']}: {p['score']:.3f}")
else:
    print("No test.jpg found, skipping image classification.")
