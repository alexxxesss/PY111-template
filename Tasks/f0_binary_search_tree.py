"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx


class BinarySearchTree:
    def __init__(self):
        """
        Example:
        {
            "key": 8,
            "value": 8,
            "left": {
                "key": 3,
                "value": 3,
                "left": left,
                "right": right
            },
            "right": {
                "key": 10,
                "value": 10,
                "left": None,
                "right": None
            }
        }

        """
        self.root = None

    @staticmethod
    def _create_node(key, value, left=None, right=None) -> dict:
        """ Фабричный метод """
        return {
            "key": key,
            "value": value,
            "left": left,
            "right": right
        }

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        if self.root is None:
            self.root = self._create_node(key, value)
        else:
            current_node = self.root
            current_key = current_node["key"]

            while True:
                if key > current_key:                    # уходим вправо
                    if current_node["right"] is None:
                        current_node["right"] = self._create_node(key, value)
                        break
                    else:
                        current_node = current_node["right"]
                        current_key = current_node["key"]
                else:                                    # уходим влево
                    if current_node["left"] is None:
                        current_node["left"] = self._create_node(key, value)
                        break
                    else:
                        current_node = current_node["left"]
                        current_key = current_node["key"]

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        print(key)
        return None

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        def _find(current_node):
            if current_node is None:
                raise KeyError('Нет такого значения в дереве')
            if current_node["key"] == key:
                return current_node["value"]

            current_key = current_node["key"]
            # next_node = current_node["right"] if key > current_key current_node["left"]
            # _find(next_node)
            if key > current_key:
                return _find(current_node["right"])  # вправо
            else:
                return _find(current_node["left"])   # влево

        return _find(self.root)


    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        self.root.clear()
