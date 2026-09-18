[app]

# (str) Title of your application
title = Rsenger

# (str) Package name
package.name = rsenger

# (str) Package domain
package.domain = com.rsenger

# (str) Application version
version = 3.0.0

# (str) Source directory
source.dir = .

# (list) Source file extensions
source.include_exts = py,html,css,js,png,jpg,jpeg,webp,json,txt

# (str) Application requirements
requirements = python3,kivy,pyjnius

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 1


# (str) Android API
android.api = 35

# (str) Minimum Android API
android.minapi = 23

# (list) Android architectures
android.archs = arm64-v8a,armeabi-v7a


# (list) Android permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,CAMERA,READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,POST_NOTIFICATIONS

# (bool) Enable AndroidX
android.enable_androidx = True

# (bool) Accept Android SDK license
android.accept_sdk_license = True

# (bool) Allow Android backup
android.allow_backup = True

# (str) Application icon
icon.filename = %(source.dir)s/assets/rsenger_logo.png


[buildozer]

# (str) Build directory
build_dir = .buildozer

# (str) Output directory
bin_dir = bin

# (int) Log level
log_level = 2

# (bool) Warn when running as root
warn_on_root = 1
