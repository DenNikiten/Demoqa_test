#  Первый вариант запуска тестов:

## Запуск автоматического теста E2E UI для тестирования распространенных типов элементов DOM на сайте demoqa.com с использованием Python + Selenium + Pytest + CI/CD.

На сайте github.com перейдите по ссылке:
```html
https://github.com/DenNikiten/Demoqa_test/actions/workflows/run_tests.yml
```
Нажмите на Run workflow, выберите тесты, которые необходимо проверить и кликните на button 'Run workflow'.

# Второй вариант запуска тестов:

## Запуск автоматического теста E2E UI и просмотр отчетов Allure для тестирования распространенных типов элементов DOM на сайте demoqa.com с использованием Python + Selenium + Pytest.

С сайта github.com клонируйте репозиторий, в используемую вами IDE, следующей командой:
```html
git clone https://github.com/DenNikiten/Demoqa_test.git
```

### Создайте виртуальное окружение с помощью следующих команд:

В терминале в рабочей директории e2e_ui выполните команду для Windows, Linux и macOS:
```html
python -m venv venv
```

### Активируйте виртуальное окружение с помощью следующих команд:

В терминале в рабочей директории e2e_ui выполните команду для Windows:
```html
venv\Scripts\activate
```

В терминале в рабочей директории e2e_ui выполните команду для Linux и macOS:
```html
source venv/bin/activate
```

### В терминале в рабочей директории e2e_ui установите зависимости для работы следующей командой:
```html
pip install -r requirements.txt
```

### В терминале в директории проекта e2e_ui выполните команду для запуска тестов и создания Allure отчетов в папке test_results/:
```html
python -m pytest --alluredir=test_results/
```

### Для просмотра отчетов Allure в директории проекта e2e_ui в терминале выполните команду:
```html
allure serve test_results/
```