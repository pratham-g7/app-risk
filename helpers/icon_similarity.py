from PIL import Image
import imagehash
import requests
from io import BytesIO

def icon_similarity(icon_url1, icon_url2):
    """
    Compare two app icons from URLs and return similarity (0-1).
    1 = identical, 0 = totally different.
    """
    # Fetch images from URLs
    response1 = requests.get(icon_url1)
    response2 = requests.get(icon_url2)
    
    img1 = Image.open(BytesIO(response1.content))
    img2 = Image.open(BytesIO(response2.content))
    
    # Compute perceptual hashes
    hash1 = imagehash.phash(img1)
    hash2 = imagehash.phash(img2)
    
    max_bits = hash1.hash.size
    distance = (hash1 - hash2) / max_bits
    
    similarity = 1.0 - distance  # 1 = identical, 0 = totally different
    return similarity
