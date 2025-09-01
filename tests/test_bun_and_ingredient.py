import allure
import pytest

ING_PARAMS = [
    pytest.param("mock_sauce", "sauce", "sour cream", 200, id="sauce_sour_cream"),
    pytest.param("mock_filling", "filling", "sausage", 300, id="filling_sausage"),
]


@allure.epic("Burger App")
@allure.feature("Bun")
class TestBun:
    @allure.title("Булка: корректно возвращает имя")
    def test_bun_name(self, mock_bun):
        """Проверяет, что метод get_name у булки возвращает правильное имя."""
        with allure.step("Проверяю имя булки"):
            assert mock_bun.get_name() == "black bun"

    @allure.title("Булка: корректно возвращает цену")
    def test_bun_price(self, mock_bun):
        """Проверяет, что метод get_price у булки возвращает правильную цену."""
        with allure.step("Проверяю цену булки"):
            assert mock_bun.get_price() == 100


@allure.epic("Burger App")
@allure.feature("Ingredient")
class TestIngredient:
    @allure.title("Ингредиент: корректно возвращает тип (в нижнем регистре)")
    @pytest.mark.parametrize("ingredient_fixture, exp_type, _, _p", ING_PARAMS)
    def test_ingredient_type(self, request, ingredient_fixture, exp_type, _, _p):
        """Проверяет, что метод get_type возвращает ожидаемый тип ингредиента (sauce/filling)."""
        ing = request.getfixturevalue(ingredient_fixture)
        with allure.step(f"Проверяю тип ингредиента ({exp_type})"):
            assert ing.get_type() == exp_type

    @allure.title("Ингредиент: корректно возвращает имя")
    @pytest.mark.parametrize("ingredient_fixture, _t, exp_name, _p", ING_PARAMS)
    def test_ingredient_name(self, request, ingredient_fixture, _t, exp_name, _p):
        """Проверяет, что метод get_name возвращает правильное имя ингредиента."""
        ing = request.getfixturevalue(ingredient_fixture)
        with allure.step(f"Проверяю имя ингредиента ({exp_name})"):
            assert ing.get_name() == exp_name

    @allure.title("Ингредиент: корректно возвращает цену")
    @pytest.mark.parametrize("ingredient_fixture, _t, _n, exp_price", ING_PARAMS)
    def test_ingredient_price(self, request, ingredient_fixture, _t, _n, exp_price):
        """Проверяет, что метод get_price возвращает правильную цену ингредиента."""
        ing = request.getfixturevalue(ingredient_fixture)
        with allure.step(f"Проверяю цену ингредиента ({exp_price})"):
            assert ing.get_price() == exp_price