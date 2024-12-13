def madlibs():
    print("Welcome to Mad Libs!")
    print("Fill in the blanks with the appropriate words.")

    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (past tense): ")
    adverb1 = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter one more noun: ")
    verb2 = input("Enter a verb: ")
    adverb2 = input("Enter another adverb: ")

    story = f"""
    Today, I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree.
    It {verb1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}.
    I got some peanuts and passed them through the cage to a gigantic gray {noun3}.
    It {verb2} {adverb2} and smiled at me. What a fun day at the zoo!
    """
    
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    madlibs()
