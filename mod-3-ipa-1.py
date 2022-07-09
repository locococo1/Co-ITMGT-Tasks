'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    5 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    i=0;
    if letter==" ":
        return " ";
    else:
        for i in range(26):
            if letter==list[i]:
                if i+shift>25:
                    return list[((i+shift)%25)-1]
                else:
                    return list[i+shift]
            i=i+1;

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    10 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    i=0;
    j=0;
    message_index=[];
    for j in range(len(message)):
        if message[j]==" ":
            message_index.append(" ");
        else:
            for i in range(26):
                if message[j]==list[i]:
                    message_index.append(i);
                i=i+1;
        j=j+1;
    k=0;
    final=[];
    for k in range(len(message)):
        if message[k]==" ":
            final.append(" ");
        elif shift+message_index[k]>25:
            final.append(list[((shift+message_index[k])%25)-1]);
        else:
            final.append(list[shift+message_index[k]]);
        k=k+1;
    return "".join(final)

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    10 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    i=0;
    for i in range(26):
        if letter_shift==list[i]:
            shift=i
        i=i+1;
    i=0;
    if letter==" ":
        return " ";
    else:
        for i in range(26):
            if letter==list[i]:
                if i+shift>25:
                    return list[((i+shift)%25)-1]
                else:
                    return list[i+shift]
            i=i+1;

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    15 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    i=0;
    new_key=[1]*len(key);
    while i<len(key):
        new_key[i]=key[i];
        i=i+1;
    if len(key)<len(message):
        while i<len(message):
            new_key.append(key[i%len(key)]);
            i=i+1;
    list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    j=0;
    k=0;
    key_index=[];
    for k in range(len(message)):
        for j in range(26):
            if new_key[k]==list[j]:
                key_index.append(j);
            j=j+1;
        k=k+1;
    j=0;
    k=0;
    message_index=[];
    for k in range(len(message)):
        if message[k]==" ":
            message_index.append(" ");
        else:
            for j in range(26):
                if message[k]==list[j]:
                    message_index.append(j);
                j=j+1;
        k=k+1;
    k=0;
    final=[];
    for k in range(len(message)):
        if message[k]==" ":
            final.append(" ");
        elif key_index[k]+message_index[k]>25:
            final.append(list[((key_index[k]+message_index[k])%25)-1]);
        else:
            final.append(list[key_index[k]+message_index[k]]);
        k=k+1;
    return "".join(final)

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.
    
    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of 
        parchment that contained a string of apparent gibberish. The parchment, 
        when read using the scytale, would reveal a message due to every nth 
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number. 
        For this example, we will use "INFORMATION_AGE" as 
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of 
        the shift. If it is not, add additional underscores 
        to the end of the message until it is. 
        In this example, "INFORMATION_AGE" is already a multiple of 3, 
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message. 
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message. 
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case, 
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    i=0;
    new_message=[1]*len(message);
    while i<len(message):
        new_message[i]=message[i];
        i=i+1;
    j=len(message)%shift;
    if j>0:
        while j<shift:
            new_message.append("_");
            j=j+1;
    i=0;
    encoded=[];
    for i in range(len(new_message)):
        encoded.append(new_message[(i//shift)+(len(new_message)//shift)*(i%shift)]);
        i=i+1;
    return "".join(encoded)

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message_index=[];
    i=0;
    for i in range(len(message)):
        message_index.append((i//shift)+(len(message)//shift)*(i%shift));
        i=i+1;
    j=0;
    k=0;
    og=[1]*len(message);
    for k in range(len(message)):
        for j in range(len(message)):
            if k==message_index[j]:
                og[k]=message[j];
            j=j+1;
        k=k+1;
    return "".join(og)