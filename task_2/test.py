# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from author import Contact


def test_show_contact():
    """У класса Contact присутствует метод show_contact()"""
    assert Contact.show_contact.__name__ == 'show_contact', (
        f'Проверьте наличие метода show_contact() у класса Contact,'
        f'не забудьте про аргумент self'
    )

def test_show_contact_print(capfd):
    """метод show_contact() выводит верную информацию"""
    test_contact = Contact('test_name', 'test_phone', 'test_birthday', 'test_address')
    exception = (
        f'{test_contact.name} — адрес: {test_contact.address}, '
        f'телефон: {test_contact.phone}, день рождения: '
        f'{test_contact.birthday}'
    )
    test_contact.show_contact()
    out, err = capfd.readouterr()
    out2 = out.split('\n')
    assert out2[1] == exception, (
        f'Проверьте наличие вывода информации (print) в методе show_contact(). '
        f'Текст должен соответствовать функции print_contact()'
    )

def test_print_contact():
    """Функция def print_contact(): удалена из кода"""
    file = open('author.py', 'r', encoding='utf-8')
    data = file.read()
    print_contact_exist = False
    if "def print_contact():" in data:
        print_contact_exist = True
    assert print_contact_exist == False, (
        f'Проверьте не забыли ли удалить из кода функцию print_contact()'
    )

def test_mike_vlad_exists():
    """Проверяем вызов mike.show_contact() и vlad.show_contact()"""
    file = open('author.py', 'r', encoding='utf-8')
    data = file.read()
    make_and_vlad_exist = False
    if 'mike.show_contact()' and 'vlad.show_contact()' in data:
        make_and_vlad_exist = True
    assert make_and_vlad_exist == True, (
        f'Проверьте, что вызвали метод `show_contact` для объектов mike и vlad'
    )
