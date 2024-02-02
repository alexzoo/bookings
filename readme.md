# Automated Testing Project for Restful Booker API

This project is designed for automated testing of the API provided by Restful Booker. Restful Booker offers a wide range of APIs for users who want to practice testing and developing APIs. The API documentation is available at [this link](https://restful-booker.herokuapp.com/apidoc/index.html).

[Here you can find mindmap diagram for API endpoints](./docs/mindmap.svg)

## Technologies and Tools

The following technologies and tools are used in this project:

- **Programming Language:** Python
- **Testing Framework:** PyTest
- **Library for requests:** Requests
- **Testing Reports:** Allure
- **CI/CD:** GitHub Actions

## CI/CD

GitHub Actions is used for continuous integration and delivery. The CI/CD configuration is set up to automatically run tests with every push and pull request to the repository. This provides quick feedback on the quality of the code and the API's functionality.

## Testing Reports with Allure

The Allure Framework is used to visualize the testing results. Allure provides detailed reports on test runs, including execution statistics, testing steps, and screenshots. The test results are automatically published and available on the [Allure Report](https://alexzoo.github.io/bookings/) page.

## How to Run Tests

To run the tests locally, you need to follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/alexzoo/bookings.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run tests with PyTest:

```bash
pytest
```

4. To generate an Allure report, use the following command:

```bash
pytest --alluredir ./allure-results
allure serve allure-results
```