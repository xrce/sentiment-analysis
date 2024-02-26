import csv
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="w11wo/indonesian-roberta-base-sentiment-classifier")

input_file = 'tweet.csv'
output_file = 'sentiment.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    fieldnames = csv_reader.fieldnames + ['Sentiment', 'Sentiment_Score']

    with open(output_file, 'w', newline='', encoding='utf-8') as output_csvfile:
        csv_writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            text = row['Text']

            result = sentiment_pipeline(text)
            sentiment = result[0]['label']
            sentiment_score = result[0]['score']
            
            if sentiment.lower() != 'neutral':
                row['Sentiment'] = sentiment
                row['Sentiment_Score'] = sentiment_score
                csv_writer.writerow(row)
                print(f"[ {sentiment} ] {text}")

print(f"File {output_file} berhasil dihasilkan dengan kolom sentimen dan skor sentimen menggunakan model BERT.")
