
# Persian DateTime Converter

**Persian DateTime Converter** is a Python library that allows you to convert Python datetime objects to Persian (Jalali) calendar dates without relying on any external libraries. This is particularly useful for developers who need to work with Persian dates in Python applications.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Example](#basic-example)
  - [Additional Examples](#additional-examples)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To install the package, you can use `pip`, the Python package installer. Run the following command in your terminal:

```bash
pip install persian_datetime_converter
```

This will download and install the `persian_datetime_converter` package from PyPI.

## Usage

After installing the package, you can start using it to convert Gregorian (Python `datetime`) dates to Persian (Jalali) dates.

### Basic Example

```python
from persian_datetime_converter.converter import PersianDateConverter
import datetime

# Example datetime: 13th September 2024
dt = datetime.datetime(2024, 9, 13)

# Convert to Persian date
persian_date = PersianDateConverter.convert(dt)

print(f"Gregorian: {dt.year}-{dt.month}-{dt.day} -> Persian: {persian_date[0]}-{persian_date[1]}-{persian_date[2]}")
# Output: Gregorian: 2024-9-13 -> Persian: 1403-6-23
```

### Additional Examples

#### Converting the Start of the Persian Year

```python
dt = datetime.datetime(2023, 3, 21)  # 21st March 2023 (Start of Persian year 1402)
persian_date = PersianDateConverter.convert(dt)
print(persian_date)  # Output: (1402, 1, 1)
```

#### Converting the End of the Persian Year

```python
dt = datetime.datetime(2022, 3, 20)  # 20th March 2022 (End of Persian year 1400)
persian_date = PersianDateConverter.convert(dt)
print(persian_date)  # Output: (1400, 12, 29)
```

#### Checking Leap Years

```python
from persian_datetime_converter.converter import PersianDateConverter

print(PersianDateConverter.is_leap_gregorian(2024))  # Output: True
print(PersianDateConverter.is_leap_gregorian(2023))  # Output: False
```

## API Reference

### `PersianDateConverter.convert(datetime_obj)`

- **Description**: Converts a Python `datetime` object to a Persian date.
- **Parameters**:
  - `datetime_obj` (`datetime`): The Python datetime object to convert.
- **Returns**: A tuple containing the Persian year, month, and day.

### `PersianDateConverter.is_leap_gregorian(year)`

- **Description**: Determines if a given Gregorian year is a leap year.
- **Parameters**:
  - `year` (`int`): The Gregorian year to check.
- **Returns**: `True` if the year is a leap year, `False` otherwise.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue on the [GitHub repository](https://github.com/bahmany/persian_datetime_converter).

To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -am 'Add a new feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request.

## Running Tests

To run tests, use the following command:

```bash
python -m unittest discover tests
```

Make sure all tests pass before submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or need further information, feel free to contact me:

- **Author**: Mohammad Reza Bahmani
- **Email**: bahmanymb@gmail.com

You can also open an issue on the [GitHub repository](https://github.com/bahmany/persian_datetime_converter) for any inquiries or issues.

---

Thank you for using Persian DateTime Converter! Your contributions and feedback are always appreciated.
e `https://github.com/bahmany/persian_datetime_converter` with your actual GitHub repository URL to make the README complete.