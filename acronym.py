def generate_acronym(input_string):
    
    
    words = input_string.split()
    
   
    acronym = ''.join(word[0].upper() for word in words)
    
    return acronym


def main():
   
    text = input("Enter a phrase to generate an acronym: ")
    
    
    result = generate_acronym(text)
    print(f"Acronym: {result}")

if __name__ == "__main__":
    main()