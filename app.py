import socketio
import eventlet
import numpy as np
from flask import Flask
from keras.models import load_model
from keras.losses import mean_squared_error  # Import the required loss function
import base64
from io import BytesIO
from PIL import Image
import cv2

# Initialize SocketIO server
sio = socketio.Server()

# Initialize Flask application
app = Flask(__name__)
speed_limit = 10

# Function to preprocess the image
def img_preprocess(img):
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img

# Handle telemetry data from the simulator
@sio.on('telemetry')
def telemetry(sid, data):
    speed = float(data['speed'])
    # Decode and preprocess the image from base64 encoding
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    image = np.asarray(image)
    image = img_preprocess(image)
    image = np.array([image])
    steering_angle = float(model.predict(image))
    throttle = 1.0 - speed / speed_limit
    print('{} {} {}'.format(steering_angle, throttle, speed))
    send_control(steering_angle, throttle)

# Handle new connection to the simulator
@sio.on('connect')
def connect(sid, environ):
    print('Connected')
    send_control(0, 0)

# Function to send control commands to the simulator
def send_control(steering_angle, throttle):
    sio.emit('steer', data={
        'steering_angle': str(steering_angle),
        'throttle': str(throttle)
    })

if __name__ == '__main__':
    # Load the pre-trained Keras model
    model = load_model('model/model.h5', custom_objects={'mse': mean_squared_error})
    
    # Wrap Flask application with SocketIO middleware
    app = socketio.Middleware(sio, app)
    
    # Start the web server
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
