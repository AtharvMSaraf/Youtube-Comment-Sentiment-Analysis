# YouTube Sentiment Analysis

This Python script analyzes sentiment in YouTube video comments using the YouTube Data API and the Hugging Face Transformers library. It retrieves comments from a specified YouTube video, predicts their sentiment, and visualizes the sentiment distribution.

## Features

- Retrieves YouTube video comments using the YouTube Data API.
- Performs sentiment analysis on comments using a pre-trained model from the Hugging Face Transformers library.
- Visualizes the sentiment distribution of comments.
- Offers the option to save comment data with their corresponding sentiment tags.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Required Python packages:
  - google-api-python-client
  - transformers
  - matplotlib
  - pandas
- YouTube Data API key (obtainable from Google Cloud Console)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AtharvMSaraf/Youtube-Comment-Sentiment-Analysis.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python sentiment_analysis.py
    ```

2. Enter the YouTube video ID or URL when prompted.
3. Optionally choose to save comment data.
4. Optionally choose to visualize sentiment distribution.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The YouTube Data API and Hugging Face Transformers library for providing access to data and pre-trained models.
- The contributors to the open-source libraries used in this project.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
