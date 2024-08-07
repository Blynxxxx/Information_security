
CIPHERTEXT = "pchhlptizjhfatcrifnkhctoqvgxbusvwggszbjchmwvghnvetdsqnrkxtslmdbsuczhttiysunjtcldlhcwjkqkitktmsumgtjthlipmwvghfnxgxfdxwtacmoiyxgjvlmjxgftiytnckwoudnnvfdwexekgdoemxfbvihmwzgwsrxpiszcfxapivyfbcdouegmhnwwbrxgzgkudettcpgqwxkwhmunryovmgtufcgxwmryoxwvbdegkuxxiysquvngrzslqitihbihvdeqhunbcxhkynhhzbjvkwhrzouwvizcqmfbhtivmgwhftdljtkvphyplxeuoykgiysvypltkvdnvatislmqgapcqyuxacsucptrfbwcpndlggiwuavoxwvbdeqguvatisdlgfpemeoaxgjoqxuxacsumyadtcqnkgjfivfamgrrhuubcxzhwqfbfrlnauxugdlgfpkqkyftcuqoycktucyytmxdsdwehguwqavhiysdoemxfbuonxhtrdmcktkmscetacmrjggqzrwbgutjhnhqpcvldgretftdwftxjovyengzhlyufpiyhnunryovnjxcvkbitdhkcfegqryoqaggnjswbgkteczyzbhkbxggkdlgrhnbcvpuimxgjwwyuljtvdmehbdghwvapkcizgkhvfycexhwcunttszbjcplttiucvbtjadlmxijcqfkgtsfregkhvlkcdbikvhmcftwzdquthdcuyehcmsqnkhcrzrhnbcvoxwvbdegdhfhuwsuhqydiarzrkdksfnkhckcecfwtigfixxgruhihlttiucvrxjgxyuydiqguubhcwpcvxsnoqacgscsxhiigfdrmgwpjqkyoxufffipwjthlhilttiuycgsrbrhafdlgfxclwfkhpgkiywvmeatdslmkghvqxlgtcurryugdkogxtxhjhkyuxrlflnkxhdouegmpjdhwvhutrdmyxlzzoxklrlgvnjbhzbvyemxfb"
from collections import Counter
KEY_LENGTH = 7
cryptograms = [''] * KEY_LENGTH # Initialize an empty list to store the cryptograms
def find_cryptogram(ciphertext, key_length):
    """Extracts the cryptograms from the ciphertext based on the given key length."""
    # Iterate through the ciphertext and extract the characters for each cryptogram
    for i in range(1,len(ciphertext) + 1):
        # Determine which cryptogram the current character should be added to based on the remainder of the index divided by the key length
        if i % key_length == 1:
            cryptograms[0]= cryptograms[0] + ciphertext[i - 1]
        elif i % key_length == 2:
            cryptograms[1]= cryptograms[1] + ciphertext[i - 1]
        elif i % key_length == 3:
            cryptograms[2]= cryptograms[2] + ciphertext[i - 1]
        elif i % key_length == 4:
            cryptograms[3]= cryptograms[3] + ciphertext[i - 1]
        elif i % key_length == 5:
            cryptograms[4]= cryptograms[4] + ciphertext[i - 1]
        elif i % key_length == 6:
            cryptograms[5]= cryptograms[5] + ciphertext[i - 1]
        elif i % key_length == 0:
            cryptograms[6]= cryptograms[6] + ciphertext[i - 1]
    # Process the extracted cryptograms
    for i in range(7):
        print(f"cryptogram {i+1}: {cryptograms[i]}")
    print()
    # Process the extracted cryptograms
    for j in range(7):
        # Use the Counter class from the collections module to count the frequency of each character in the current cryptogram
        cryptograms[j] = Counter(cryptograms[j])
        # Display characters in the current cryptogram
        print(f"cryptogram {j+1}: {cryptograms[j]}")
    print()
    # Process the extracted cryptograms
    for k in range(7):
        # Use the Counter class from the collections module to count the frequency of each character in the current cryptogram
        cryptograms[k] = Counter(cryptograms[k]).most_common(4)
        # Display the 4 most common characters in the current cryptogram
        print(f"cryptogram {k+1}: {cryptograms[k]}")


find_cryptogram(CIPHERTEXT, KEY_LENGTH)
print()
print("Determine the key letter - Assume that ’e’ is the most common letter in English texts")


def find_key(cryptograms):
    """Determines the key for each cryptogram in the provided list of cryptograms."""
    vigenere_index = "abcdefghijklmnopqrstuvwxyz"  # Alphabet string for indexing

    # Iterate through each cryptogram in the list
    for i, cryptogram in enumerate(cryptograms):
        keys = []
        # Iterate through letters in the current cryptogram
        for index, (letter, count) in enumerate(cryptogram):
            # Calculate the index of the key letter
            key_index = (vigenere_index.index(letter) - vigenere_index.index('e')) % 26
            # Get the key letter from the alphabet string
            key_letter = vigenere_index[key_index]
            # Add the key letter to the list of keys
            keys.append(key_letter)
        # Display the keys for the current cryptogram
        print(f"cryptogram{i + 1}: {keys}")

find_key(cryptograms)

