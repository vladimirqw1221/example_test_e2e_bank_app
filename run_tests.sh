#!/bin/bash
#!/bin/bash

# Установить переменную окружения для указания пути к файлу .env
export DOTENV_FILE=".env"

# Запустить тесты с использованием pytest и передачей переменных окружения
pytest
