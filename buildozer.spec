[app]

# (str) Title of your application
title = Rsenger

# (str) Package name
package.name = rsenger

# (str) Package domain
package.domain = com.rsenger

# (str) Version
version = 3.0.0

# (str) Source code directory
source.dir = .

# (str) File extensions to include
source.include_exts = py,html,css,js,png,jpg,jpeg,webp,gif,json,txt,ico,svg

# (str) Application requirements
#
# IMPORTANT:
# Explicitly pin Android Python to 3.13
# so python-for-android does NOT use Python 3.14.
requirements = python3==3.13.7,hostpython3==3.13.7,kivy,pyjnius

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 1

# (int) Android API
android.api = 35

# (int) Minimum Android API
android.minapi = 24

# (str) Android architectures
android.archs = arm64-v8a,armeabi-v7a

# (str) Android permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,CAMERA,READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,POST_NOTIFICATIONS

# (bool) AndroidX
android.enable_androidx = True

# (bool) Accept Android SDK license
android.accept_sdk_license = True

# (bool) Allow backup
android.allow_backup = True

# (str) App icon
icon.filename = %(source.dir)s/assets/rsenger_logo.png

# (str) Presplash
# presplash.filename = %(source.dir)s/assets/rsenger_logo.png


[buildozer]

# (str) Build directory
build_dir = .buildozer

# (str) Output directory
bin_dir = bin

# (int) Log level
log_level = 2

# (bool) Warn if running as root
warn_on_root = 1
