[app]
title = Gorfer Jore Raja
package.name = gorferjoreraja
package.domain = org.example
source.dir = .
source.include_exts = py,ttf,png,jpg,kv,json,mp3,wav
version = 1.0
requirements = python3,kivy
orientation = landscape
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.copy_libs = 1
