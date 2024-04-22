import streamlit as st

st.title("Tiktok Stats")

data_dict = {
    "Likes": 1613,
    "Saves": 1613,
    "Comments": 1613,
    "Posts": 31,
    "Follows": 2058
}

cols = st.columns(len(data_dict))

i = 0
for data in data_dict:
    with cols[i]:
        st.metric(data, data_dict[data])
    i += 1