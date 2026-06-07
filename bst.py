class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, target):
        return self._search_recursive(self.root, target)
    
    def _search_recursive(self, node, target):
        if node is None:
            return False
        if target == node.value:
            return True
        elif target < node.value:
            return self._search_recursive(node.left, target)
        else:
            return self._search_recursive(node.right, target)
    
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def sum_values(self):
        return self._sum_recursive(self.root)
    
    def _sum_recursive(self, node):
        if node is None:
            return 0
        return node.value + self._sum_recursive(node.left) + self._sum_recursive(node.right)


def main():
    bst = BST()
    
    while True:
        print("БИНАРНОЕ ДЕРЕВО ПОИСКА")
        print("1. Вставить значение")
        print("2. Найти значение")
        print("3. Вывести все значения (по возрастанию)")
        print("4. Найти сумму всех значений (№9)")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            try:
                val = int(input("Введите целое число: "))
                bst.insert(val)
                print(f"Число {val} добавлено")
            except ValueError:
                print("Ошибка: введите целое число")
        
        elif choice == '2':
            try:
                target = int(input("Введите число для поиска: "))
                if bst.search(target):
                    print(f"Число {target} НАЙДЕНО")
                else:
                    print(f"Число {target} НЕ НАЙДЕНО")
            except ValueError:
                print("Ошибка: введите целое число")
        
        elif choice == '3':
            values = bst.inorder()
            if values:
                print("Значения в порядке возрастания:")
                print(" -> ".join(map(str, values)))
            else:
                print("Дерево пусто")
        
        elif choice == '4':
            total = bst.sum_values()
            print(f"Сумма значений во всех узлах: {total}")
        
        elif choice == '0':
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
