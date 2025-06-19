[app]

# Название приложения
title = Password App

# Имя пакета (должно быть уникальным)
package.name = passwordapp

# Домен (обычно обратный домен)
package.domain = org.example

# Путь к исходникам
source.dir = .

# Главный файл приложения
source.main = main.py

# Версии Python и Kivy
requirements = python3,kivy==2.3.0

# Версия Android SDK
android.api = 34
android.minapi = 21
android.ndk = 25b

# Разрешения Android (если нужны)
#android.permissions = INTERNET

# Ориентация экрана
orientation = portrait

# Включить поддержку OpenGL ES 2
fullscreen = 1

[buildozer]

# Уровень логирования (0-3)
log_level = 2

# Папка для билдов
build_dir = ./.buildozer

# Папка для бинариев
bin_dir = ./bin
