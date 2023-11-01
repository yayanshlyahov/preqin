import pytest
from utils import generate_random_values


# Permissible deviation from normal distribution
EPS = 0.25


# Check if our random values are in normal distribution
@pytest.mark.parametrize(
    'min_value, max_value, count, result', (
        (0, 1, 500, 0.5),
        (0, 10, 500, 5),
    )
)
def test_utils_normal_values(min_value, max_value, count, result):
    sum_of_values = sum(generate_random_values(min_value, max_value, count))
    avg_of_values = sum_of_values / count
    assert abs(avg_of_values - result) < EPS
