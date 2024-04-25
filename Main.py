from typing import List

# Clase para el nodo del árbol binario de búsqueda
class Node:
    def __init__(self, data, filename):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1  # Contador para el número de veces que aparece la palabra en este archivo
        self.files = {filename}  # Conjunto de nombres de archivos en los que aparece la palabra


# Función para insertar una palabra en el árbol correspondiente al archivo
def insert_word(root, word, filename):
    if root is None:
        return Node(word, filename)
    elif word < root.data:
        root.left = insert_word(root.left, word, filename)
    elif word > root.data:
        root.right = insert_word(root.right, word, filename)
    else:
        # Si la palabra ya existe, simplemente incrementamos el contador y agregamos el nombre del archivo
        root.count += 1
        root.files.add(filename)
    return root


# Función para buscar una palabra en el árbol y devolver su frecuencia y en qué archivos aparece
def search_word(root, word):
    if root is None:
        return 0, set()
    elif word < root.data:
        return search_word(root.left, word)
    elif word > root.data:
        return search_word(root.right, word)
    else:
        return root.count, root.files


# Función para procesar el archivo y construir el árbol correspondiente
def process_file(filename):
    root = None
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.strip().lower()
                if word.isalpha():
                    if root is None:
                        root = Node(word, filename)
                    else:
                        root = insert_word(root, word, filename)  # Insertar palabras como hijos
    return root





# Función para imprimir el árbol en orden
def inorder_traversal(root, filename):
    if root:
        inorder_traversal(root.left, filename)
        print(root.data, root.count, filename)
        inorder_traversal(root.right, filename)


# Función principal
def main(files: List[str]):
    roots = {}  # Diccionario para mantener los árboles de cada archivo
    for file in files:
        roots[file] = process_file(file)

    while True:
        display_menu()
        choice = input("Ingrese su elección: ")

        if choice == "1":
            show_words_in_file(files, roots)
        elif choice == "2":
            search_word_in_files(files, roots)
        elif choice == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


def display_menu():
    print("\nMenu:")
    print("1. Mostrar palabras en un archivo")
    print("2. Buscar una palabra en todos los archivos")
    print("3. Salir")


def show_words_in_file(files: List[str], roots):
    print("Seleccione un archivo:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")
    file_index = int(input("Ingrese el número del archivo: ")) - 1
    if 0 <= file_index < len(files):
        filename = files[file_index]
        print(f"\nPalabras en {filename} (Inorder):")
        inorder_traversal(roots[filename], filename)
    else:
        print("Número de archivo inválido.")


def search_word_in_files(files: List[str], roots):
    word = input("Ingrese la palabra a buscar: ").strip().lower()
    print(f"Buscando la palabra '{word}' en todos los archivos:")
    total_count = 0
    for filename, root in roots.items():
        count, files = search_word(root, word)
        total_count += count
        print(f"'{word}' aparece {count} veces en '{filename}'")
    print(f"\nLa palabra '{word}' aparece un total de {total_count} veces en todos los archivos.")


if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt",
             "file6.txt", "file7.txt", "file8.txt", "file9.txt", "file10.txt"]  # Lista de archivos

    main(files)
