RSENGER — PYTHON ANDROID VERSION

What this is
-------------
This package turns the existing Rsenger HTML/Firebase application into an Android APK shell using Python + Kivy + the native Android WebView.

Why this approach
-----------------
The supplied app is a large Firebase web application: authentication, Firestore, Realtime Database, Firebase Storage, Cloudinary uploads and Lucide UI are already implemented in JavaScript. A literal rewrite of ~1,000 KB of HTML/JS into pure Python would not preserve those services reliably. This version keeps the existing working web logic and uses Python for the Android application shell.

Files
-----
main.py         Python Android app shell
index.html      Your supplied Rsenger application
buildozer.spec  Android APK build configuration

Android build
-------------
1. Use a Linux/WSL/cloud Linux environment with Buildozer. Buildozer itself is normally not run directly on Android.
2. Put all three files in one folder.
3. Run:
   buildozer android debug
4. The APK will be created under bin/.

Important
---------
- Google Sign-In still depends on the Firebase Authentication configuration and authorized domains.
- Firestore/Realtime Database security rules must protect private chats and user data. UI filtering alone is NOT security.
- Cloudinary upload presets must be configured correctly for uploads.
- The native WebView shell improves APK packaging, Android back navigation, caching, JavaScript/DOM support and media permissions, but it does not magically convert Firebase web APIs into native Python APIs.

Premium upgrades included in the shell
---------------------------------------
- Native Android WebView
- JavaScript + DOM storage enabled
- Persistent cookies for Firebase sessions
- Image/media loading and cache support
- Android back-button navigation inside the app
- Portrait app layout
- Full-screen app mode
- Network/media permissions
- Bundled offline HTML fallback
