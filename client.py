import socket

LANGUAGES = {
    "french": "fr",
    "spanish": "es",
    "german": "de",
    "arabic": "ar",
    "chinese": "zh-cn",
    "japanese": "ja",
    "italian": "it",
    "russian": "ru",
    "portuguese": "pt",
    "english": "en",
    "swahili": "sw",
    "hausa": "ha",
    "hindi": "hi",
    "korean": "ko",
    "dutch": "nl",
    "greek": "el",
    "polish": "pl",
    "romanian": "ro",
    "turkish": "tr",
    "swedish": "sv"
}

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    word = input("\nEnter the word to translate: ").strip()
    client_socket.send(word.encode())

    print("\nSupported languages:")
    for name in LANGUAGES:
        print("-", name.title())

    language_name = input("\nEnter the language name: ").strip().lower()

    if language_name in LANGUAGES:
        lang_code = LANGUAGES[language_name]
        client_socket.send(lang_code.encode())
        translated = client_socket.recv(1024).decode()
        print("\nTranslated word:", translated)
    else:
        print("\nLanguage not supported.")
        client_socket.send("invalid".encode())

    client_socket.close()

    while True:
        again = input("\nDo you want to translate again? (yes/no): ").strip().lower()
        if again in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no' only.")

    if again == 'no':
        print("Exiting...")
        break
    
