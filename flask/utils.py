import random

from const import STANDART


# Can be extanded with other algorithms
# First argument should be the min value, second vax value
ALGORITHM_TO_FUNCTION = {
    STANDART: random.uniform,
}


def randomize_value(min_value: float = 0, max_value: float = 1, algorithm: str = STANDART) -> float:
    random_function = ALGORITHM_TO_FUNCTION.get(algorithm)
    if random_function is None:
        raise ValueError('Invalid algoritm for random')
    return random_function(min_value, max_value)


def generate_random_values(
        min_value: float = 0, max_value: float = 1, count: int = 500, algorithm: str = STANDART) -> list[float]:
    return [
        randomize_value(min_value, max_value, algorithm) for _ in range(count)
    ]
