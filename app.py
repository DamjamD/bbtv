import csv
from faker import Faker
import random
import string
import datetime

fake = Faker()

def generate_fake_data():
    platform_choices = ['YouTube', 'Facebook', 'TikTok']
    content_type_choices = ['video', 'image', 'text']
    gender_choices = ['Male', 'Female', 'Other']
    device_choices = ['mobile', 'desktop', 'tablet']

    for _ in range(100000000):  # Generating 100 million rows
        yield {
            'Platform': random.choice(platform_choices),
            'User ID': ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            'Username': fake.user_name(),
            'Age': random.randint(18, 60),
            'Gender': random.choice(gender_choices),
            'Location': fake.country(),
            'Language': fake.language_code(),
            'Followers/Subscribers': random.randint(0, 1000000),
            'Likes/Reactions': random.randint(0, 100000),
            'Shares/Retweets': random.randint(0, 10000),
            'Comments': random.randint(0, 10000),
            'Engagement Rate': round(random.uniform(0, 10), 2),
            'Content Type': random.choice(content_type_choices),
            'Category': fake.word(),
            'Views': random.randint(0, 10000000),
            'Impressions': random.randint(0, 10000000),
            'Reach': random.randint(0, 10000000),
            'CTR': round(random.uniform(0, 10), 2),
            'Posting Frequency': random.randint(1, 30),
            'Time of Posting': fake.date_time_this_year(),
            'Audience Interests': fake.words(nb=random.randint(1, 5)),
            'Audience Behavior': {
                'Average Watch Time': random.randint(0, 600),
                'Bounce Rate': round(random.uniform(0, 100), 2)
            },
            'External Referral Source': fake.url(),
            'Device Used': random.choice(device_choices),
            'Monetization': {
                'Ad Revenue': round(random.uniform(0, 1000), 2),
                'Sponsored Content Revenue': round(random.uniform(0, 1000), 2),
                'Affiliate Sales': round(random.uniform(0, 1000), 2)
            },
            'User Actions': {
                'Clicks': random.randint(0, 1000),
                'Participation': {
                    'Polls': random.randint(0, 100),
                    'Surveys': random.randint(0, 100),
                    'Live Streams': random.randint(0, 100)
                }
            }
        }

def write_to_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    data_generator = generate_fake_data()
    batch_size = 100000  # Writing data in batches to prevent memory overflow
    for i in range(1, 10001):  # Generating 1 billion rows in batches
        print(f"Generating batch {i}")
        batch_data = [next(data_generator) for _ in range(batch_size)]
        write_to_csv(f'dataset_batch_{i}.csv', batch_data)
