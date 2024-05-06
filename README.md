YouTube Sentiment Analysis

This Python script analyzes sentiment in YouTube video comments using the YouTube Data API and the Hugging Face Transformers library. It retrieves comments from a specified YouTube video, predicts their sentiment, and visualizes the sentiment distribution.

Features

Retrieves YouTube video comments using the YouTube Data API.
Performs sentiment analysis on comments using a pre-trained model from the Hugging Face Transformers library.
Visualizes the sentiment distribution of comments.
Offers the option to save comment data with their corresponding sentiment tags.
Prerequisites

Before running the script, ensure you have the following installed:

Python 3.x
Required Python packages:
google-api-python-client
transformers
matplotlib
pandas
YouTube Data API key (obtainable from Google Cloud Console)
Installation

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/your-repository.git
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Usage

Run the script:
bash
Copy code
python sentiment_analysis.py
Enter the YouTube video ID or URL when prompted.
Optionally choose to save comment data.
Optionally choose to visualize sentiment distribution.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

The YouTube Data API and Hugging Face Transformers library for providing access to data and pre-trained models.
The contributors to the open-source libraries used in this project.
Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
