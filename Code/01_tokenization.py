import tiktoken

enc= tiktoken.encoding_for_model("gpt-4o")

text= "Hello , i  am atul"
tokens= enc.encode(text)
print("Tokens are:",tokens)
# Output: Tokens are: [13225, 1366, 575, 220, 939, 540, 361]

decoded_text= enc.decode(tokens)
print("Decoded text is:",decoded_text)
# output: Decoded text is: Hello , i  am atul 