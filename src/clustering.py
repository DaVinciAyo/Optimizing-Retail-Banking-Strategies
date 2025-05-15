import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def perfrom_clustering(rfm_df, n_clusters=4):
    features = ['Recency', 'Frequency', 'Monetary']
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_df[features])


    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    rfm_df['Cluster'] = kmeans.fit_predict(rfm_scaled)
    
    return rfm_df
