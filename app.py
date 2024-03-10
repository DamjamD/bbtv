import pandas as pd
import numpy as np
from tqdm import tqdm
from data.geo import Location
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

end_date = datetime.now()  # Today's date
start_date = end_date - timedelta(days=365 * 4) 
content_setups = [
    "10 Tips for Healthy Living",
    "Top 5 Travel Destinations of the Year",
    "Beginner's Guide to Python Programming",
    "Fashion Trends for Spring/Summer",
    "Delicious Recipes for a Weekend Brunch",
    "Mindfulness Meditation Techniques",
    "Latest Tech Gadgets and Innovations",
    "How to Boost Your Productivity",
    "Exploring the Wonders of the Universe",
    "Ultimate Guide to Fitness and Exercise",
    "DIY Home Decor Ideas",
    "Inspirational Quotes for Daily Motivation",
    "Financial Planning for Beginners",
    "Gardening Tips and Tricks",
    "Mastering Photography: Essential Techniques",
    "Effective Communication Skills",
    "Art and Creativity: Unleash Your Potential",
    "The Power of Positive Thinking",
    "Healthy Eating Habits for Weight Loss",
    "Travel Hacks for Budget-Friendly Adventures"
]
content_setup_probs = np.random.dirichlet(np.ones(len(content_setups)))

def new_city(): 
    return Location.random_location()

def generate_fake_data(num_rows):
    data = []
    for _ in range(num_rows):
        location = new_city()
        data.append({
            'Platform': np.random.choice(['YouTube', 'Facebook', 'TikTok', 'Instagram', 'Twitter'], p=[0.4, 0.2, 0.2, 0.1, 0.1]),
            'User_ID': fake.uuid4(),
            'Username': fake.user_name(),
            'Age': int(np.round(np.random.beta(8, 5) * 70 + 1)),
            'Gender': np.random.choice(['Male', 'Female', 'Other'], p=[0.45, 0.45, 0.1]),
            'Language': fake.language_code(),
            'Watch_Time_Minutes': np.random.randint(1, 5000),
            'Most_Viewed_Content': fake.sentence(),
            'Comments': np.random.randint(0, 2),
            'Shares': np.random.randint(0, 2),
            'Likes_Reactions': np.random.randint(0, 2),
            'Followers_Subscribers': np.random.randint(0, 2),
            'Device_Used': np.random.choice(['Mobile', 'Desktop', 'Tablet'], p=[0.6, 0.3, 0.1]),
            'Timestamp' : fake.date_time_between(start_date=start_date, end_date=end_date),
            'Content_Type': np.random.choice(['Video', 'Image', 'Text'], p=[0.4, 0.4, 0.2]),
            'Content_Category': np.random.choice(['Entertainment', 'News', 'Technology', 'Fashion', 'Food', 'Travel'], p=[0.2, 0.2, 0.2, 0.2, 0.1, 0.1]),
            'Referral_Source': np.random.choice(['Direct', 'Search Engine', 'Social Media', 'Referral Link'], p=[0.3, 0.3, 0.2, 0.2]),
            'Monetization': np.random.choice(['Ad Revenue', 'Sponsored Content', 'Affiliate Marketing'], p=[0.6, 0.3, 0.1]),
            'payback':  np.random.uniform(0, 0.05),
            'Content_Setup': np.random.choice(content_setups, p=content_setup_probs),
            'Views': np.random.randint(0, 3),
            'City': location['City'],
            'State': location['State'],
            'Latitude': location['Latitude'],
            'Longitude': location['Longitude'],
            'Country': "Canada"
        })
    return data

num_rows = 564234
df = pd.DataFrame(generate_fake_data(num_rows))
#print(df)
df.to_csv('DATA_SET/fake_data_canada.csv', index=False)
