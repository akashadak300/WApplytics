from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import re
import emoji

extract=URLExtract()

def fetch_stats(selected_user,df):
    if selected_user!='Overall':
        df=df[df['user']==selected_user]
    
    # 1. fetch no.of messages
    num_messages= df.shape[0]
    # 2. fetch no of words
    words=[]
    for message in df['message']:
        words.extend(message.split())

    # 3. fetch no of media messages
    num_media_messages=df[df['message']=='<Media omitted>\n'].shape[0]

    # 4. fetch no of links shared
    links=[]
    for message in df['message']:
        links.extend(extract.find_urls(message))

    
    return num_messages,len(words),num_media_messages,len(links)

def most_busy_users(df):
    x=df['user'].value_counts().head(5)
    df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'user':'name','count':'percent'})

    return x,df

# Remove group notifications
# Remove media omitted messages
# Remove stop words
# # removing emojis as creates a nuisance
# def remove_emojis(text):
#     emoji_pattern = re.compile(
#         "["
#         u"\U0001F600-\U0001F64F"  # emoticons
#         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#         u"\U0001F680-\U0001F6FF"  # transport & map symbols
#         u"\U0001F1E0-\U0001F1FF"  # flags
#         u"\U00002700-\U000027BF"  # other symbols
#         u"\U000024C2-\U0001F251"
#         "]+", flags=re.UNICODE)
#     return emoji_pattern.sub(r'', text)

def ceate_wordcloud(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Remove group notifications and media omitted messages
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    # Remove stop words
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = f.read()

    messages = []
    for message in temp['message']:
        filtered_words = [word for word in message.lower().split() if word not in stop_words]
        messages.append(" ".join(filtered_words))

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color="#000000", font_path=None)
    df_wc = wc.generate(" ".join(messages))
    return df_wc

def most_common_words(selected_use,df):
    f=open('stop_hinglish.txt','r')
    stop_words=f.read()

    temp=df[df['user']!='group_notification']
    temp=temp[temp['message']!='<Media omitted>\n']

    words=[]
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df=pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    emojis=[]
    for message in  df['message']:
        emojis.extend([c for c in message if emoji.is_emoji(c)])
    emoji_df=pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df

def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    timeline=df.groupby(['year','month_num','month']).count()['message'].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i]+"-"+str(timeline['year'][i]))
    timeline['time']=time
    return timeline


def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline


def weekly_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    return df['day_name'].value_counts()
    

def monthly_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    return df['month'].value_counts()


def activity_heatmap(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap=df.pivot_table(index='day_name',columns='period',values='message',aggfunc='count').fillna(0)

    return user_heatmap














