from collections import MutableMapping
import json
import pprint
import sys


# https://github.com/ScriptSmith/socialreaper/blob/master/socialreaper/tools.py#L8
def flatten(dictionary: dict, parent_key: bool = False, separator: str = ".") -> dict:
    """
    Turn a nested dictionary into a flattened dictionary
    :param dictionary: The dictionary to flatten
    :param parent_key: The string to prepend to dictionary's keys
    :param separator: The string used to separate flattened keys
    :return: A flattened dictionary
    """

    items = []
    for key, value in dictionary.items():
        # new_key = str(parent_key) + separator + key if parent_key else key
        new_key = str(parent_key) + "[" + repr(key) + "]" if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(flatten(value, new_key, separator).items())
        elif isinstance(value, list):
            for k, v in enumerate(value):
                items.extend(flatten({str(k): v}, new_key).items())
        else:
            items.append((new_key, value))
    return dict(items)


def main():
    data = json.load(sys.stdin)
    pprint.pprint(flatten(data, "json"))
    print(json.dumps(flatten(data, "json")))


if __name__ == "__main__":
    main()
