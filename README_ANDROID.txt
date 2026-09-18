RSENGER ANDROID BUILD - V3.1

This version changes the Android wrapper from Kivy + an embedded file:// WebView to
python-for-android's WebView bootstrap.

Why:
- The existing app is already an HTML/CSS/JavaScript app.
- Kivy was only being used to create a WebView/splash wrapper.
- There are documented Android/arm64 cases where Kivy can crash around its window
  initialization, while the p4a WebView bootstrap is designed to host a webpage
  from a Python web server.

Files:
- index.html            = main web app
- index.backup.html     = backup copy
- style.css             = premium visual layer
- main.py               = tiny Flask local web server
- buildozer.spec        = Android build configuration
- assets/rsenger_logo.png = app logo
- .github/workflows/build-apk.yml = GitHub Actions APK build

Build:
1. Push all files to GitHub.
2. Open Actions -> Rsenger Android APK.
3. Run workflow.
4. Download the Rsenger-APK artifact.
5. Inside it, download the generated .apk and install it on Android.

Important:
- This fixes the likely Kivy/SDL runtime-crash path. It does not rewrite the web
  app's Firebase code.
- Firebase email/password, Firestore, Storage, Cloudinary, etc. still depend on
  their existing web configuration and security rules.
- Google sign-in may still require Firebase Authorized Domains / OAuth configuration
  appropriate for the local WebView origin. That is a separate authentication
  configuration issue, not the Android launch crash.
- Do not use open Firestore rules (allow read, write: if true) in a real deployment.
