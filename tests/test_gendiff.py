import os

from gendiff.gendiff import generate_diff


def test_generate_diff():
    # Ожидаемый результат
    expected_output = """
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
"""

    # Пути к фикстурам (относительно расположения теста)
    FILE1_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file1.json")
    FILE2_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file2.json")

    result = generate_diff(FILE1_PATH, FILE2_PATH)
    # Сравнение (игнорируем лишние пробелы и переносы)
    assert result.strip() == expected_output.strip()


