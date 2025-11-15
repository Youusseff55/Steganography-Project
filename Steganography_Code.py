def stega_encode(message, image_path=0):

# transforms the message to be hidden into binary format that can be hidden in the image
    binary_message=''
    for ch in message:
        ascii_format=ord(ch)
        binary_ch=format(ascii_format,'08b')
        binary_message+=binary_ch
    return binary_message


print(stega_encode("hi"))