# Project AI Doctor 2.0

Welcome to Project AI Doctor 2.0, an advanced system designed to assist with medical interactions using a combination of a powerful AI brain, voice-to-text, and text-to-voice capabilities. This project is built using Python and leverages state-of-the-art libraries for a seamless and intuitive experience.

## Table of Contents
1. [Project Setup Guide](#project-setup-guide)
2. [Installing FFmpeg and PortAudio](#installing-ffmpeg-and-portaudio)
3. [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)
4. [Running the Application](#running-the-application)
5. [Project Phases](#project-phases)
6. [Troubleshooting](#troubleshooting)
7. [Important Notes](#important-notes)
8. [License](#license)

## Project Setup Guide

This guide provides step-by-step instructions to set up your project environment, including the installation of FFmpeg and PortAudio across macOS, Linux, and Windows, as well as setting up a Python virtual environment using Pipenv, pip, or conda.

### Installing ffmpeg and portaudio

FFmpeg is required for handling audio files, and PortAudio is necessary for real-time audio input/output.

### macOS

1. **Install Homebrew (if not already installed):**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. **Install FFmpeg and PortAudio:**

    ```bash
    brew install ffmpeg portaudio
### Linux

For Debian-based distributions (e.g., Ubuntu):

1. Update the package list:

    ```bash
    sudo apt update
2. Install FFmpeg and PortAudio:

    ```bash
    sudo apt install ffmpeg portaudio19-dev
### Windows

#### Download ffmpeg:

1. Visit the official FFmpeg download page: FFmpeg Downloads

2. Navigate to the Windows builds section and download the latest static build.

#### Extract and Set Up ffmpeg:

1. Extract the downloaded ZIP file to a folder (e.g., ```C:\ffmpeg```).

2. Add the ```bin``` directory to your system's PATH:

   * Search for "Environment Variables" in the Start menu.

   * Click on "Edit the system environment variables."

   * In the System Properties window, click on "Environment Variables."

   * Under "System variables," select the "Path" variable and click "Edit."

   * Click "New" and add the path to the bin directory (e.g., C:\ffmpeg\bin).

   * Click "OK" to apply the changes.

### Install PortAudio:

1. Download the PortAudio binaries from the official website: PortAudio Downloads

2. Follow the installation instructions provided on the website.

## Setting Up a Python Virtual Environment
A virtual environment is highly recommended to manage project dependencies and avoid conflicts.

### Using Pipenv
1. Install Pipenv (if not already installed):

    ```bash
    pip install pipenv
2. Install Dependencies with Pipenv:

    ```bash
    pipenv install
3. Activate the Virtual Environment:

    ```bash
    pipenv install
### Using ```pip``` and ```venv```

1.  **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

2.  **Activate the Virtual Environment:**

    * **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

    * **Windows:**

        ```bash
        venv\Scripts\activate
        ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
### Using Conda

1.  **Create a Conda Environment:**

    ```bash
    conda create --name myenv python=3.11
    ```

2.  **Activate the Conda Environment:**

    ```bash
    conda activate myenv
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Once you have set up your environment and installed all dependencies, you can run the different phases of the project. Ensure your virtual environment is activated before running any of the following commands.

* **Phase 1: Brain of the Doctor** 🧠

    ```bash
    python doctor_brain.py
    ```

* **Phase 2: Voice of the Patient** 🗣️

    ```bash
    python patient_voice.py
    ```

* **Phase 3: Voice of the Doctor** 🤖

    ```bash
    python doctor_voice.py
    ```

* **Phase 4: Setup Gradio UI** 🖥️

    ```bash
    python gradio_app.py
    ```