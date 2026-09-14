# গোঁফের জোরে রাজা — Android Kivy Edition

এই project-টি মূল HTML/CSS/JavaScript movie-টির Android-compatible Python/Kivy conversion।
মূল ফাইলটি 10টি scene এবং 600-second timeline ব্যবহার করে। (Source: index.html)

## Included
- Python + Kivy
- 10-minute timeline
- 10 scene navigator
- Play / Pause / Restart
- ±5 second seek
- 0.5× / 1× / 1.5× / 2× speed
- touch timeline
- fullscreen
- animated village, sun, mountains, road, trees and six characters
- Bengali dialogue UI

## APK বানানোর সহজ পথ
Buildozer সাধারণত Linux/WSL-এ চালানো হয়।

1. Python 3 ও Buildozer install করো।
2. এই folder-এ terminal খুলে:
   `buildozer android debug`
3. build শেষ হলে `bin/` folder-এ APK পাওয়া যাবে।
4. APK Android ফোনে install করো।

### গুরুত্বপূর্ণ
এই project-এর `main.py` Android-এর জন্য। আগের Tkinter version Android-এ সরাসরি চলে না।
Bengali font আরও ভালো করতে চাইলে `NotoSansBengali-Regular.ttf` এই folder-এ রাখলে app সেটি ব্যবহার করবে।
