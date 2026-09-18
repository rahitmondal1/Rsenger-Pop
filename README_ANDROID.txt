RSENGER PREMIUM V3
==================

Rsenger is a Firebase-powered web application packaged as an
Android application using Python, Kivy and Android WebView.

The original HTML/CSS/JavaScript application is retained and
loaded inside the Android WebView.


PROJECT FILES
=============

index.html
    Main Rsenger web application.

style.css
    Premium visual styling and mobile refinements.

main.py
    Python + Kivy Android application wrapper.

buildozer.spec
    Buildozer Android APK configuration.

assets/rsenger_logo.png
    Rsenger application logo and launcher icon.

index.backup.html
    Backup copy of the original HTML application.

.github/workflows/build-apk.yml
    GitHub Actions workflow used to build the Android APK.

FIREBASE_RULES_WARNING.txt
    Important security information about the supplied Firebase rules.


GITHUB ANDROID BUILD
====================

The APK is built automatically using GitHub Actions.

Steps:

1. Upload the complete project to a GitHub repository.

2. Make sure buildozer.spec is located in the repository root.

3. Make sure main.py is located in the repository root.

4. Make sure index.html is located in the repository root.

5. Make sure the following folder exists:

   assets/
       rsenger_logo.png

6. Make sure the workflow exists:

   .github/
       workflows/
           build-apk.yml

7. Open the GitHub repository.

8. Open:

   Actions

9. Select:

   Rsenger Android APK

10. Select:

   Run workflow

11. Wait for the workflow to finish.

12. When the workflow is successful, open the completed
    workflow run.

13. Find the Artifacts section.

14. Download:

    Rsenger-APK

15. Extract the downloaded ZIP file.

16. The APK file will be inside the ZIP.


BUILD SYSTEM
============

The GitHub Actions workflow uses:

- Ubuntu 22.04
- Python 3.11 for the Buildozer host environment
- Java 17
- Buildozer
- python-for-android
- Kivy
- PyJNIus
- Android SDK/NDK components required by the build


ANDROID PYTHON VERSION
======================

The Android application Python version is explicitly specified
in buildozer.spec.

The important requirement is:

requirements = python3==3.13.7,hostpython3==3.13.7,kivy,pyjnius

This is separate from the Python version used by the GitHub
Actions runner.

The GitHub runner uses Python 3.11 to run Buildozer.

The Android application is configured to use Python 3.13.7.


ANDROID ARCHITECTURE
====================

The application is currently configured for:

arm64-v8a

This is the architecture used by most modern Android devices.


ANDROID SETTINGS
================

Target Android API:

35

Minimum Android API:

24

Application orientation:

portrait

AndroidX:

enabled

Fullscreen:

enabled


ANDROID PERMISSIONS
===================

The application requests permissions required by the current
application configuration, including:

- INTERNET
- ACCESS_NETWORK_STATE
- CAMERA
- READ_MEDIA_IMAGES
- READ_MEDIA_VIDEO
- POST_NOTIFICATIONS


APPLICATION STRUCTURE
=====================

The Android application uses Python/Kivy as the application shell.

The existing Rsenger HTML application is loaded inside an
Android WebView.

The structure is:

Android Application
        |
        v
Python / Kivy
        |
        v
Android WebView
        |
        v
index.html
        |
        +---- style.css
        |
        +---- JavaScript
        |
        +---- Firebase
        |
        +---- Cloudinary


IMPORTANT FUNCTIONAL NOTES
===========================

The existing Rsenger web application uses Firebase services
including authentication, Firestore, Realtime Database and other
web integrations.

The application also contains Cloudinary/webtonative-related
integrations from the original project.

The HTML application was retained instead of replacing the
existing application logic with an incomplete native rewrite.


GOOGLE SIGN-IN
==============

Google Sign-In inside a local Android WebView may require
additional Firebase and Google configuration.

If Google Sign-In does not work inside the APK, additional
Android/Firebase configuration may be required.

This can include:

- Android package configuration
- Firebase Android application configuration
- SHA-1 fingerprint
- SHA-256 fingerprint
- Google authentication configuration


FIREBASE SECURITY
=================

Before production use, review:

FIREBASE_RULES_WARNING.txt

The Firebase rules supplied with the original project may allow
more access than is appropriate for a production application.

Do not assume that the current Firebase rules are production-safe.


CLOUDINARY
==========

Image and file upload features depend on the Cloudinary
configuration contained in the application.

Cloudinary upload presets must remain valid for uploads to work.


LOCAL BUILD
===========

The project can also be built on a compatible Linux environment.

Install Buildozer and its required dependencies first.

Then run:

    buildozer android debug


APK OUTPUT
==========

When Buildozer finishes successfully, the APK is placed inside:

    bin/


GITHUB ACTIONS OUTPUT
=====================

When GitHub Actions finishes successfully, the workflow uploads
the APK as an artifact.

Artifact name:

    Rsenger-APK


TROUBLESHOOTING
===============

If the GitHub Actions build fails:

1. Open the repository.

2. Open Actions.

3. Select Rsenger Android APK.

4. Open the failed workflow run.

5. Check the failed Build APK step.

6. Review the final error message in the workflow log.


IMPORTANT
=========

Do not delete the following files:

    index.html
    main.py
    style.css
    buildozer.spec

Also keep:

    assets/rsenger_logo.png

The GitHub Actions workflow requires the project structure
to remain intact.


VERSION
=======

Rsenger Premium V3
Version 3.0.1
