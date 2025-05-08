from PIL import Image
from sklearn.cluster import KMeans
import numpy as np


class ImageProcessor:
    def load_image(self, image_path):
        try:
            return Image.open(image_path)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def extract_colors(self, image, num_colors=80):
        # Convert image to RGB if not already in that mode
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Resize image to reduce the number of pixels (optional, for performance)
        image = image.resize((100, 100))
        pixels = np.array(image).reshape(-1, 3)

        # Use K-Means clustering to find the top `num_colors` colors
        kmeans = KMeans(n_clusters=num_colors, random_state=0)
        kmeans.fit(pixels)

        # Get the cluster centers (the representative colors)
        colors = kmeans.cluster_centers_
        return [tuple(map(int, color)) for color in colors]