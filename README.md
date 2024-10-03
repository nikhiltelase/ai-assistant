# Avi AI

Welcome to the **Avi AI** project! Avi AI is a personal voice assistant designed to enhance your daily productivity and automate various tasks using voice commands. Built with cutting-edge technology, Avi AI integrates seamlessly with smart home devices, apps, and more.

## Watch The Video
[![Video Thumbnail](https://img.youtube.com/vi/mpLLt3EGm0Y/hqdefault.jpg)](https://www.youtube.com/watch?v=mpLLt3EGm0Y)

Click the image to watch the video.
## Check Out This LinkedIn Post
[View the LinkedIn post here](https://www.linkedin.com/feed/update/urn:li:activity:7204754130039435264/)


## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Microcontroller Setup](#microcontroller-setup)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

Avi AI comes packed with a variety of features:

- **Speech Recognition**: Understands and processes user commands with high accuracy.
- **Smart Home Control**: Turn on/off lights and control other smart devices.
- **App Control**: Open applications like VS Code with simple voice commands.
- **Website Browsing**: Access popular websites like YouTube and Wikipedia.
- **Music Playback**: Play music from your local library or online services.
- **Time Telling**: Get real-time updates on the current time.
- **Conversational AI**: Engage in natural conversations and get answers to your questions.

## Technologies Used

- **Python**: The primary programming language for developing Avi AI.
- **Google Gemini API**: For generative AI capabilities.
- **Speech Recognition**: For understanding voice commands.
- **Edge TTS**: For text-to-speech functionality.
- **Pygame**: For playing audio responses.
- **Requests**: For handling HTTP requests (smart home integration).
- **dotenv**: For environment variable management.

## Installation

To set up Avi AI on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/avi-ai.git
   cd avi-ai
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory and add your API keys and IP addresses:
     ```
     GEMINI_API_KEY=your_api_key
     IP=your_device_ip
     ```

4. Run the application:
   ```bash
   python main.py
   ```

## Microcontroller Setup

To control lights using Avi AI, you will need a microcontroller (such as an ESP8266 or Arduino) connected to your lights. Follow these steps to set up the microcontroller:

1. **Choose a Microcontroller**: Use an ESP8266, Arduino, or similar device that can connect to your local Wi-Fi network.

2. **Connect the Relay Module**: Wire a relay module to the microcontroller to control the power to your lights.

3. **Upload Code to the Microcontroller**: Write a program to handle HTTP requests and control the relay based on those requests. Below is a simple example for an ESP8266:
   ```cpp
      import network
   import socket
   from machine import Pin
   
   # Connect to Wi-Fi
   ssid = 'your_ssid'
   password = 'your_password'
   wlan = network.WLAN(network.STA_IF)
   wlan.active(True)
   wlan.connect(ssid, password)
   
   while not wlan.isconnected():
       pass
   
   print('Connection successful')
   print(wlan.ifconfig()[0])
   
   # Set up the LED
   led = Pin(2, Pin.OUT)
   led.value(1)
   
   # Create a web server
   addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
   s = socket.socket()
   s.bind(addr)
   s.listen(1)
   
   while True:
       cl, addr = s.accept()
       request = cl.recv(1024)
       request = str(request)
   
       if 'GET /led/on' in request:
           led.value(0)  # Turn LED on
       elif 'GET /led/off' in request:
           led.value(1)  # Turn LED off
   
       # Determine the current LED status
       if led.value() == 0:
           status = 'on'
       else:
           status = 'off'
   
       # Prepare the HTML response
       response = f"""HTTP/1.1 200 OK
       Content-Type: text/html
   
       <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Light Control</title>
       <style>
         body {{
           font-family: Arial, sans-serif;
           display: flex;
           flex-direction: column;
           justify-content: center;
           align-items: center;
           height: 100vh;
           margin: 0;
           background-color: #f4f4f9;
         }}
         h1 {{
           color: #333;
         }}
         button {{
           background-color: #007bff;
           color: white;
           padding: 10px 20px;
           margin: 10px;
           border: none;
           border-radius: 5px;
           font-size: 16px;
           cursor: pointer;
         }}
         button:hover {{
           background-color: #0056b3;
         }}
       </style>
     </head>
     <body>
       <h1>Control Your Light</h1>
       <h2>Light is {status}</h2>
       <a href="/led/on"><button id="lightOn">Turn On</button></a>
       <a href="/led/off"><button id="lightOff">Turn Off</button></a>
     </body>
   </html>
    """
    # Send the response back to the client
    cl.send(response)
    cl.close()


   ```

4. **Connect to the Same Network**: Ensure that your computer running Avi AI and the microcontroller are connected to the same local network.

5. **Set the IP Address**: Update the `.env` file with the IP address of your microcontroller:
   ```
   IP=http://your_microcontroller_ip/
   ```

## Usage

To interact with Avi AI, simply speak your commands. Here are a few examples:

- "Turn on the light."
- "Open YouTube."
- "Play my favorite song."
- "What time is it?"

For a complete list of commands and features, refer to the [documentation](#).

## Contributing

Contributions are welcome! If you would like to contribute to the Avi AI project, please fork the repository and submit a pull request. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact:
- **Nikhil**: [nikhiltelase@gmail.com](mailto:nikhiltelase@gmail.com)
- **LinkedIn**: [nikhiltelase](https://www.linkedin.com/in/nikhiltelase/)

Thank you for checking out Avi AI! We hope you enjoy using your personal voice assistant!
