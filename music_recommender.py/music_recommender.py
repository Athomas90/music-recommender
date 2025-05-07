import pandas as pd

# Load the clustered dataset
df = pd.read_csv('/Users/andreathomas/Desktop/Tableau dashboard/final_df.csv')

def get_recommendations(artist_name):
    # Find all songs by the artist (case-insensitive)
    artist_songs = df[df['Artist'].str.lower() == artist_name.lower()]

    if artist_songs.empty:
        return [f"No songs found for artist '{artist_name}'"]

    # Find the most representative cluster
    cluster = artist_songs['Cluster'].mode()[0]

    # Filter recommendations: same cluster, different artist
    recommendations = df[
        (df['Cluster'] == cluster) &
        (df['Artist'].str.lower() != artist_name.lower())
    ]

    if recommendations.empty:
        return [f"No similar artists found in the same cluster."]

    return [
        f"{row['Track']} by {row['Artist']}" 
        for _, row in recommendations.sample(n=min(5, len(recommendations))).iterrows()
    ]
