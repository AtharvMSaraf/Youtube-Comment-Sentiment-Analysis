from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
from urllib.parse import urlparse, parse_qs
from transformers import pipeline 
import matplotlib.pyplot as plt
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow warnings (1: INFO, 2: WARNING, 3: ERROR)
import tensorflow as tf

api_key = 'AIzaSyBNSiaDz1WKyD2C7oQgORKMncQT8yv4cM8'

def extract_video_id(video_input):
    parsed_url = urlparse(video_input)
    query = parse_qs(parsed_url.query)
    if 'v' in query:
        return query['v'][0]
    else:
        # If 'v' parameter not found, assume video_input is already a video ID
        return video_input

def get_video_comments(video_input, api_key):
    video_id = extract_video_id(video_input)
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        comments = []
        next_page_token = None

        while True:
            response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                pageToken=next_page_token,
                maxResults=100  # Adjust as needed, maximum allowed value is 100
            ).execute()

            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        return comments

    except HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred: {e.content}')

def mode_prediction(comments):
    classifier = pipeline(model='distilbert-base-uncased-finetuned-sst-2-english', revision='af0f99b')
    result = classifier(comments)
    return result

def display_output(predictions):
    positive_comments_count = 0
    negative_comments_count = 0
    positive_comments = []
    for i in predictions:
        if i['label'] == "POSITIVE":
            positive_comments_count+=1
            # positive_comments.append()
        else:
            negative_comments_count+=1

    positive_comment_percentage = (positive_comments_count/(positive_comments_count+negative_comments_count)) * 100

    print('Percent of positive comments: ',positive_comment_percentage, '%')
    print('Number of positive comments: ', positive_comments_count )
    print('Number of negative comments: ', negative_comments_count)
    return positive_comment_percentage, max(positive_comments_count,negative_comments_count)

def create_df(comments,prediction, save_data_bool):
    if(save_data_bool):
        df = pd.DataFrame(columns=['Comments', 'Tag'])
        df['Comments'] = comments
        label_list = []
        for i in prediction:
            label_list.append(i['label'])
        df['Tag']= label_list

        return df
    else:
        pass

def display_visualisation(df,percentage, y_len):
    fig = plt.figure(figsize=[10,10])
    ax = fig.add_subplot()
    ax.hist(df['Tag'])
    ax.set_title('Comment Sentiment Split')
    summary_text = f'Positive Sentiment Percentage = {round(percentage,2)}'
    if(percentage>50):
        color = 'green'
    else:
        color = 'red'
    ax.text(0.3, y_len/2, summary_text, bbox={'facecolor': color, 'alpha': 0.5, 'pad': 10})
    plt.show()

if __name__== "__main__":
    video_input = input("Please paste the video ID or URL: ")
    # video_input = 'https://www.youtube.com/watch?v=XzSlEA4ck2I'
    comments = get_video_comments(video_input, api_key)
    comments_to_be_analysed = comments[:510]
    predictions = mode_prediction(comments[:510])
    percentage, y_len = display_output(predictions)
    save_data_bool = input("Do you want to save the comments with their tags? ")
    df = create_df(comments[:510], predictions, save_data_bool)
    visualiuse_data_bool = input("See vidualisation? ")
    display_visualisation(df, percentage, y_len)



# # Print the comments
# for idx, comment in enumerate(comments, start=1):
#     print(f'Comment {idx}: {comment}')

# Optionally, you can save the comments to a file
# with open('video_comments.json', 'w') as file:
#     json.dump(comments, file)
