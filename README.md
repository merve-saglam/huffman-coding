# Huffman File Compression and Indexing System

A Python command-line application that combines Huffman coding with tree-based file indexing. The project demonstrates lossless text compression, binary file generation, Red-Black Tree operations, and a simple secondary file index.

## Features

* Compresses UTF-8 text files using Huffman coding
* Generates binary `.bin` output files
* Decompresses encoded files back into text
* Calculates character frequencies
* Builds Huffman codes using a minimum heap
* Handles bit padding and byte conversion
* Indexes file names using a Red-Black Tree
* Supports file insertion, search, and sorted listing
* Maintains an additional simple B-Tree-style file index
* Provides an interactive command-line menu

## Technologies

* Python 3
* Huffman coding
* Priority queues and minimum heaps
* Binary trees
* Red-Black Trees
* File I/O
* Binary encoding

No external libraries are required.

## Running the Application

Clone the repository and run:

```bash
python3 Main.py
```

The application displays the following menu:

```text
1. File Compress
2. File Decompress
3. File Insert
4. File Search
5. File List
6. Exit
7. BTree Display
```

## Compressing a File

Select option `1` and enter the path of a text file:

```text
test.txt
```

The program creates:

```text
test.bin
```

## Decompressing a File

Select option `2` and provide the compressed file path:

```text
test.bin
```

The decompressed content is written to:

```text
test_decompressed.txt
```

The current implementation stores the Huffman code mapping in memory. Therefore, decompression should be performed in the same application session after compression.

## Huffman Coding Pipeline

1. Read the input text.
2. Calculate the frequency of each character.
3. Create leaf nodes and insert them into a minimum heap.
4. Merge the two lowest-frequency nodes repeatedly.
5. Generate prefix codes by traversing the Huffman tree.
6. Encode the text as a binary string.
7. Add padding so the data can be stored as complete bytes.
8. Write the encoded data to a binary file.
9. Remove padding and decode the bit stream during decompression.

## File Indexing

### Red-Black Tree

The Red-Black Tree implementation provides:

* File-name insertion
* Duplicate prevention
* Recursive search
* Left and right rotations
* Tree rebalancing after insertion
* Sorted file listing through in-order traversal

### Secondary File Index

`BTree.py` provides a lightweight secondary index for storing, searching, and alphabetically displaying file names.

## Project Structure

```text
huffman-coding/
├── Main.py                  # Interactive command-line application
├── HuffmanCoding.py         # Compression and decompression logic
├── RBNode.py                # Red-Black Tree implementation
├── BTree.py                 # Simple secondary file index
├── test.txt                 # Sample input file
├── test.bin                 # Sample compressed output
├── test_decompressed.txt    # Sample decompressed output
├── Project Report.docx      # Project documentation
└── README.md                # Repository documentation
```

## Learning Outcomes

This project demonstrates:

* Designing a lossless compression pipeline
* Working with bits, bytes, and binary files
* Using heaps to construct a Huffman tree
* Implementing tree rotations and balancing logic
* Searching and sorting indexed file names
* Organizing a modular Python command-line application

## Current Limitations

* The Huffman code mapping is stored in memory rather than embedded in the compressed file.
* The secondary index is a simplified educational structure rather than a complete balanced B-Tree implementation.
* The output path requested by the menu is not currently used by the decompression method.
* The application is intended for text files and educational use.
