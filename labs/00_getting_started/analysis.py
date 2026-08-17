"""A leakage-aware forecasting baseline for ISYE 4031 Lab 00."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error


def make_series(n_periods: int = 80, seed: int = 4031) -> pd.DataFrame:
    """Create a reproducible time series with trend, seasonality, and noise."""
    rng = np.random.default_rng(seed)
    period = np.arange(n_periods)
    response = (
        25.0
        + 0.45 * period
        + 4.0 * np.sin(2.0 * np.pi * period / 12.0)
        + rng.normal(loc=0.0, scale=1.8, size=n_periods)
    )
    return pd.DataFrame({"period": period, "response": response})


def chronological_split(
    data: pd.DataFrame, test_periods: int = 16
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Reserve the most recent observations for honest forecast evaluation."""
    if not 0 < test_periods < len(data):
        raise ValueError("test_periods must be between 1 and len(data) - 1")
    split_at = len(data) - test_periods
    return data.iloc[:split_at].copy(), data.iloc[split_at:].copy()


def evaluate_baselines(
    train: pd.DataFrame, test: pd.DataFrame
) -> pd.DataFrame:
    """Compare a last-observation baseline with a linear-trend baseline."""
    naive_prediction = np.repeat(train["response"].iloc[-1], len(test))

    trend = LinearRegression()
    trend.fit(train[["period"]], train["response"])
    trend_prediction = trend.predict(test[["period"]])

    return pd.DataFrame(
        {
            "model": ["last observation", "linear trend"],
            "test_rmse": [
                root_mean_squared_error(test["response"], naive_prediction),
                root_mean_squared_error(test["response"], trend_prediction),
            ],
        }
    )


def main() -> None:
    data = make_series()
    train, test = chronological_split(data)
    results = evaluate_baselines(train, test)

    print(f"Training periods: {train['period'].min()} through {train['period'].max()}")
    print(f"Test periods: {test['period'].min()} through {test['period'].max()}")
    print("\nBaseline test-set performance (lower RMSE is better):")
    print(results.to_string(index=False, formatters={"test_rmse": "{:.3f}".format}))


if __name__ == "__main__":
    main()
