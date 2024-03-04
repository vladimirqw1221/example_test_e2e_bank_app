#!/bin/bash



# Установить переменную окружения для указания пути к файлу .env
export BASE_URL=https://www.globalsqa.com/angularJs-protractor/BankingProject/

# Загрузить переменные окружения из файла .env


# Запустить тесты с использованием pytest и передачей переменных окружения
pytest
