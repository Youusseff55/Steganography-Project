def stega_encode(message, image_path, output_image):

# transforms the message to be hidden into binary format that can be hidden in the image

#check if message is empty
    if len(message)==0:
        raise ValueError("Message is empty")
    
# Check if input image is BMP format
    if not image_path.lower().endswith('.bmp'):
        raise ValueError("Input image must be a BMP file")
# Check if image path is different than output path
    if image_path==output_image:
        raise ValueError("Output image path can't be the same as the input")
    if message.lower().endswith('.txt'):
        try:
            with open (message, 'r') as text_file:
                message_content=text_file.read().strip()
                message=message_content
        except FileNotFoundError:
            raise ValueError(f'Text file {message} not found')
        except:
            raise ValueError(f'Error reading text file: {message}')

# transforms the message to be hidden into binary format that can be hidden in the image    
    binary_message=''
    final_binary_list=[]
    
    for ch in message:
        ascii_format=ord(ch)
# Check if ch is ascii
        if ascii_format>127:
            raise ValueError(f"Non ascii charachter {ch}, please insert ascii charachters only")
        
        binary_ch=format(ascii_format,'08b')
        binary_message+=binary_ch
    binary_message += "00000000"

#convert image bytes to binary list
    try:
        with open (image_path, 'rb') as image_file:
            byte_data=bytearray(image_file.read())
    except FileNotFoundError:
            raise ValueError(f"File {image_path} not found")
    except:
            raise ValueError(f"can't read {image_path}")
# Check if the message fits the image
    if len(binary_message)>len(byte_data):
        raise ValueError("Message too long for this image")
            
    byte_list=list(byte_data)
    for byte in byte_list:
        binary_byte = format(byte,"08b")
        final_binary_list.append(binary_byte)
#replacement

    for i in range(54,54+len(binary_message)):
        old_byte = final_binary_list[i]          
        new_byte = old_byte[:-1] + binary_message[i-54]
        final_binary_list[i] = new_byte

    new_byte_values = [int(b, 2) for b in final_binary_list]
    stego_data= bytearray(new_byte_values)
    with open(output_image, 'wb') as image_file:
         image_file.write(stego_data)

def stega_decode(stego_image):
    # Read image bytes
    try:
        with open(stego_image, 'rb') as f:
            byte_data = bytearray(f.read())
    except FileNotFoundError:
        raise ValueError(f"File {stego_image} not found")
    except:
        raise ValueError(f"can't read {stego_image}")

    
    # Convert each byte to binary string starting from offset 54
    binary_bytes = []
    for i in range(54, len(byte_data)):
        binary_bytes.append(format(byte_data[i], '08b'))
    
    # Extract LSBs to get the hidden message bits
    message_bits = ''
    for b in binary_bytes:
        message_bits += b[-1]  # take the last bit
    
    # Split the bits into 8-bits
    chars = []
    for i in range(0, len(message_bits), 8):
        byte = message_bits[i:i+8]
        if len(byte) < 8:  # incomplete byte at the end
            break
        if byte == '00000000':  # stop at delimiter
            break
        chars.append(chr(int(byte, 2)))  # convert binary to character
    
    # Join the characters to get the message
    message = ''.join(chars)
    return message


def user_interface():
    print("\n=== BMP Steganography ===")
    
    while True:
        print("\n1. Hide message")
        print("2. Extract message")  
        print("3. Quit")
        
        opt = input("\nChoice: ").strip()
        
        if opt == '1':
            msg = input("Message: ")
            in_img = input("Input BMP: ")
            out_img = input("Output BMP: ")
            
            try:
                stega_encode(msg, in_img, out_img)
                print("✓ Done!")
            except Exception as e:
                print(f"✗ Error: {e}")
                
        elif opt == '2':
            img = input("Stego BMP: ")
            
            try:
                result = stega_decode(img)
                print(f"\nExtracted: {result}")
            except Exception as e:
                print(f"✗ Error: {e}")
                
        elif opt == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice")

user_interface()