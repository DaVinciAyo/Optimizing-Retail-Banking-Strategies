import pandas as pd
from src.rfm_engineering import compute_rfm
from src.clustering import perform_clustering
from src.utils import load_data,save_data

def main():

    # Load dataset
    df = pd.read_csv("output/cleaned_bank_data.csv")

    # Compute RFM scores
    rfm_data = compute_rfm(df)


    # Apply clustering
    clustered_data = perform_clustering(rfm_data)


    # Save final output
    save_data(clustered_data, "output/rfm_segmented_customers.csv")
    print("Customer segmentation completed successfully.")

if __name__ == "__main__":
    main()
