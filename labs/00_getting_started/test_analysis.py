from __future__ import annotations

import numpy as np
import pytest

from analysis import chronological_split, evaluate_baselines, make_series


def test_series_is_reproducible() -> None:
    first = make_series(seed=4031)
    second = make_series(seed=4031)
    assert first.equals(second)


def test_split_is_chronological_and_disjoint() -> None:
    train, test = chronological_split(make_series(), test_periods=16)
    assert len(train) == 64
    assert len(test) == 16
    assert train["period"].max() < test["period"].min()
    assert set(train.index).isdisjoint(test.index)


def test_invalid_split_is_rejected() -> None:
    data = make_series()
    with pytest.raises(ValueError):
        chronological_split(data, test_periods=len(data))


def test_baseline_metrics_are_finite_and_nonnegative() -> None:
    train, test = chronological_split(make_series())
    results = evaluate_baselines(train, test)
    assert list(results["model"]) == ["last observation", "linear trend"]
    assert np.isfinite(results["test_rmse"]).all()
    assert (results["test_rmse"] >= 0).all()
