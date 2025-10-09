import cv2

# image load
image = cv2.imread("python_code.png")

if image is not None:
    # image display
    cv2.imshow("Python Code", image) # image + window title
    cv2.waitKey(0) # display screen ko pause pe rakhne ka kaam karega
    # 0 = keyboard pe koi bhi button pe click karu toh ban hona chiaye display
    cv2.destroyAllWindows() # close karne ke liye window ko

    # changes + save
    success = cv2.imwrite("output_py.jpg", image) # edting file name + new or update path
    if success:
        print("Image Save succesfully as 'output_py.jpg'")
    else:
        print('Failed to save an image')
else:
    print('Error: Image Not Found')
