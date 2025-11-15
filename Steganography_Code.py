def stega_encode(message, image_path):

# transforms the message to be hidden into binary format that can be hidden in the image

    binary_message=''
    final_binary_list=[]

    for ch in message:
        ascii_format=ord(ch)
        binary_ch=format(ascii_format,'08b')
        binary_message+=binary_ch

#convert image bytes to binary list

    with open (image_path, 'rb') as image_file:
            byte_data=bytearray(image_file.read())
            byte_list=list(byte_data)
            for byte in byte_list:
                binary_byte = format(byte,"08b")
                final_binary_list.append(binary_byte)
            print(final_binary_list[0:10])

#replacement

    for i in range(len(binary_message)):
        old_byte = final_binary_list[i]
        new_byte = old_byte[:-1] + binary_message[i]
        final_binary_list[i] = new_byte
    print(final_binary_list[0:10])
stega_encode("h","boat.png")
print(format(ord("h"),'08b'))


         