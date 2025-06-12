import socket
from deep_translator import GoogleTranslator

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5555))
server_socket.listen(1)

print("Server is listening on port 5555...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connected with {address}")

    word = client_socket.recv(1024).decode()
    lang_code = client_socket.recv(1024).decode()

    try:
        translated_word = GoogleTranslator(source='auto', target=lang_code).translate(word)
        if not translated_word:
            translated_word = "Translation error: Empty result"
    except Exception as e:
        translated_word = f"Translation error: {e}"

    client_socket.send(translated_word.encode())
    client_socket.close()
