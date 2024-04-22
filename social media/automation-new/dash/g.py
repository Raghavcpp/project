import streamlit as st

st.title("G - Tiktok Stats")

data_dict = {
    "Likes": 100,
    "Saves": 150,
    "Comments": 200,
    "Posts": 4
}

total_likes = 100
total_saves = 150
total_comments = 250
total_posts = 4

cols = st.columns(len(data_dict))

i = 0
for data in data_dict:
    with cols[i]:
        st.metric(data, data_dict[data])
    i += 1