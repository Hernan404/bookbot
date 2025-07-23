import sys 
from stats import words_number
from stats import times_per_each
from stats import report 


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]


def get_book_text (filepath):
    with open(filepath) as f:
        text = f.read()
        return text 

def main (filepath):
    text = get_book_text(filepath)
    cant_words = words_number(text)
    times_words = times_per_each(text)
    ordenado = report(times_words)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {cant_words} total words")
   
   
    print("--------- Character Count -------")
    for n in ordenado:
        print(f'{n["name"]}: {n["num"]}')
         
    print("============= END ===============")
    


if __name__ == "__main__":
  main(filepath)

