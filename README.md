# My Django News Website - Test Automation Suite

This repository contains comprehensive automated tests for the [My Django News Website](https://github.com/explrprobe-tech/my_django_news_website) project.


## 🚀 What's Inside

- **API Tests** (pytest + requests) - Testing backend endpoints
- **UI Tests** (Playwright) - Testing user interface and interactions
- **Performance Tests** (k6) - Load and stress testing
- **CI/CD** (GitHub Actions) - Automated test runs on every push
- **Reporting** (Allure) - Beautiful test reports with history


## Project organization

my_django_news_tests/

├── .github/

│   └── workflows/

│       ├── api-ui-tests.yml      # API + UI tests CI

│       └── load-tests.yml        # Performance tests CI

├── tests/

│   ├── api/                      # API tests

│   │   ├── test_auth.py

│   │   └── test_news.py

│   ├── ui/                       # UI tests with Playwright

│   │   ├── page_tests/

│   │   └── e2e_tests/

│   ├── load_tests/               # k6 performance tests

│   │   ├── smoke_test.js

│   │   └── average_test.js

│   ├── conftest.py               # Shared test fixtures

│   └── helpers.py                # Helper functions

├── allure-results/               # Allure test results (generated)

├── pytest.ini                    # Pytest configuration

├── requirements-test.txt         # Python dependencies

└── README.md                     # This file


## Reports

- api and ui tests 
  Allure report
  https://explrprobe-tech.github.io/my_django_news_tests/allure/
- performance smoke test
  K6-web-dashboard report
  https://explrprobe-tech.github.io/my_django_news_tests/k6-smoke/index.html
- performance average test
  K6-web-dashboard report
  https://explrprobe-tech.github.io/my_django_news_tests/k6-average/index.html


## Installing

1. Create folder website
   mkdir website
2. Clone my_django_news_website repository
   git clone https://github.com/explrprobe-tech/my_django_news_website.git
3. Clone my_django_news_tests repository
   git clone https://github.com/explrprobe-tech/my_django_news_tests.git
4. Create my_django_news_website docker image
   cd my_django_news_website/mysite
   docker build -t mysite-web
5. Run api tests
   cd ../../my_django_news_tests/
   docker-compose -f docker-compose-api-ui.yml up api-test-runner --build
6. Run ui tests
   docker-compose -f docker-compose-api-ui.yml up ui-test-runner --build
7. Run load k6-smoke tests
   docker-compose -f docker-compose-load.yml up k6-smoke --build
8. Run load k6-average tests
   docker-compose -f docker-compose-load.yml up k6-average --build
