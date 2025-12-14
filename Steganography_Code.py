def stega_encode(message, image_path, output_image):

# transforms the message to be hidden into binary format that can be hidden in the image

    binary_message=''
    final_binary_list=[]

    if len(binary_message)==0:
        raise ValueError("Message is empty")
    
# Check if input image is BMP format
    if not image_path.lower().endswith('.bmp'):
        raise ValueError("Input image must be a BMP file")
# Check if image path is different than output path
    if image_path==output_image:
        raise ValueError("Output image path can't be the same as the input")
    
    for ch in message:
        ascii_format=ord(ch)
# Check if ch is ascii
        if ascii_format>127:
            raise ValueError(f"Non ascii charachter {ch}, please insert ascii charachters only")
        
        binary_ch=format(ascii_format,'08b')
        binary_message+=binary_ch
    binary_message += "00000000"

#convert image bytes to binary list

    with open (image_path, 'rb') as image_file:
            byte_data=bytearray(image_file.read())
# Check if the message fits the image
            if len(binary_message)>len(byte_data):
                raise ValueError("Message too long for this image")
            
            byte_list=list(byte_data)
            for byte in byte_list:
                binary_byte = format(byte,"08b")
                final_binary_list.append(binary_byte)
 
#replacement

    for i in range(len(binary_message)):
        old_byte = final_binary_list[i]
        new_byte = old_byte[:-1] + binary_message[i]
        final_binary_list[i] = new_byte

    new_byte_values = [int(b, 2) for b in final_binary_list]
    stego_data= bytearray(new_byte_values)
    with open(output_image, 'wb') as image_file:
         image_file.write(stego_data)