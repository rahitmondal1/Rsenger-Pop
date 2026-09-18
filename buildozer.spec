[app]

# (str) Title of your application
title = Rsenger

# (str) Package name
package.name = rsenger

# (str) Package domain
package.domain = com.rsenger

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,html,css,js,png,jpg,jpeg,webp,json,txt

# (str) Application version
version = 2.0.0


# (list) Python requirements
requirements = python3,kivy,pyjnius


# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 1


# (str) Android API
android.api = 35

# (str) Minimum Android API
android.minapi = 23


# (list) Android architectures
android.arch = arm64-v8a,armeabi-v7a


# (list) Android permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,CAMERA,READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,POST_NOTIFICATIONS


# (bool) Enable AndroidX
android.enable_androidx = True

# (bool) Accept Android SDK licenses
android.accept_sdk_license = True


# (str) Android app theme
android.entrypoint = org.kivy.android.PythonActivity


# (bool) Allow backup
android.allow_backup = True


# (str) Android app name
android.app_name = Rsenger


# (str) Presplash
presplash.filename =


# (str) Icon
icon.filename =


# (str) Window
orientation = portrait


[buildozer]

# (str) Build directory
build_dir = .buildozer

# (str) APK output directory
bin_dir = bin

# (int) Log level
log_level = 2

# (bool) Warn if running as root
warn_on_root = 1
