RSENGER PREMIUM V3
==================

This package keeps the existing Firebase-powered Rsenger web application and packages it as an Android application using Python + Kivy + Android WebView.

Files
-----
index.html              Existing Rsenger app logic/UI
style.css               Premium visual layer and Android/mobile refinements
main.py                 Python/Kivy Android shell
buildozer.spec          APK build configuration
assets/rsenger_logo.png App logo/icon
.github/workflows/...   GitHub Actions workflow for cloud APK builds
FIREBASE_RULES_WARNING  Important security note about the rules supplied for this project
index.backup.html       Original HTML backup

GitHub / Android build
----------------------
1. Upload the project files to a GitHub repository.
2. Make sure buildozer.spec is in the repository root.
3. Open GitHub -> Actions.
4. Select "Build Rsenger Android APK".
5. Run workflow (or push to main/master).
6. After the build finishes, open the workflow run and download the APK artifact named Rsenger-Premium-APK.

The workflow uses the Buildozer GitHub Action. Buildozer itself is normally run in Linux/CI rather than directly on Android.

Important functional notes
--------------------------
- The existing app uses Firebase Auth, Firestore, Realtime Database, Firebase Messaging/Storage and Cloudinary/webtonative integrations.
- The existing HTML was retained rather than pretending a ~1 MB web app had been fully rewritten into native Python.
- Google Sign-In inside a local Android WebView can require additional Firebase/Google configuration; a production native Google login may need Android Firebase configuration and package signing fingerprints.
- The existing app references style.css; this package now includes that missing stylesheet.
- The supplied Firestore rules are wide open. See FIREBASE_RULES_WARNING.txt before production use.
- Cloudinary upload presets must remain valid for image/file uploads.

Build command (Linux/CI)
------------------------
buildozer android debug

APK output
----------
The Buildozer APK is placed in bin/ when built locally. In GitHub Actions it is uploaded as an artifact.
