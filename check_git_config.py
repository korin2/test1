#!/usr/bin/env python3
"""
Скрипт для проверки конфигурации Git
"""

import subprocess
import os

def check_git_config():
    """Проверяет настройки user.name и user.email в Git"""
    
    print("=" * 50)
    print("ПРОВЕРКА КОНФИГУРАЦИИ GIT")
    print("=" * 50)
    
    # Проверяем, установлен ли git
    try:
        result = subprocess.run(['git', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"✓ Git установлен: {result.stdout.strip()}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git не установлен или не найден в PATH")
        return
    
    # Проверяем user.name
    try:
        user_name = subprocess.run(['git', 'config', 'user.name'], 
                                 capture_output=True, text=True, check=True)
        print(f"✓ user.name: {user_name.stdout.strip()}")
    except subprocess.CalledProcessError:
        print("❌ user.name не настроен")
    
    # Проверяем user.email
    try:
        user_email = subprocess.run(['git', 'config', 'user.email'], 
                                  capture_output=True, text=True, check=True)
        print(f"✓ user.email: {user_email.stdout.strip()}")
    except subprocess.CalledProcessError:
        print("❌ user.email не настроен")
    
    # Проверяем глобальные настройки
    print("\nГлобальные настройки:")
    try:
        global_name = subprocess.run(['git', 'config', '--global', 'user.name'], 
                                   capture_output=True, text=True)
        if global_name.returncode == 0:
            print(f"  user.name: {global_name.stdout.strip()}")
        else:
            print("  user.name: не настроен глобально")
            
        global_email = subprocess.run(['git', 'config', '--global', 'user.email'], 
                                    capture_output=True, text=True)
        if global_email.returncode == 0:
            print(f"  user.email: {global_email.stdout.strip()}")
        else:
            print("  user.email: не настроен глобально")
    except Exception as e:
        print(f"  Ошибка при проверке глобальных настроек: {e}")
    
    print("\n" + "=" * 50)
    print("Для настройки выполни команды:")
    print('git config --global user.name "Твое Имя"')
    print('git config --global user.email "твой@email.com"')
    print("=" * 50)

if __name__ == "__main__":
    check_git_config()