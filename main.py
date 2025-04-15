import cv2
import os
import ctypes
#THIS IS ALL ETHICALY AND USED FOR LEARNING ONLY 
def capture_and_set_wallpaper():
    # Open the default webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("")
        return

    # Capture one frame
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("")
        return

    user_dir = os.environ.get("USERPROFILE", os.getcwd())
    wallpaper_path = os.path.join(user_dir, "wallpaper.bmp")  # BMP format for Windows compatibility

    # Save the captured image as a BMP file
    #BMP is better becusae it works better with windows and is more compatible with it
    # The image is saved in the user's home directory as wallpaper.bmp
    # The file will be overwritten if it already exists
    if cv2.imwrite(wallpaper_path, frame):
        print(f" {wallpaper_path}")
    else:
        print("")
        return

    # Set the BMP file as the desktop wallpaper
    # SPI_SETDESKWALLPAPER = 20, and 3 is used to update the INI file and notify the system of the change.
    # The wallpaper is set to the captured image
    result = ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)
    if result:
        print("")
    else:
        print("")

if __name__ == "__main__":
    capture_and_set_wallpaper()
