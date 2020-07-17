virginAlphabet = input()
chadAlphabet = input()
rawText = list(input())
readyText = list(input())
def cryptEncrypt(_text, _firstAlphabet, _secondAlphabet):
    lenAlphabet = len(_firstAlphabet)
    lenText = len(_text)
    for indRawChar in range(lenText):
        for i in range(lenAlphabet):
            if _text[indRawChar] == _firstAlphabet[i]:
                _text[indRawChar] = _secondAlphabet[i]
                break
    print(''.join(_text))
cryptEncrypt(rawText, virginAlphabet, chadAlphabet)
cryptEncrypt(readyText, chadAlphabet, virginAlphabet)