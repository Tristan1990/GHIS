from pathlib import Path
from PIL import Image

folder = Path(r"C:\Users\Silen\OneDrive\Documenten\GHIS\assets\day1")
for img_path in folder.glob("base_*.avif"):          # convert AVIF ➜ PNG
    im = Image.open(img_path)
    im.save(img_path.with_suffix(".png"), format="PNG")
