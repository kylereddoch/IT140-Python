def pyramid_volume(base_length, base_width, pyramid_height):
    b_area = length * width
    volume = b_area * (height * 1/3)
    return volume


length = float(input())
width = float(input())
height = float(input())
print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(length, width, height))
