#!/bin/bash
set -e

chmod +x geckodriver
export PATH=$PATH:$(pwd)
python webdriver_easy_crm.py
