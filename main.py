def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()
    
    count = get_num_words(file_contents)

    lowered_string = file_contents.lower()
    my_dic = {}
   
    
    for char in lowered_string:
        if char in my_dic:
            my_dic[char] += 1
        else:
            my_dic[char] =1

    my_list = my_dic.items()
    print(f"--- Begin report of {file} ---")
    print(f"{count} words found in the document")
    for x,y in my_list:
        if x.isalpha() == 1:
            print(f"The '{x}' character was found {y} times")

def get_num_words(text):
    words = text.split()
    return len(words)

main()