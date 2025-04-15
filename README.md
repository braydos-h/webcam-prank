# 📸 Webcam Wallpaper Setter for Windows 11

This Python script captures a photo from your webcam and sets it as your Windows 11 desktop wallpaper.

---

## 🖼️ What the Script Does

### 1. Opens Your Webcam
Uses OpenCV to access your webcam and capture a single photo.

### 2. Saves the Photo
The image is saved as a `.bmp` file — this format is preferred by Windows for wallpapers.

### 3. Sets the Wallpaper
Uses Windows API via `ctypes` to programmatically update your desktop wallpaper with the captured
