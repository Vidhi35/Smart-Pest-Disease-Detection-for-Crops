# 🌱 Plant Disease Detection & Treatment System

<div align="center">

![Plant Disease Detection](https://img.shields.io/badge/AI-Plant%20Disease%20Detection-green)
![Groq](https://img.shields.io/badge/LLM-Groq%20%2B%20Llama%203.3-orange)
![Hugging Face](https://img.shields.io/badge/Model-Hugging%20Face-yellow)
![Gradio](https://img.shields.io/badge/Interface-Gradio-blue)

**A comprehensive AI-powered plant disease detection and treatment recommendation system**

**Group 13 - AgriTech Innovators** 🌾

[🚀 Live Demo on Hugging Face](https://huggingface.co/spaces/Vidhi/plant-disease-detection) | [📖 Documentation](#documentation) | [🤝 Team](#team-members)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [System Architecture](#system-architecture)
- [Installation &amp; Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Deployment](#deployment)
- [Team Members](#team-members)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **Plant Disease Detection & Treatment System** is an intelligent application that helps farmers, gardeners, and agricultural professionals identify plant diseases and receive AI-powered treatment recommendations. Built by **Group 13**, this system combines state-of-the-art computer vision and large language models to provide accurate disease detection and comprehensive treatment guidance.

### Key Highlights

- 🔍 **Accurate Detection**: Uses pre-trained MobileNetV2 model for disease classification
- 🤖 **AI-Powered Recommendations**: Leverages Groq's Llama 3.3 70B for detailed treatment advice
- 📱 **User-Friendly Interface**: Simple web interface built with Gradio
- 🌐 **Deployed on Hugging Face**: Accessible anywhere, anytime
- 💯 **Free to Use**: No API costs - completely free LLM via Groq

---

## ✨ Features

### 🔬 Disease Detection

- ✅ Upload plant images or capture from webcam
- ✅ AI-powered disease classification with confidence scores
- ✅ Top 3 disease predictions for comprehensive analysis
- ✅ Support for multiple plant species and diseases

### 💊 Treatment Recommendations

- ✅ **Disease Overview**: Detailed description of the detected disease
- ✅ **Symptoms**: Key symptoms to identify the disease
- ✅ **Causes**: Root causes and contributing factors
- ✅ **Treatment Options**:
  - ⚡ Immediate actions to take
  - 🌱 Organic/natural remedies
  - 🧪 Chemical treatments (when necessary)
  - 🛡️ Preventive measures
- ✅ **Recovery Timeline**: Expected recovery duration
- ✅ **Additional Tips**: Expert advice for disease management

### 🎨 Enhanced UI/UX

- ✅ Beautiful Markdown-formatted output
- ✅ Custom CSS styling for better readability
- ✅ Emoji-enhanced sections for visual appeal
- ✅ Responsive design for all devices

---

## 🎬 Demo

### Live Application

Access the deployed application: **[Plant Disease Detection on Hugging Face](https://huggingface.co/spaces/Vidhi/plant-disease-detection)**

### How It Works

1. **Upload/Capture Image** 📸

   - Upload a plant image from your device
   - Or use your webcam to capture a live image
2. **AI Analysis** 🔍

   - The system analyzes the image using a pre-trained model
   - Provides top 3 disease predictions with confidence scores
3. **Get Treatment** 💊

   - Receive comprehensive AI-generated treatment recommendations
   - Formatted with clear sections and actionable advice

---

## 🛠️ Technologies Used

### Machine Learning & AI

| Technology                          | Purpose                             | Version |
| ----------------------------------- | ----------------------------------- | ------- |
| **Hugging Face Transformers** | Disease classification model        | 4.35+   |
| **Groq**                      | Free LLM API provider               | Latest  |
| **Llama 3.3 70B**             | Treatment recommendation generation | Latest  |
| **LangChain**                 | LLM orchestration and chaining      | 1.0+    |
| **PyTorch**                   | Deep learning framework             | 2.0+    |

### Web Interface

| Technology              | Purpose                         | Version |
| ----------------------- | ------------------------------- | ------- |
| **Gradio**        | Web UI framework                | 4.0+    |
| **Pillow**        | Image processing                | 10.0+   |
| **Python-dotenv** | Environment variable management | 1.0+    |

### Model Details

- **Classification Model**: `linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification`
  - Architecture: MobileNetV2
  - Input Size: 224x224
  - Pre-trained on plant disease dataset
  - Supports 38+ disease classes

---

## 🏗️ System Architecture

```
┌─────────────────┐
│  User Interface │
│    (Gradio)     │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│         Image Input                 │
│  (Upload / Webcam Capture)          │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│    Disease Classification           │
│  (Hugging Face MobileNetV2)         │
│  - Top 3 Predictions                │
│  - Confidence Scores                │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│   Treatment Generation              │
│  (Groq + Llama 3.3 70B)             │
│  via LangChain                      │
│  - Disease Overview                 │
│  - Symptoms & Causes                │
│  - Treatment Recommendations        │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│    Formatted Output                 │
│  (Markdown with CSS Styling)        │
└─────────────────────────────────────┘
```

---

## 📦 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for first-time model download)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/plant-disease-detection.git
cd plant-disease-detection
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies include:**

- gradio>=4.0.0
- transformers>=4.35.0
- torch>=2.0.0
- torchvision>=0.15.0
- Pillow>=10.0.0
- langchain>=1.0.0
- langchain-core>=1.0.0
- langchain-groq>=1.0.0
- python-dotenv>=1.0.0

### Step 4: Get Free Groq API Key

1. Visit [Groq Console](https://console.groq.com)
2. Sign up for a free account (no credit card required)
3. Navigate to "API Keys" in the sidebar
4. Click "Create API Key"
5. Copy your API key (starts with `gsk_...`)

### Step 5: Configure Environment Variables

Create a `.env` file in the project root:

```bash
# .env file
GROQ_API_KEY="gsk_your_actual_api_key_here"
```

**Alternative: Set environment variable directly**

**Windows (PowerShell):**

```powershell
$env:GROQ_API_KEY="gsk_your_api_key_here"
```

**Windows (Command Prompt):**

```cmd
set GROQ_API_KEY=gsk_your_api_key_here
```

**Linux/Mac:**

```bash
export GROQ_API_KEY=gsk_your_api_key_here
```

### Step 6: Run the Application

```bash
python app.py
```

The application will launch at: **http://localhost:7860**

---

## 📖 Usage Guide

### Basic Usage

1. **Launch the Application**

   ```bash
   python app.py
   ```
2. **Access the Web Interface**

   - Open your browser
   - Navigate to `http://localhost:7860`
3. **Upload or Capture Image**

   - Click on the image upload area
   - Choose "Upload" to select an image from your device
   - Or choose "Webcam" to capture a live image
4. **Analyze Disease**

   - Click the "🔬 Analyze Disease" button
   - Wait for the AI to process the image (usually 2-5 seconds)
5. **View Results**

   - **Left Panel**: Disease predictions with confidence scores
   - **Right Panel**: Comprehensive treatment recommendations

### Tips for Best Results

✅ **Image Quality**

- Use clear, well-lit images
- Focus on affected plant areas
- Avoid blurry or dark images

✅ **Image Content**

- Capture leaves, stems, or fruits showing disease symptoms
- Include close-up shots of affected areas
- Ensure the disease symptoms are visible

✅ **Multiple Angles**

- Try different angles if first result is uncertain
- Compare predictions from multiple images

---

## 🚀 Deployment

### Deployed on Hugging Face Spaces

This project is deployed on **Hugging Face Spaces** under **Vidhi's account**.

**Live URL**: [https://huggingface.co/spaces/Vidhi/plant-disease-detection](https://huggingface.co/spaces/Vidhi/plant-disease-detection)

### Deployment Steps (For Reference)

1. **Create Hugging Face Account**

   - Sign up at [huggingface.co](https://huggingface.co)
2. **Create New Space**

   - Click "New Space"
   - Choose "Gradio" as the SDK
   - Name: `plant-disease-detection`
3. **Upload Files**

   - `app.py` - Main application file
   - `requirements.txt` - Dependencies
   - `.env` - Environment variables (add Groq API key as a Space secret)
   - `README.md` - This documentation
4. **Configure Secrets**

   - Go to Space Settings
   - Add `GROQ_API_KEY` as a secret
   - Paste your Groq API key
5. **Deploy**

   - Space will automatically build and deploy
   - Access via the provided URL

### Alternative Deployment Options

#### Deploy on Render

```bash
# Add Procfile
web: python app.py
```

#### Deploy on Railway

```bash
# Add railway.json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python app.py"
  }
}
```

---

## 👥 Team Members

**Group 13 - AgriTech Innovators** 🌾

Our team of passionate developers and agricultural technology enthusiasts working together to revolutionize plant disease detection.

| Name                       | Roll Number  | Role                                | Contribution                                                                |
| -------------------------- | ------------ | ----------------------------------- | --------------------------------------------------------------------------- |
| **Roshan Khatri**    | 300012723047 | Backend Developer & LLM Integration | Implemented Groq/Llama integration, LangChain setup, and prompt engineering |
| **Suman Kumar**      | 300012723065 | Model Integration Specialist        | Disease classification model setup, optimization, and testing               |
| **Vedshree Shrawan** | 300012723070 | UI/UX Designer                      | Gradio interface design, CSS styling, and user experience enhancement       |
| **Vidhirani Netam**  | 300012723071 | Deployment Lead                     | Hugging Face Spaces deployment, configuration, and maintenance              |
| **Yash Shukla**      | 300012723073 | Documentation & Testing             | Comprehensive documentation, testing, debugging, and quality assurance      |

### 🎯 Team Contributions

Our collaborative efforts resulted in a comprehensive plant disease detection system:

- **🤖 AI/ML Development**:

  - Integrated Hugging Face MobileNetV2 for disease classification
  - Implemented Groq + Llama 3.3 70B for intelligent treatment recommendations
  - Optimized model performance and response time
- **💻 Backend Development**:

  - Migrated from Google Gemini to free Groq LLM
  - Updated to modern LangChain 1.1.0 (LCEL syntax)
  - Implemented robust error handling and validation
- **🎨 Frontend & UI/UX**:

  - Designed beautiful Gradio interface
  - Created custom CSS styling for Markdown rendering
  - Enhanced user experience with emoji-rich formatted output
- **📚 Documentation**:

  - Created 10+ comprehensive documentation files
  - Wrote detailed setup and deployment guides
  - Prepared user manuals and troubleshooting guides
- **🚀 Deployment & DevOps**:

  - Deployed on Hugging Face Spaces
  - Configured environment variables and secrets
  - Set up continuous integration workflow
- **🧪 Testing & Quality Assurance**:

  - Comprehensive testing of all features
  - Bug fixes and performance optimization
  - User acceptance testing

### 🏆 Team Achievements

- ✅ Successfully built a production-ready AI application
- ✅ Migrated to 100% FREE LLM solution (zero API costs)
- ✅ Created professional-grade documentation
- ✅ Deployed on Hugging Face for public access
- ✅ Achieved fast response times (2-5 seconds)
- ✅ Implemented modern best practices and coding standards

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Reporting Issues

- Use GitHub Issues to report bugs
- Provide detailed description and steps to reproduce
- Include screenshots if applicable

### Suggesting Features

- Open a GitHub Issue with the "enhancement" label
- Describe the feature and its benefits
- Discuss implementation approach

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Group 13

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **Hugging Face** for providing the disease classification model
- **Groq** for free access to Llama 3.3 70B
- **LangChain** for LLM orchestration framework
- **Gradio** for the amazing web interface framework
- **Our Instructors** for guidance and support

---

## 📞 Contact & Support

- **Project Repository**: [GitHub Link]
- **Live Demo**: [Hugging Face Spaces - Vidhi](https://huggingface.co/spaces/Vidhi/plant-disease-detection)
- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/discussions)

---

## ⚠️ Disclaimer

This system provides **suggestions only**. Always consult with agricultural experts, agronomists, or plant pathologists for serious plant health issues. The AI-generated recommendations should be used as a supplementary tool, not as a replacement for professional agricultural advice.

---

## 📊 Project Statistics

- **Lines of Code**: ~380
- **Dependencies**: 9 main packages
- **Model Size**: ~14MB (MobileNetV2)
- **Supported Diseases**: 38+ plant disease classes
- **Average Response Time**: 2-5 seconds
- **Deployment Platform**: Hugging Face Spaces

---

## 🔮 Future Enhancements

- [ ] Add support for more plant species
- [ ] Implement disease severity assessment
- [ ] Add multi-language support
- [ ] Create mobile application
- [ ] Integrate weather data for better predictions
- [ ] Add user feedback mechanism
- [ ] Implement disease tracking over time
- [ ] Create API endpoints for integration

---

<div align="center">

**Made with ❤️ by Group 13**

⭐ Star this repository if you found it helpful!

</div>
