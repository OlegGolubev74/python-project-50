import os

from gendiff.gendiff import generate_diff


def test_generate_diff_flat_json():
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

    FILE1_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file1.json")
    FILE2_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file2.json")

    result = generate_diff(FILE1_PATH, FILE2_PATH)
 
    assert result.strip() == expected_output.strip()


def test_generate_diff_flat_yaml():

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

    FILE1_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file1.yaml")
    FILE2_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file2.yaml")

    result = generate_diff(FILE1_PATH, FILE2_PATH)

    assert result.strip() == expected_output.strip()


def test_generate_diff_recursive_json():

    expected_output = """
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
"""
    
    FILE1_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file3.json")
    FILE2_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file4.json")

    result = generate_diff(FILE1_PATH, FILE2_PATH)
  
    assert result.strip() == expected_output.strip()


def test_generate_diff_recursive_yaml():

    expected_output = """
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
"""
    
    FILE1_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file3.yaml")
    FILE2_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file4.yaml")

    result = generate_diff(FILE1_PATH, FILE2_PATH)

    assert result.strip() == expected_output.strip()


def test_generate_diff_plain_json():

    expected_output = """
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
"""
    
    FILE1_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file3.json")
    FILE2_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file4.json")

    result = generate_diff(FILE1_PATH, FILE2_PATH, 'plain')

    assert result.strip() == expected_output.strip()


def test_generate_diff_plain_yaml():

    expected_output = """
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
"""

    FILE1_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file3.yaml")
    FILE2_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file4.yaml")

    result = generate_diff(FILE1_PATH, FILE2_PATH, 'plain')

    assert result.strip() == expected_output.strip()


def test_generate_diff_json_to_json():

    expected_output = '''
[
  {
    "key": "common",
    "type": "nested",
    "children": [
      {
        "key": "follow",
        "type": "added",
        "value": false
      },
      {
        "key": "setting1",
        "type": "unchanged",
        "value": "Value 1"
      },
      {
        "key": "setting2",
        "type": "removed",
        "value": 200
      },
      {
        "key": "setting3",
        "type": "changed",
        "old_value": true,
        "new_value": null
      },
      {
        "key": "setting4",
        "type": "added",
        "value": "blah blah"
      },
      {
        "key": "setting5",
        "type": "added",
        "value": {
          "key5": "value5"
        }
      },
      {
        "key": "setting6",
        "type": "nested",
        "children": [
          {
            "key": "doge",
            "type": "nested",
            "children": [
              {
                "key": "wow",
                "type": "changed",
                "old_value": "",
                "new_value": "so much"
              }
            ]
          },
          {
            "key": "key",
            "type": "unchanged",
            "value": "value"
          },
          {
            "key": "ops",
            "type": "added",
            "value": "vops"
          }
        ]
      }
    ]
  },
  {
    "key": "group1",
    "type": "nested",
    "children": [
      {
        "key": "baz",
        "type": "changed",
        "old_value": "bas",
        "new_value": "bars"
      },
      {
        "key": "foo",
        "type": "unchanged",
        "value": "bar"
      },
      {
        "key": "nest",
        "type": "changed",
        "old_value": {
          "key": "value"
        },
        "new_value": "str"
      }
    ]
  },
  {
    "key": "group2",
    "type": "removed",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  {
    "key": "group3",
    "type": "added",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
]
'''

    FILE1_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file3.json")
    FILE2_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file4.json")

    result = generate_diff(FILE1_PATH, FILE2_PATH, 'json')

    assert result.strip() == expected_output.strip()


def test_generate_diff_yaml_to_json():

    expected_output = '''
[
  {
    "key": "common",
    "type": "nested",
    "children": [
      {
        "key": "follow",
        "type": "added",
        "value": false
      },
      {
        "key": "setting1",
        "type": "unchanged",
        "value": "Value 1"
      },
      {
        "key": "setting2",
        "type": "removed",
        "value": 200
      },
      {
        "key": "setting3",
        "type": "changed",
        "old_value": true,
        "new_value": null
      },
      {
        "key": "setting4",
        "type": "added",
        "value": "blah blah"
      },
      {
        "key": "setting5",
        "type": "added",
        "value": {
          "key5": "value5"
        }
      },
      {
        "key": "setting6",
        "type": "nested",
        "children": [
          {
            "key": "doge",
            "type": "nested",
            "children": [
              {
                "key": "wow",
                "type": "changed",
                "old_value": "",
                "new_value": "so much"
              }
            ]
          },
          {
            "key": "key",
            "type": "unchanged",
            "value": "value"
          },
          {
            "key": "ops",
            "type": "added",
            "value": "vops"
          }
        ]
      }
    ]
  },
  {
    "key": "group1",
    "type": "nested",
    "children": [
      {
        "key": "baz",
        "type": "changed",
        "old_value": "bas",
        "new_value": "bars"
      },
      {
        "key": "foo",
        "type": "unchanged",
        "value": "bar"
      },
      {
        "key": "nest",
        "type": "changed",
        "old_value": {
          "key": "value"
        },
        "new_value": "str"
      }
    ]
  },
  {
    "key": "group2",
    "type": "removed",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  {
    "key": "group3",
    "type": "added",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
]
'''
    FILE1_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file3.yaml")
    FILE2_PATH = os.path.join(os.path.dirname(__file__), 
                              "test_data", "file4.yaml")

    result = generate_diff(FILE1_PATH, FILE2_PATH, 'json')

    assert result.strip() == expected_output.strip()