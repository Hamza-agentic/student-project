# Student Information Application

A modular Python project developed following professional software engineering principles and standard project structures.

## Project Structure
```text
student_project/
├── data/
│   └── student.json
│
├── src/
│   └── student_app/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── logger.py
│       │
│       ├── models/
│       │   └── student.py
│       │
│       ├── services/
│       │   └── calculator.py
│       │
│       ├── utils/
│       │   └── validation.py
│       │
│       └── reports/
│           └── student_report.py
│
├── tests/
│   ├── test_calculator.py
│   └── test_validation.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt