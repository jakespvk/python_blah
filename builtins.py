if __name__ == "__main__":
    word: str = "hello";
    word = word.capitalize();
    print(word);
    word = word.upper();
    print(word);
    word = word.lower();
    print(word);
    word = word.replace("l", "-");
    print(word);
    word = "hehho";
    word = word[0] + word[1:len(word)].replace(word[0], "-");
    print(word);
