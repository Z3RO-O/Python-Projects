# Steganography

import cv2  # pip install opencv-python


def splitbyte(by):
    first_three_bits = by >> 5
    mid_three_bits = (by >> 2) & 7
    last_two_bits = by & 3
    return first_three_bits, mid_three_bits, last_two_bits


def embed(vessel_image, target_image):
    # load the vessel_image into memory
    mem_image = cv2.imread(vessel_image)
    print(type(mem_image))
    print(mem_image.shape)

    # dummy data to embed
    data = [x for x in range(65, 91)]
    size = len(data)
    index = 0

    # embedding loop
    r = 0
    while r < mem_image.shape[0] and index < size:
        c = 0
        while c < mem_image.shape[0] and index < size:
            # Free 2,3,3 bits of the pixel
            mem_image[r, c, 0] &= 252  # Blue band
            mem_image[r, c, 1] &= 248  # Green band
            mem_image[r, c, 2] &= 248  # Red band

            bits = splitbyte(data[index])
            print(data[index], bits)
            # Merge the bits into the bands
            mem_image[r, c, 0] = bits[2]  # Blue band
            mem_image[r, c, 1] = bits[1]  # Green band
            mem_image[r, c, 2] = bits[0]  # Red band

            # next val to embed
            index += 1

            c += 1
        r += 1
    # Save back the image
    cv2.imwrite(target_image, mem_image)


def main():
    embed('f:/snake.jpg', 'f:/new_snake.png')
    print('OK')


main()
