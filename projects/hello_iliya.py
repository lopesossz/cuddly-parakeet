#!/usr/bin/env python3
import os, sys, platform

print("="*50)
print("Welcome to Iliyas High-Performance GitHub Runner!")
print(f"OS: {platform.system()} {platform.release()} ({platform.machine()})")
print(f"CPU count: {os.cpu_count()}")
print("="*50)
