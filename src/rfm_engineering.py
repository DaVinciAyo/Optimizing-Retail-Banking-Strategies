import pandas as pd

def compute_rfm(data):
    reference_date = data['TransactionDate'].max()
    
    rfm = data.groupby('CustomerID').agg({
        'TransactionDate': lambda x: (reference_date - x.max()).days,
        'TransactionID': 'count',
        'TransactionAmount (INR)': 'sum'
    }).reset_index()
    
    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

    # Scoring
    rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4,3,2,1])
    rfm['F_Score'] = pd.cut(rfm['Frequency'], bins=[0,1,2,4,rfm['Frequency'].max()],
                            labels=[1,2,3,4], include_lowest=True)
    rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1,2,3,4], duplicates='drop')
    
    rfm['RFM_Segment'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
    rfm['RFM_Score'] = rfm[['R_Score', 'F_Score', 'M_Score']].astype(int).sum(axis=1)
    
    return rfm

def assign_segment(score):
    if score >= 9:
        return 'Best Customers'
    elif score >= 6:
        return 'Loyal Customers'
    elif score >= 4:
        return 'At Risk'
    else:
        return 'Churned'
    
rfm['Segment'] = rfm['RFM_Score'].apply(assign_segment)

return rfm
