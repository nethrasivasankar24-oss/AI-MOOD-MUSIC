# emotion_music.py

# Map emotions to Spotify playlist URLs
emotion_playlists = {
    "happy": {
        "en": "https://open.spotify.com/playlist/7wQFYPk5p3Hr7nd4M5J1s7?si=voO5ESaFQPqE0H5n4zsR-Q&pi=VmNBDKoCRK-gd",   # English Happy/Pop
        "hi": "https://open.spotify.com/playlist/6MTRZiXtYzTCAvbVX7kOfI?si=urKkrANmR8e1fjqF04nuUg&pi=RZuAfQ2RTKmfN",   # Hindi Happy
        "ko": "https://open.spotify.com/playlist/5IDyeTcTkLCbXrnLFDG5Hr?si=LenQ_rjlShevhe4HOzAs4g",   # K-pop Happy
        "ta": "https://open.spotify.com/playlist/37i9dQZF1DX4Im4BTs2WMg?si=2dnVP9uDQlG6HVHqhl24og",    # Tamil Happy (example)
    },
    "sad": {
        "en": "https://open.spotify.com/playlist/25ZzkJkOuYir9kHr2CqwPQ?si=eiXLrKbWS3KnUYwW8gDO5A",   # English Sad
        "hi": "https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT?si=GBKcmV5FRQCsnn34yy4ulw",   # Hindi Sad
        "ko": "https://open.spotify.com/playlist/6YfrWSdPlykyJRwvbqk86w?si=mL0fx87WRFWQbFHogDJmpQ",   # K-pop Sad
        "ta": "https://open.spotify.com/playlist/0AyOLKzLZZmlliok7bu1mp?si=w_H_TAvZQW2oYD8IF5cxBQ",    # Tamil Sad (example)
    },
    "angry": {
        "en": "https://open.spotify.com/playlist/7L4qbPDXElR0sw75vLJobW?si=ThVCbik-Q9uSAPevSj2_YQ",   # English Angry/Rock
        "hi": "https://open.spotify.com/playlist/5cwtgqs4L1fX8IKoQebfjJ?si=8ZBMV0xoT5aabUJPdn8uIA",   # Hindi Angry
        "ko": "https://open.spotify.com/playlist/1AXlvvhsf6InfWjADV2zDd?si=dSmqjsAQT7y_HER3wc9rWQ",   # K-pop Angry
        "ta": "https://open.spotify.com/playlist/3p8ejB7BscAVmEdyK7AtXx?si=xkO4S0FbRuOh58YHUgp8bg",    # Tamil Angry (example)
    },
    "neutral": {
        "en": "https://open.spotify.com/playlist/6cX5Ev5Piq7DpPJNzicXl5?si=5EJI2IhmSWaOr7fIgDgA8g",   # English Chill
        "hi": "https://open.spotify.com/playlist/1QbJym8B3Xb6rpXdk7MBiJ?si=hatqehoaTjGA8F0mST5Z4w",   # Hindi Chill
        "ko": "https://open.spotify.com/playlist/1nUBL4tv7IrNko4wxHycA1?si=jXVuZiRpT6y-hNO8H9pSWA",   # K-pop Chill
        "ta": "https://open.spotify.com/playlist/5nG3U5u6Q7Zcl8mjkrqHpX?si=mtRXpI_uSXi5P8tAwe475A",    # Tamil Chill (example)
    }
}

# Function to get playlist URL based on emotion & language
def get_playlist(emotion, language):
    if emotion not in emotion_playlists:
        emotion = "neutral"
    return emotion_playlists[emotion].get(language, emotion_playlists[emotion]["en"])