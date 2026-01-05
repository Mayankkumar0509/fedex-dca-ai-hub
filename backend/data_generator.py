import pandas as pd
import numpy as np

def generate_data(n=1000):
    np.random.seed(42)

    amount_due = np.random.randint(500, 50000, n)
    days_overdue = np.random.randint(1, 180, n)
    customer_risk_score = np.random.uniform(0, 1, n)
    past_recovery_rate = np.random.uniform(0.2, 0.9, n)

    # Business-driven recovery logic
    recovery_score = (
        0.4 * (1 - days_overdue / 180) +
        0.4 * past_recovery_rate +
        0.2 * (1 - customer_risk_score)
    )

    recovered = (recovery_score > 0.5).astype(int)

    df = pd.DataFrame({
        "amount_due": amount_due,
        "days_overdue": days_overdue,
        "customer_risk_score": customer_risk_score,
        "past_recovery_rate": past_recovery_rate,
        "recovered": recovered
    })

    return df

if __name__ == "__main__":
    df = generate_data()
    df.to_csv("dca_cases.csv", index=False)
    print("✅ Smart synthetic data generated")
