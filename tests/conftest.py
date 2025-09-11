import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

"""
Общие фикстуры для тестов Burger.
- Используем unittest.mock.Mock с параметром spec=..., чтобы мок имел тот же
интерфейс, что и реальные классы Bun/Ingredient. Это даёт раннее падение
при обращении к несуществующим методам.
- Фиксируем значения (имя/цена/тип), чтобы упрощать проверку.
"""


@pytest.fixture
def mock_bun():
    """Мок булочки: имя 'black bun', цена 100."""
    bun = Mock(spec=Bun)  # spec ограничивает доступные атрибуты реальным интерфейсом Bun
    bun.get_name.return_value = 'black bun'
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_sauce():
    """Мок соуса: тип 'sauce', имя 'sour cream', цена 200."""
    sauce = Mock(spec=Ingredient)  # любые вызовы несуществующих методов приведут к ошибке
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE.lower()
    sauce.get_name.return_value = 'sour cream'
    sauce.get_price.return_value = 200
    return sauce


@pytest.fixture
def mock_filling():
    """Мок начинки: тип 'filling', имя 'sausage', цена 300."""
    filling = Mock(spec=Ingredient)
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING.lower()
    filling.get_name.return_value = 'sausage'
    filling.get_price.return_value = 300
    return filling