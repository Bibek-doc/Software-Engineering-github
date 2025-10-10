"""
1. Calculates total length.
2. Counts uppercase characters (for strings).
"""

from typing import Union


class DataAnalyzer:
    """
    A class to analyze either a string or a list.
    """

    def __init__(self, data: Union[str, list]) -> None:
        """
        
        :param data: A string or list to be analyzed.
        """
        self.data = data #Initialize with data.#

    def total_length(self) -> int:
        """
        Returns the total length of the data.
        :return: Length of string or list.
        """
        return len(self.data)

    def count_uppercase(self) -> int:
        # """
        # Returns the number of uppercase characters if data is string.
        # For list, counts uppercase characters only if elements are strings.
        # :return: Number of uppercase characters.
        # """
        count = 0
        if isinstance(self.data, str):
            count = sum(1 for char in self.data if char.isupper())
        elif isinstance(self.data, list):
            for item in self.data:
                if isinstance(item, str):
                    count += sum(1 for char in item if char.isupper())
        return count


def main() -> None:
    """
    Demonstrates the DataAnalyzer with sample inputs.
    """
    # Example 1: Input is string
    text = "Hello World!"
    analyzer1 = DataAnalyzer(text)
    print("Input:", text)
    print("Total length:", analyzer1.total_length())
    print("Uppercase count:", analyzer1.count_uppercase())

    # Example 2: Input is list
    data_list = ["Hello", "WORLD", 123, "Python"]
    analyzer2 = DataAnalyzer(data_list)
    print("\nInput:", data_list)
    print("Total length:", analyzer2.total_length())
    print("Uppercase count:", analyzer2.count_uppercase())


if __name__ == "__main__":
    main()
