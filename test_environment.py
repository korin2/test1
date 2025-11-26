#!/usr/bin/env python3
"""
Тестовый скрипт для проверки окружения Python
"""

import sys
import platform
import os

def check_environment():
    """Проверяет основные компоненты окружения Python"""
    
    print("=" * 50)
    print("ПРОВЕРКА ОКРУЖЕНИЯ PYTHON")
    print("=" * 50)
    
    # Версия Python
    print(f"✓ Версия Python: {sys.version}")
    print(f"✓ Платформа: {platform.platform()}")
    print(f"✓ Текущая директория: {os.getcwd()}")
    
    # Проверка стандартных библиотек
    libraries_to_check = ['json', 'os', 'sys', 'math', 'datetime', 're']
    print("\n✓ Стандартные библиотеки:")
    for lib in libraries_to_check:
        try:
            __import__(lib)
            print(f"  - {lib}: ✅ доступна")
        except ImportError:
            print(f"  - {lib}: ❌ недоступна")
    
    # Проверка основных функций
    print("\n✓ Проверка базовых операций:")
    try:
        result = 2 + 3
        print(f"  - Арифметика: 2 + 3 = {result} ✅")
    except Exception as e:
        print(f"  - Арифметика: ❌ ошибка - {e}")
    
    try:
        test_list = [1, 2, 3]
        test_list.append(4)
        print(f"  - Работа со списками: {test_list} ✅")
    except Exception as e:
        print(f"  - Работа со списками: ❌ ошибка - {e}")
    
    try:
        test_dict = {"key": "value"}
        print(f"  - Работа со словарями: {test_dict} ✅")
    except Exception as e:
        print(f"  - Работа со словарями: ❌ ошибка - {e}")
    
    print("\n" + "=" * 50)
    print("ПРОВЕРКА ЗАВЕРШЕНА!")
    print("=" * 50)

if __name__ == "__main__":
    check_environment()