[app]

title = Rsenger
package.name = rsenger
package.domain = com.rsenger

version = 3.0.0

source.dir = .

source.include_exts = py,html,css,js,png,jpg,jpeg,webp,gif,json,txt,ico,svg

requirements = python3==3.13.7,hostpython3==3.13.7,kivy,pyjnius

orientation = portrait

fullscreen = 1

android.api = 35
android.minapi = 24

android.archs = arm64-v8a

android.permissions = INTERNET,ACCESS_NETWORK_STATE,CAMERA,READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,POST_NOTIFICATIONS

android.enable_androidx = True
android.accept_sdk_license = True
android.allow_backup = True

icon.filename = %(source.dir)s/assets/rsenger_logo.png

# Use the current python-for-android development branch
p4a.branch = develop


[buildozer]

build_dir = .buildozer
bin_dir = bin

log_level = 2
warn_on_root = 1
