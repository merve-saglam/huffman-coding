import os
from HuffmanCoding import HuffmanCoding
from RBNode import RedBlackTree
from BTree import BTree

def main():
    huffman = HuffmanCoding()
    rbtree = RedBlackTree()
    btree = BTree()

    while True:
        print("\n--- Menu ---")
        print("1. File Compress")
        print("2. File Decompress")
        print("3. File Insert")
        print("4. File Search")
        print("5. File List")
        print("6. Exit")
        print("7. BTree Display")

        choice = input("Your choice: ").strip()

        if choice == "1":
            input_path = input("File path to compress: " ).strip()
            if not os.path.exists(input_path):
                print("File not found.")
                continue
            huffman.compress(input_path)
            print("File compressed successfully.")

        elif choice == "2":
            input_path = input("File path to decompress: " ).strip()
            output_path =input("Enter output path for decompressed file: ").strip()
            if not input_path or not output_path:
                print("Paths cannot be empty.")
                continue
            if not os.path.exists(input_path):
                print("Compressed file not found.")
                continue
            huffman.decompress(input_path)
            print("File decompressed successfully.")

        elif choice == "3":
            filename = input("Enter file name to insert into index: " ).strip()
            if not filename:
                print("File name cannot be empty.")
                continue
            rbtree.insert(filename)
            btree.insert(filename)
            print("File inserted into Red-Black Tree and B-Tree.")

        elif choice == "4":
            filename= input ("Enter file name to search. ").strip()
            result = rbtree.search(filename)
            if result and result.key is not None:
                print("File found in index.")
            else:
                print("File is not found.")

        elif choice == "5":
            print("File list: ")
            rbtree.list_files()

        elif choice == "6":
            print("Exiting...")
            break

        elif choice == "7":
            print("B-Tree File Index:")
            btree.display()

        else:
            print("invalid selection. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()