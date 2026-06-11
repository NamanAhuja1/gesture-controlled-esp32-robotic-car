# gesture-controlled-esp32-robotic-car
A computer vision-based robotic car that uses MediaPipe hand tracking and OpenCV gesture recognition to control an ESP32-powered vehicle in real time.
# Gesture Controlled ESP32 Robotic Car

A computer vision based robotic car controlled using hand gestures.

## Features

- Real-time hand tracking
- Gesture recognition using MediaPipe
- ESP32 motor control
- Serial communication
- Touchless vehicle navigation

## Tech Stack

- Python
- OpenCV
- MediaPipe
- ESP32
- Arduino IDE
- L298N Motor Driver

## Architecture

Webcam
↓
OpenCV + MediaPipe
↓
Gesture Recognition
↓
Serial Communication
↓
ESP32
↓
Motor Driver
↓
Robot Car

## Supported Gestures

| Gesture | Action |

| Open Hand | Forward |
| Fist | Stop |
| Peace Sign | Left |
| Three Fingers | Right |
| Thumb Down | Backward |

## Installation

pip install -r requirements.txt

## Run

python gesture_control.py
