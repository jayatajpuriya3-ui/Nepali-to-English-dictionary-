# nepali_english_dictionary.py

# Nepali to English Dictionary
dictionary = {
    "namaste": "hello",
    "pani": "water",
    "bato": "road",
    "ghar": "house",
    "dhan": "rice",
    "dost": "friend",
    "maya": "love",
    "timi": "you",
    "kinnu": "buy",
}

print("📖 Nepali-English Dictionary")
print("Type 'exit' to quit.\n")

while True:
    word = input("Enter a Nepali word: ").strip().lower()
    
    if word == "exit":
        print("Thank you for using the dictionary. 🙏")
        break
    
    translation = dictionary.get(word)
    if translation:
        print(f"✅ English: {translation}\n")
    else:
        print("❌ Word not found in dictionary.\n")