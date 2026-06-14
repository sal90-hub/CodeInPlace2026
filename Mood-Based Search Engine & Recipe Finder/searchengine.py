import os
import string

def clean_word(word):
    """
    Cleans a word by converting it to lowercase and stripping punctuation.
    """
    if isinstance(word, list):
        if len(word) > 0:
            word = str(word)
        else:
            return ""

    return str(word).strip(string.punctuation).lower()

def load_recipes(directory):
    """
    Reads all text files in the given directory.
    Returns a dictionary mapping filenames to their titles.
    """
    db = {}
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        return db

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    title = file.readline().strip()
                    db[filename] = title if title else filename
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return db

def build_index(directory):
    """
    Builds an inverse index for the search engine.
    Maps words to the sets of files that contain them.
    """
    index = {}
    if not os.path.isdir(directory):
        return index

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    words = content.split()

                    for word in words:
                        cleaned = clean_word(word)
                        if cleaned:
                            if cleaned not in index:
                                index[cleaned] = set()
                            index[cleaned].add(filename)
            except Exception as e:
                print(f"Error indexing {filename}: {e}")
    return index

def lookup_query(index, query):
    """
    Searches the index for the user's query.
    Supports multi-word searches using flexible set UNION (OR search).
    """
    query_words = query.split()
    if not query_words:
        return set()

    # Get initial results for the first word
    first_word = clean_word(query_words)
    results = index.get(first_word, set()).copy()

    # Loop through all remaining words and UNION them (OR search)
    for word in query_words[1:]:
        cleaned = clean_word(word)
        word_files = index.get(cleaned, set())
        results = results.union(word_files)

    return results

def main():
    recipe_dir = "recipes"

    # 🍳 Straightened Cooking Pot (Right smoke column pulled left)
    print("=" * 55)
    print(r"""
        (    (    (
           )    )    )
         ___________
        |___________|
         \         /     
          \_______/      
      [===============]
    """)
    print("  Welcome to the Mood & Ingredient Recipe Search Engine!")
    print("=" * 55)
    print(f"Indexing recipes from the '{recipe_dir}' folder...")

    recipe_titles = load_recipes(recipe_dir)
    index = build_index(recipe_dir)

    print(f"Successfully indexed {len(recipe_titles)} recipes.")
    print("Try searching for ingredients (e.g., 'butter sugar'), moods ('lazy'), or both!\n")

    while True:
        user_input = input("What are you craving? (Leave blank to quit): ")
        query = user_input.strip()

        if query == "":
            # 🍰 Cake Drawing on instant exit
            print(r"""
                     ~
                    ( )
                _.-'_.-'_.-._
              ('_._'_._'_._'_)
               \            /
                \_._._._._./
            """)
            print("Goodbye! Happy cooking!")
            break

        matching_files = lookup_query(index, query)

        if not matching_files:
            print(f"No recipes found matching '{query}'. Try something else!\n")
        else:
            # 🍴 Clean Fork and Distinct Kitchen Chef's Knife
            print(r"""
                   _ _       _
                  | | |     | \
                  | | |     |  \
                  |_|_|     |   \
                    |       |___|
                    |         |
                    |         |
                    |         |
                    |         |
                    |         |
            """)
            print(f"Results for '{query}' (OR match):")
            print("-" * 55)
            for i, filename in enumerate(matching_files, start=1):
                filepath = os.path.join(recipe_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        recipe_content = file.read()
                        print(f"[Match #{i}] From File: {filename}")
                        print(recipe_content)
                        print("-" * 55)
                except Exception as e:
                    title = recipe_titles.get(filename, filename)
                    print(f"{i}. Title: {title} (Could not read full text: {e})")
            print()

if __name__ == "__main__":
    main()