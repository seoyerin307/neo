import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

tokens = enc.encode("Hello wolrd")
print(len(tokens))
print(tokens)
print('-' * 50)
print(enc.decode(tokens))
print(enc.decode_tokens_bytes(tokens))