# Image Encryption Program
This Python implementation of a custom image encryption function works by using the bitwise XOR operator, which not only temporarily renders the image unreadable as desired, but allows for reversal with the same function. Both encryption and decryption both use the same logic to operate, so the algorithm undoes itself as long as the keys match across the encryption and decryption.

To use the program, simply enter the FULL PATH of the image you would like to modify. A key can be any combination of numbers and letters(spaces will be skipped).

A custom toolbar is also included in the code. It uses the length of the image bytearray and uses simple iterators to add a tick mark to the bar display every x%.

Please feel free to use this code wherever you like, no need to credit! 
