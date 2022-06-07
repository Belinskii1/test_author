import time


try:
    from author import time_check
except ImportError:
    assert False, 'Не найдена функция time_check'

try:
    from author import cache_args
except ImportError:
    assert False, 'Не найдена функция cache_args'

try:
    from author import long_heavy
except ImportError:
    assert False, 'Не найдена функция long_heavy'


class TestDecorator: 

    def test_long_heavy(self):
        """Проверяем рtзультат long_heavy"""
        assert long_heavy(10) == 20

    def test_few_runs(self):
        """проверяем несколько запусков функции"""
        start = time.time()
        long_heavy(20)
        stop = time.time()
        assert round(
            stop - start
        ) == 1, 'Учет времени не верен, проверьте работу функции'
        start1 = time.time()
        long_heavy(20)
        stop1 = time.time()
        assert round(
            stop1 - start1
        ) == 0, 'Повторный пуск по-прежнему выводит время выполнения функции'
