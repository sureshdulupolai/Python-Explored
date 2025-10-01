import cv2

image = cv2.imread("python_code.png")

def show(new_image, title = "GrayScale Image"):
    cv2.imshow(title, new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def saveimg(filename):
    message = cv2.imwrite(f"{filename}.jpg", new_image)
    if message:
        return True
    return False

if image is not None:
    new_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    user_input = int(input("1. Show \n2. Save &\n3. Both => "))
    if user_input == 1:
        new_title = input("Any Title or Default : ")
        if not new_title:
            new_title = 'GrayScale Imgage'
        show(new_image, title=new_title)
        
    elif user_input == 2:
        Filename = input("Enter File Name: ")
        check_img = saveimg(filename=Filename)
        if check_img:
            print(f'Image Save Successfully with filename : {Filename}.jpg')

    elif user_input == 3:
        Filename = input("Enter File Name: ")
        check_img = saveimg(filename=Filename)
        if check_img:
            print(f'Image Save Successfully with filename : {Filename}.jpg')
            show(new_image, title=Filename.title())

    else:
        print("Oops!, we cannot connect to user input...")

    print("Every Done Successfully")
    
else:
    print("image cant upload successfully to your system")