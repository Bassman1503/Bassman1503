
# An example of a sequence of a Unicode characters
#
string = 'Un1c0dé st1ng§'
print(string)
print(type(string))

# An example of string encoding to UTF-8 format
# UTF-8 is useful for transmitting textual data 
# on the web, where it is the dominant text format.
#
bytesObject = string.encode('utf-8')
print(bytesObject)

# An example of bytes object decoding to string.
#
decodedBytesObject = bytesObject.decode('utf-8')
print(decodedBytesObject)