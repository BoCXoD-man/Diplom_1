"""
Тесты класса Burger:
- сетап булочек;
- добавление/удаление/перемещение ингредиентов;
- корректный расчёт итоговой цены;
- формат чека (включая порядок строк).
Фикстуры берём из conftest.py.
"""

import pytest
from praktikum.burger import Burger


class TestBurger:
    def test_burger_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        # Проверяем, что внутри Burger хранится ровно та же ссылка на мок (а не копия и т.п.)
        assert burger.bun is mock_bun

    def test_burger_add_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert mock_sauce in burger.ingredients

    def test_burger_remove_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_burger_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        # Важно проверить именно перестановку, а не дублирование/удаление:
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_filling, mock_sauce]

    def test_burger_get_price(self, mock_bun, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)

        # Итог = булочка сверху+снизу + сумма ингредиентов
        price = burger.get_price()
        expected_price = mock_bun.get_price() * 2 + mock_sauce.get_price()
        assert price == expected_price

    def test_burger_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        # Чек чувствителен к форматированию (строки/порядок/регистр),
        # поэтому сравниваем целиком ожидаемую строку.
        expected_result = (
            '(==== black bun ====)\n'
            '= sauce sour cream =\n'
            '= filling sausage =\n'
            '(==== black bun ====)\n'
            '\n'
            'Price: 700'
        )
        assert burger.get_receipt() == expected_result