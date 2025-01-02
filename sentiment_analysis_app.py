import streamlit as st
from textblob import TextBlob

# Title of the app
st.title("Sentiment Analysis Web App")

# Description
st.write("This app analyzes the sentiment of the text you provide.")

# Input text area
user_input = st.text_area("Enter text to analyze", placeholder="Type something here...")

# Analyze button
if st.button("Analyze Sentiment"):
    if user_input:
        # Perform sentiment analysis
        blob = TextBlob(user_input)
        sentiment_score = blob.sentiment.polarity

        # Determine sentiment category
        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Display results
        st.subheader("Results:")
        st.write(f"Sentiment: **{sentiment}**")
        st.write(f"Sentiment Score: **{sentiment_score:.2f}**")
    else:
        st.error("Please enter some text to analyze!")

# Footer
st.write("Made with ❤️ using Streamlit")
