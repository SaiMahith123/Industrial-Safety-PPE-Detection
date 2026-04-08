# 👷 Industrial Safety AI: Real-time PPE Compliance System

A computer vision application designed for industrial safety monitoring. This project demonstrates an end-to-end AI pipeline—from automated data collection and deep learning training to optimized real-time inference.

## 🌟 Project Impact
In industrial settings, ensuring every worker wears a safety helmet is critical. This project provides a scalable, low-latency solution that can be deployed on standard hardware (like a Ryzen 5 laptop) without needing expensive GPUs.

## 🚀 Key Technical Features
* **Framework Interoperability:** Model developed in **PyTorch**, converted to **TensorFlow**, and optimized via **ONNX**.
* **Transfer Learning:** Leveraged the **MobileNetV2** architecture, fine-tuned on a custom-curated safety dataset.
* **Data Augmentation:** Implemented `RandomHorizontalFlip`, `RandomRotation`, and `ColorJitter` to improve model robustness against lighting and glare.
* **Edge Optimized:** Achieves high FPS using **ONNX Runtime** for CPU-based inference.

## 🛠️ Tech Stack
| Category | Technology |
| :--- | :--- |
| **Languages** | Python 3.10 |
| **Deep Learning** | PyTorch, TensorFlow, Torchvision |
| **Inference** | ONNX Runtime |
| **Computer Vision** | OpenCV |
| **Tools** | Bing Image Downloader, Git, VS Code |

## 📁 Project Structure
* `0_get_data.py`: Automated scraper for safety-gear imagery.
* `4_final_train.py`: The **Training Engine** (20 Epochs with Data Augmentation).
* `2_bridge.py`: The **Transpilation Script** (Exports PyTorch weights to ONNX).
* `3_live_ai_final.py`: The **Production App** (Real-time webcam monitoring).
* `model.onnx`: The final "smart" model weights.

## 📈 Performance & Results
* **Training Loss:** Reduced from **0.69** to **0.16** over 20 epochs.
* **Accuracy:** Successfully identifies helmet compliance on live video feeds and digital screens.

## 💻 How to Run
1. Create a virtual environment: `python -m venv venv`
2. Activate venv: `.\venv\Scripts\activate`
3. Install dependencies: `pip install torch torchvision onnxruntime opencv-python`
4. Start the monitor: `python 3_live_ai_final.py`

---
**Developed by T Sai Mahit** *B.E in AI & ML (DEC 2025)* 