morse= { 'A':'.-',     'B':'-...','C':'-.-.',   'D':'-..','E':'.', 'F':'..-.',   'G':'--.',     'H':'....',
                    'I':'..',     'J':'.---',    'K':'-.-',
                    'L':'.-..',   'M':'--',      'N':'-.',
                    'O':'---',    'P':'.--.',    'Q':'--.-',
                    'R':'.-.',    'S':'...',     'T':'-',
                    'U':'..-',    'V':'...-',    'W':'.--',
                    'X':'-..-',   'Y':'-.--',    'Z':'--..',
                    '1':'.----',  '2':'..---',   '3':'...--',
                    '4':'....-',  '5':'.....',   '6':'-....',
                    '7':'--...',  '8':'---..',   '9':'----.',
                    '0':'-----',  ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.',   '-':'-....-',
                    '(':'-.--.',  ')':'-.--.-', '':'/'}

english = {
    '.-':'A',     '-...':'B',   '-.-.':'C',   '-..':'D',
    '.':'E',      '..-.':'F',   '--.':'G',     '....':'H',
    '..':'I',     '.---':'J',   '-.-':'K',     '.-..':'L',
    '--':'M',     '-.':'N',     '---':'O',     '.--.':'P',
    '--.-':'Q',   '.-.':'R',    "...":'S',     '-':'T',
    '..-':'U',    "...-":'V',   '.--':'W',     '-..-':'X',
    '-.--':'Y',   '--..':'Z',   '.----':'1',   '..---':'2',
    "...--":'3',  "....-":'4',  ".....":'5',   "-....":'6',
    "--...":'7',  "---..":'8',  "----.":'9',   "-----":'0',
    "--..--":", ", ".-.-.-":'.',"..--..":'?',  "-..-.":'/',
    "-....-":'-',"-.--.":'(',  "-.--.-":')',"/":' '
}

option = input('Do you wish to translate English into morse code or morse code into English?(Enter 1 or 2):')
if option == '1':
    words = input('Enter text here:').upper()
    translated = ''
    for char in words:
        translated += morse[char.strip()] + " "
    print(translated)

elif option == '2':
    words = input('Enter morse here (use spaces between letters and slashes for words):')
    translated =''
    morse_char = words.split()
    for char in morse_char:
        translated += english[char]
    print(translated)