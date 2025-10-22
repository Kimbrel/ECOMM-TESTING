# 🛒 Automated Testing for Demo E-Commerce Platform

This repository contains a robust, structured QA automation framework designed to test the critical user flow of the **Sauce Demo** e-commerce website. The project is built using Python, Selenium WebDriver, and follows the Page Object Model (POM) to ensure code reusability and maintainability.

---

## 🚀 Project Overview

The primary goal of this project is to automate and validate the core user journey: **Login** $\rightarrow$ **Product Selection** $\rightarrow$ **Add to Cart** $\rightarrow$ **Cart Verification**.

### Key Features Demonstrated:

* **Page Object Model (POM):** Implemented to separate test logic from page element locators, making the framework scalable and easier to maintain.
* **Data-Driven Testing (DDT):** Utilized Pytest parameterization to test the login functionality against multiple valid and invalid user credentials sourced from a JSON file.
* **Pytest Framework:** Used for test discovery, execution, fixture management (setup/teardown), and assertions.
* **WebDriver Management:** Proper use of Pytest fixtures (`conftest.py`) to handle browser initialization, implicit waits, and graceful closure (`driver.quit()`).

---

## 🛠️ Technology Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.x |
| **Automation Tool** | Selenium WebDriver |
| **Testing Framework** | Pytest |
| **Dependencies Management** | `requirements.txt` / `pip` |
| **Design Pattern** | Page Object Model (POM) |

---

## 💻 Setup and Execution

### Prerequisites

1.  **Python:** Ensure you have Python 3.x installed.
2.  **Chrome/Firefox:** The WebDriver will automatically download the necessary browser driver (using Selenium Manager).


### Running the Tests

Execute the test suite from the root directory using the `pytest` command:

1.  **Run the entire suite:**
    ```bash
    pytest
    ```
2.  **Run a specific test file (e.g., Login Tests):**
    ```bash
    pytest tests/test_login.py
    ```
3.  **Generate a detailed report (requires external plugin like `pytest-html` or `allure-pytest` if used):**
    ```bash
    # Example using pytest-html (if installed)
    pytest --html=report.html
    ```

---
