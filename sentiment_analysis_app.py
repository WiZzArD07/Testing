# import streamlit as st
# from textblob import TextBlob

# # Title of the app
# st.title("Sentiment Analysis Web App")

# # Description
# st.write("This app analyzes the sentiment of the text you provide.")

# # Input text area
# user_input = st.text_area("Enter text to analyze", placeholder="Type something here...")

# # Analyze button
# if st.button("Analyze Sentiment"):
#     if user_input:
#         # Perform sentiment analysis
#         blob = TextBlob(user_input)
#         sentiment_score = blob.sentiment.polarity

#         # Determine sentiment category
#         if sentiment_score > 0:
#             sentiment = "Positive"
#         elif sentiment_score < 0:
#             sentiment = "Negative"
#         else:
#             sentiment = "Neutral"

#         # Display results
#         st.subheader("Results:")
#         st.write(f"Sentiment: **{sentiment}**")
#         st.write(f"Sentiment Score: **{sentiment_score:.2f}**")
#     else:
#         st.error("Please enter some text to analyze!")

# # Footer
# st.write("Made with ❤️ using Streamlit")

import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import numpy as np

# Title of the app
st.title("Sentiment Analysis Web App")

# Description
st.write("This app analyzes the sentiment of the text you provide and visualizes the results.")

# Placeholder for storing sentiment trends
data = []

# Input text area
user_input = st.text_area("Enter text to analyze", placeholder="Type something here...")

# Analyze button
if st.button("Analyze Sentiment"):
    if user_input:
        # Perform sentiment analysis
        blob = TextBlob(user_input)
        sentiment_score = blob.sentiment.polarity
        subjectivity_score = blob.sentiment.subjectivity

        # Determine sentiment category
        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Append data for trends
        data.append({"text": user_input, "sentiment": sentiment, "score": sentiment_score})

        # Display results
        st.subheader("Results:")
        st.write(f"Sentiment: **{sentiment}**")
        st.write(f"Sentiment Score: **{sentiment_score:.2f}**")
        st.write(f"Subjectivity Score: **{subjectivity_score:.2f}**")

        # Visualization: Sentiment Score
        st.subheader("Sentiment Score Visualization")
        fig, ax = plt.subplots()
        ax.bar(["Sentiment Score"], [sentiment_score], color="blue")
        ax.set_ylim([-1, 1])
        ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
        ax.set_ylabel("Score")
        st.pyplot(fig)

        # Visualization: Subjectivity Score
        st.subheader("Subjectivity Score Visualization")
        fig, ax = plt.subplots()
        ax.pie([subjectivity_score, 1 - subjectivity_score], labels=["Subjective", "Objective"], autopct="%1.1f%%", colors=["orange", "green"])
        st.pyplot(fig)

        # Sentiment Trends
        st.subheader("Sentiment Trends")
        if len(data) > 1:
            trend_data = pd.DataFrame(data)
            fig, ax = plt.subplots()
            ax.plot(trend_data.index, trend_data['score'], marker='o', color='blue', label='Sentiment Score')
            ax.axhline(0, color='black', linewidth=0.5, linestyle="--")
            ax.set_ylabel("Score")
            ax.set_xlabel("Entries")
            ax.legend()
            st.pyplot(fig)

        # Insights: Pie Chart
        st.subheader("Sentiment Distribution")
        sentiment_counts = pd.DataFrame(data)["sentiment"].value_counts()
        fig, ax = plt.subplots()
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", colors=["green", "grey", "red"])
        st.pyplot(fig)

        # Feedback Analysis: Word Cloud
        st.subheader("Word Cloud of Feedback")
        all_text = " ".join([d['text'] for d in data])
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_text)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

    else:
        st.error("Please enter some text to analyze!")

# Footer
st.write("Made with ❤️ using Streamlit")

