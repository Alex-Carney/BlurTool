import numpy as np
from PIL import Image




def convolution(image, kernel):
    """
    Performs convolution on an entire image with a given kernel
    @author Jane O'Reilly
    :param image: A PIL image object
    :param kernel: A square matrix with odd dimension
    :return: convolved image
    """

    kernel_dim = int(np.sqrt(np.size(kernel)))
    img_row = np.shape(image)[0]
    img_col = np.shape(image)[1]
    img_colors = np.shape(image)[2]

    image_array = np.array(image)

    convoluted_img = np.array(image)
    #convoluted_img = np.array(image)

    ker_idx_max = kernel_dim - 2
    for row in range(ker_idx_max, img_row - ker_idx_max):
        for col in range(ker_idx_max, img_col - ker_idx_max):
            result = np.array([0])
            """
            The kernel has the following representation (assuming 3x3):
            [(-1, -1) (-1, 0) (-1, 1)]
            [(0,  -1) (0,  0) (0,  1)]
            [(1,  -1) (1,  0) (1,  1)]
            Therefore, our parameter of interest is kernel_dim - 2
            """
            for ker_row in range(-ker_idx_max, ker_idx_max + 1):
                for ker_col in range(-ker_idx_max, ker_idx_max + 1):
                    # print(str(row - ker_row) + " + " + str(col - ker_col))
                    result = result + (kernel[ker_row + ker_idx_max, ker_col + ker_idx_max]
                               * image_array[(row - ker_row), (col - ker_col)])
            convoluted_img[row, col] = result

    final_image = Image.fromarray(convoluted_img)
    return final_image


def convolution_2(image, kernel, starting_points, range_around):
    """
    Performs convolution on a specified section with a given kernel
    @author Jane O'Reilly
    :param image: A PIL image object
    :param kernel: A square matrix with odd dimension
    :param starting_point: the starting pixel value, must be within the dimensions of the image and be a 1x2 array
    :param range_around: the area that will be convolved
    :return: convolved image
    """

    kernel_dim = int(np.sqrt(np.size(kernel)))
    img_row = np.shape(image)[0]
    img_col = np.shape(image)[1]

    image_array = np.array(image)

    # convoluted_img = np.zeros((img_row, img_col))

    ker_idx_max = 1 if kernel_dim == 3 else 2

    convoluted_img = np.array(image)

    # starting and ending row
    start_row = starting_points[0] - range_around if (starting_points[0] - range_around) >= 0 else 0
    end_row = starting_points[0] + range_around if (starting_points[0] + range_around) <= img_row - ker_idx_max else (img_row-ker_idx_max)

    # starting and ending column
    start_col = starting_points[1] - range_around if (starting_points[1] - range_around) >= 0 else 0
    end_col = starting_points[1] + range_around if (starting_points[1] + range_around) <= img_col - ker_idx_max else (img_col-ker_idx_max)


    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            result = 0
            """
            The kernel has the following representation (assuming 3x3):
            [(-1, -1) (-1, 0) (-1, 1)]
            [(0,  -1) (0,  0) (0,  1)]
            [(1,  -1) (1,  0) (1,  1)]
            Therefore, our parameter of interest is kernel_dim - 2
            """
            for ker_row in range(-ker_idx_max, ker_idx_max + 1):
                for ker_col in range(-ker_idx_max, ker_idx_max + 1):
                    # print(str(row - ker_row) + " + " + str(col - ker_col))
                    result += (kernel[ker_row + ker_idx_max, ker_col + ker_idx_max] * image_array[
                        (row - ker_row), (col - ker_col)]).astype(np.int16)
            convoluted_img[row, col] = result

    final_image = Image.fromarray(convoluted_img)
    return final_image


def main():

    def load_image(image_file):
        img = Image.open(image_file)
        return img

    myImage = Image.open("jeremy.jpg");
    myImage.show();


    image = load_image("jeremy.jpg")


    print(image.size)

    converted_img = np.array(image.convert('RGB'))
    print(converted_img)

    image_row = np.ndim(converted_img)
    print(image_row)

    image_size = np.size(converted_img)
    print(image_size)

    imgGray = image.convert('L')
    imgGray.save('test_gray.jpg')

    b_w_img = np.array(imgGray)
    print(b_w_img)

    print(np.size(imgGray))
    print(np.ndim(imgGray))

    print(range(1,np.size(imgGray)[0]-2))


    kernal=np.zeros((3,3))
    print(np.size(kernal))
    print(np.sqrt(np.size(kernal)))

    # convolution(imgGray,kernal).show()

    kernal_gauss = np.array([[1/16, 2/16, 1/16], [2/16, 4/16, 2/16], [1/16, 2/16, 1/16]])
    # convolution(converted_img, kernal_gauss).show()
    # convolution(imgGray,kernal_gauss).show()
    #
    # kernal_box = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])
    # convolution(imgGray,kernal_box).show()
    #
    convolution(converted_img, kernal_gauss).show()


if __name__ == '__main__':
    main()

