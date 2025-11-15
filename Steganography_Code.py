def stega_encode(message, image_path):

# transforms the message to be hidden into binary format that can be hidden in the image

    binary_message=''
    final_binary_list=[]

    for ch in message:
        ascii_format=ord(ch)
        binary_ch=format(ascii_format,'08b')
        binary_message+=binary_ch
    print(f"your secret message have been converted to binary and it's : {binary_message}")

#convert image bytes to binary list

    with open (image_path, 'rb') as image_file:
            byte_data=image_file.read()
            byte_list=list(byte_data)
            for byte in byte_list:
                binary_byte = format(byte,"08b")
                final_binary_list.append(binary_byte)
            print (final_binary_list)

stega_encode("hi","boat.png")


    




        