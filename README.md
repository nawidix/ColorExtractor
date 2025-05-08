# Color Extractor

This project is designed to extract dominant colors from an image, convert them to hexadecimal format, and save the results in a text file.

## Project Structure

```
color-extractor
├── src
│   ├── main.py
│   ├── utils
│   │   └── color_utils.py
│   └── services
│       └── image_processor.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/nawidix/ColorExtractor.git
   cd color-extractor
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place the image you want to analyze in the project directory.

2. Run the application:
   ```
   python src/main.py <image-file-path>
   ```

3. The extracted colors will be saved in a file named `colors.txt` in the project directory.

## Dependencies

- Pillow: A Python Imaging Library that adds image processing capabilities to your Python interpreter.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.
