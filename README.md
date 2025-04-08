# 🧠 Self-Driving Car using Udacity Simulator

This project is a deep learning-based self-driving car implementation using the [Udacity Self-Driving Car Simulator](https://github.com/udacity/self-driving-car-sim). A convolutional neural network (CNN) is trained with images from the simulator to predict steering angles for autonomous driving.

## 🚗 Project Overview

The car receives images from a front-facing camera in the simulator and uses a trained model to predict the steering angle in real time. The model is trained using TensorFlow and follows an end-to-end learning approach inspired by NVIDIA’s self-driving research.

## 🔧 Technologies Used

- **Python 3**
- **TensorFlow 2.x / Keras**
- **OpenCV**
- **NumPy**
- **Udacity Self-Driving Car Simulator**

## 📦 Installation

1. **Clone this repository**

```bash
git clone https://github.com/your-username/self-driving-car-udacity.git
cd self-driving-car-udacity
```

2. **Create and activate a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Download the Udacity Simulator**

Simulator download: [Udacity Self-Driving Car Simulator](https://github.com/udacity/self-driving-car-sim)

## 🚀 How to Run

### 📸 Collect Training Data (Optional)

Use the simulator in **training mode** to drive manually and collect images + steering angles. The data will be saved into a CSV log and an image folder.

### 🧠 Train the Model

```bash
python train.py
```

This will train the model and save it as `model.h5`.

### 🕹️ Drive Using the Trained Model

Run the simulator in **autonomous mode**, then:

```bash
python drive.py model.h5
```

## 📁 Project Structure

```
.
├── data/                   # Collected driving data (images + driving_log.csv)
├── model/                  # Saved model(s)
├── train.py                # Model training script
├── drive.py                # Script to drive car in simulator using trained model
├── model.py                # CNN architecture (TensorFlow/Keras)
├── utils.py                # Image preprocessing and helpers
├── requirements.txt        # List of dependencies
└── README.md               # This file
```

## 📷 Example Results

*(Optional: Add screenshots or a video/GIF of the car successfully driving in the simulator)*

## ✅ To-Do / Future Work

- Add lane detection and object avoidance
- Train on multiple tracks
- Implement PID control for smoother driving

## 🤝 Contributing

Contributions and suggestions are welcome! Please fork the repo and open a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
