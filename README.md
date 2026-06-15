# Recipe Search Engine

📖 Project Description

This project is a terminal-based Python application designed to help users find the perfect recipe based on their current ingredients or emotional mood (e.g., "lazy", "sweet").

The core of the program relies on an inverted index data structure. It scans a local directory of text-based recipe files, cleans and parses the text, and maps individual keywords to their corresponding source files. When a user inputs a query, the search engine utilizes flexible set operations (UNION / OR matching) to instantly surface all relevant recipes.

To elevate the command-line interface (CLI) user experience, the application features custom, meticulously aligned cooking-themed ASCII art that dynamically changes based on the user's workflow:

A steaming cooking pot welcomes the user at launch.

A sharp chef's knife and fork graphic highlights successful recipe matches.

A slice of dessert cake bids the user goodbye upon exit.

🛠️ Key Features

Inverted Indexing: Efficiently builds a dictionary mapping cleaned, lowercase words to sets of matching filenames.

Smart Text Parsing: Standardizes user inputs and text content by dynamically stripping punctuation and ignoring case sensitivity.

Multi-Word Query Support: Allows users to input multiple ingredients or moods simultaneously, returning a combined pool of matching dishes.

Instant Exit: A streamlined input loop that catches empty strings and closes the program instantly on a single blank "Enter."

💻 My Experience Developing It

Building this project as part of Stanford's Code in Place 2026 was an incredible learning experience that bridged foundational Python syntax with practical data structures and UI design.
