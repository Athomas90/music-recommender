import pandas as pd

# Load the clustered dataframe (must be saved in the same folder)
df = pd.read_csv("final_df.csv")

def get_recommendations(artist_name):
    # Case-insensitive match
    artist_songs = df[df['Channel'].str.lower() == artist_name.lower()]

    if artist_songs.empty:
        return [f"No songs found for artist '{artist_name}'"]

    # Find the most common cluster
    cluster = artist_songs['Cluster'].mode()[0]

    # Recommend other tracks from same cluster, excluding original artist
    recommendations = df[
        (df['Cluster'] == cluster) & 
        (df['Channel'].str.lower() != artist_name.lower())
    ]

    if recommendations.empty:
        return [f"No similar artists found in the same cluster."]

    return [
        f"{row['Track']} by {row['Channel']}" 
        for _, row in recommendations.sample(n=min(5, len(recommendations))).iterrows()
    ]
