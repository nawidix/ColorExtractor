# Color Extractor

Color Extractor is a Python-based application that can extract and sort colors from an image file. The extracted colors are saved in a `colors.txt` file.

## Features
- Extract colors from an image file.
- Sort colors by brightness (lightest to darkest).
- Save extracted colors in HEX format to a text file.
- Simple and user-friendly GUI built with Tkinter.

## Requirements
- Python 3.7 or higher
- Required Python libraries (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nawidix/ColorExtractor.git
   cd ColorExtractor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python src/main.py
   ```

2. Use the GUI to:
   - Select an image file.
   - Specify the number of colors to extract.
   - View the progress of the extraction process.
   - Open the `colors.txt` file to see the extracted colors.

## File Structure
```
ColorExtractor/
├── src/
│   ├── main.py
│   ├── utils/
│   │   └── color_utils.py
│   ├── services/
│   │   └── image_processor.py
├── requirements.txt
└── README.md
```

## Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## License
Free License.

---

Made by: @NAWIDX
