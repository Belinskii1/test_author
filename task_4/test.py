from inspect import isfunction
import author

try:
    from author import make_divider_of
except ImportError:
    assert False, 'Не найдена функция make_divider_of'


class TestDivideMaker:

    def test_code_has_precode_variables_and_methods(self):
        assert hasattr(
            author,
            'make_divider_of'
        ), 'Проверьте наличие функции "make_divider_of"'
        assert hasattr(
            author,
            'div2'
        ), 'Проверьтеналичие переменной "div2"'
        assert hasattr(
            author,
            'div5'
        ), 'Проверьте наличие переменной "div5"'

    def test_return_type_is_func(self):
        div2 = make_divider_of(2)
        assert isfunction(
            div2
        ), 'Убедитесь, что вызов функции make_divider_of возвращает функцию'

    def test_result_of_division(self):
        div2 = make_divider_of(2)
        assert div2(10) == 5, 'Функция div2(10) возвращает неверный результат'


def test_show_contact_print(capfd):
    """метод show_contact() выводит верную информацию"""
    div2 = make_divider_of(2)
    print(div2(10))
    div5 = make_divider_of(5)
    print(div5(20))
    print(div5(div2(20)))
    out, err = capfd.readouterr()
    out2 = out.split('\n')
    assert float(out2[0]) == 5.0, (
        f'Проверьте вывод результата 5.0 для div2(10)'
    )
    assert float(out2[1]) == 4.0, (
        f'Проверьте вывод результата 4.0 для div2(20)'
    )
    assert float(out2[2]) == 2.0, (
        f'Проверьте вывод результата 2.0 для div5(div2(20))'
    )
