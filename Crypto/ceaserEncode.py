message = input("Enter message to encode: ")
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
key = int(input("Enter a key: "))
translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        translatedIndex = (symbolIndex - key) % len(SYMBOLS)
        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol
print('Key #%s: %s' % (key, translated))