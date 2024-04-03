import streamlit as st

def show_about_page():
    st.title("About WhatsApp Chat Analyser")
    
    # Image Section (smaller size)
    st.image("Animation - 1712153318197.gif", caption="WhatsApp Chat Analyser Demo", width=200)

    # Application Description
    st.markdown(
        """
        WhatsApp Chat Analyser is a Streamlit web application designed to analyze WhatsApp chat data.
        """
    )
    
    # Features Section
    st.header("Features")
    st.markdown(
        """
        - Analyze various statistics such as total messages, words, media shared, links shared, etc.
        - View timelines of message activity on a daily and monthly basis.
        - Explore word clouds and most common words used in the chat.
        - Discover the most commonly used emojis.
        - Identify the most active users in the chat.
        """
    )
    
    # How to Use Section
    st.header("How to Use")
    st.markdown(
        """
        1. Upload your WhatsApp chat export file.
        2. Select the user (or choose 'Overall' for aggregate statistics).
        3. Click on "Show Analysis" to view insights and visualizations.
        """
    )
    
    # Creator and GitHub Repository Section
    st.header("Creator and GitHub Repository")
    st.markdown(
        """
        WhatsApp Chat Analyser was created by [Kavaskar]().
        You can find the source code on [GitHub]().
        """
    )

    # Footer Section
    st.markdown(
        """
        ---
        Made with ❤️ by Kavaskar S | Contact: kavaskarsundarmoorthi@gmail.com
        """
    )

if __name__ == "__main__":
    show_about_page()
