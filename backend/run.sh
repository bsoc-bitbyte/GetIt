#!/bin/bash

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
exec ".venv/bin/python" build.py
