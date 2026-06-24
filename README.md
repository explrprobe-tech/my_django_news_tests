# My Django News Website - Test Automation Suite

Project was written with:<br>
Page Object Model pattern, used stack: pytest + requests, Playwright, k6 and Allure.<br><br>
This repository contains comprehensive automated tests for the [My Django News Website](https://github.com/explrprobe-tech/my_django_news_website) project.


## 🚀 What's Inside

- **API Tests** (pytest + requests) - Testing backend endpoints
- **UI Tests** (Playwright) - Testing user interface and interactions
- **Performance Tests** (k6) - Load and stress testing
- **CI/CD** (GitHub Actions) - Automated test runs on every push
- **Reporting** (Allure) - Beautiful test reports with history


## Project organization

my_django_news_tests/<br>
├── .github/<br>
│   └── workflows/<br>
│       ├── api-ui-tests.yml      # API + UI tests CI<br>
│       └── load-tests.yml        # Performance tests CI<br>
│<br>
├── tests/<br>
│   ├── api/                      # API tests<br>
│   │   ├── test_auth.py<br>
│   │   └── test_news.py<br>
│&nbsp;│<br>
│   ├── ui/                       # UI tests with Playwright<br>
│   │   ├── page_tests/<br>
│   │   └── e2e_tests/<br>
│&nbsp;│<br>
│   ├── load_tests/               # k6 performance tests<br>
│   │   ├── smoke_test.js<br>
│   │   └── average_test.js<br>
│&nbsp;│<br>
│   ├── conftest.py               # Shared test fixtures<br>
│   └── helpers.py                # Helper functions<br> 
│<br>
├── allure-results/               # Allure test results (generated)<br>
├── pytest.ini                    # Pytest configuration<br>
├── requirements-test.txt         # Python dependencies<br>
└── README.md                     # This file<br>


## CI/CD
### - api-ui-tests.yml<br>
  Launching:  every push to [main, master]<br>
  After changing:<br>
      - '.github/workflows/api-ui-tests.yml'<br>
      - 'tests/api/*'<br>
      - 'tests/ui/*'<br>
      - 'tests/conftest.py'<br>
      - 'tests/helpers.py'<br>
      - 'tests/test_data.py'<br>
      - 'tests/files_for_tests/*'<br>
### - load-tests.yml<br>
  Launching: every push to [main, master]<br>
  After changing:<br>
      - '.github/workflows/load-tests.yml'<br>
      - 'tests/load_tests/*'<br>
      - 'tests/files_for_tests/*'<br>

## Reports

- api and ui tests<br>
  Allure report<br>
  https://explrprobe-tech.github.io/my_django_news_tests/allure/
- performance smoke test<br>
  K6-web-dashboard report<br>
  https://explrprobe-tech.github.io/my_django_news_tests/k6-smoke/index.html
- performance average test<br>
  K6-web-dashboard report<br>
  https://explrprobe-tech.github.io/my_django_news_tests/k6-average/index.html


## Installing

1. Create folder website<br>
   mkdir website<br>
2. Clone my_django_news_website repository<br>
   git clone https://github.com/explrprobe-tech/my_django_news_website.git<br>
3. Clone my_django_news_tests repository<br>
   git clone https://github.com/explrprobe-tech/my_django_news_tests.git<br>
4. Create my_django_news_website docker image<br>
   cd my_django_news_website/mysite<br>
   docker build -t mysite-web<br>
5. Run api tests<br>
   cd ../../my_django_news_tests/<br>
   docker-compose -f docker-compose-api-ui.yml up api-test-runner --build<br>
6. Run ui tests<br>
   docker-compose -f docker-compose-api-ui.yml up ui-test-runner --build<br>
7. Run load k6-smoke tests<br>
   docker-compose -f docker-compose-load.yml up k6-smoke --build<br>
8. Run load k6-average tests<br>
   docker-compose -f docker-compose-load.yml up k6-average --build<br>
