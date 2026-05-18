from app import main


def test_should_return_zero_human_years_when_age_is_less_than_15() -> None:
    result = main.get_human_age(10, 14)
    assert result == [0, 0]


def test_first_15_cat_dog_years_give_1_human_year() -> None:
    result = main.get_human_age(15, 15)
    assert result == [1, 1]


def test_cat_and_dog_should_have_different_human_age() -> None:
    result = main.get_human_age(28, 28)
    assert result == [3, 2]


def test_24_is_the_second_human_age() -> None:
    result = main.get_human_age(24, 24)
    assert result == [2, 2]


def test_23_is_the_first_human_age() -> None:
    result = main.get_human_age(23, 23)
    assert result == [1, 1]


def test_100_is_21_and_17_human_years_for_cat_and_dog() -> None:
    result = main.get_human_age(100, 100)
    assert result == [21, 17]
