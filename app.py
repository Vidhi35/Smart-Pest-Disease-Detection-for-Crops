"""
Plant Disease Detection System
- Upload or capture image
- Predict disease using Hugging Face model
- Get remedies using Groq (Llama 3.3 70B) via LangChain
"""

import os
import io
import base64
from PIL import Image
import gradio as gr
from transformers import pipeline
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

# ============================================================================
# CONFIGURATION
# ============================================================================

# Load environment variables from .env file
load_dotenv()

# Set your Groq API Key here or via environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# Hugging Face model for plant disease classification
# Using a popular plant disease detection model
HF_MODEL = "linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification"

# ============================================================================
# MODEL INITIALIZATION
# ============================================================================

print("Loading Hugging Face model...")
try:
    # Initialize the image classification pipeline
    disease_classifier = pipeline(
        "image-classification",
        model=HF_MODEL,
        top_k=3  # Get top 3 predictions
    )
    print("✓ Hugging Face model loaded successfully")
except Exception as e:
    print(f"✗ Error loading Hugging Face model: {e}")
    disease_classifier = None

print("Initializing LangChain with Groq...")
try:
    # Initialize Groq with Llama 3.3 70B (free and powerful)
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",  # You can also use: "mixtral-8x7b-32768", "llama-3.1-70b-versatile"
        groq_api_key=GROQ_API_KEY,
        temperature=0.7,
        max_tokens=1024
    )
    
    # Create prompt template for disease remedies
    remedy_prompt = PromptTemplate(
        input_variables=["disease_name", "confidence"],
        template="""You are an expert agricultural consultant specializing in plant diseases.

A plant disease has been detected with the following information:
- Disease Name: {disease_name}
- Confidence Level: {confidence}%

Please provide a comprehensive response in MARKDOWN format with the following sections:

## 📖 Disease Overview
Brief description of this plant disease (2-3 sentences)

## 🔍 Symptoms
Key symptoms to look for (use bullet points with - )

## 🦠 Causes
What causes this disease (use bullet points with - )

## 💊 Treatment Recommendations

### ⚡ Immediate Actions
- List immediate steps to take

### 🌱 Organic/Natural Remedies
- List organic and natural treatment options

### 🧪 Chemical Treatments (if necessary)
- List chemical treatment options

### 🛡️ Preventive Measures
- List preventive measures to avoid future infections

## ⏱️ Recovery Timeline
Expected recovery timeline and what to expect

## 💡 Additional Tips
Any other helpful advice for managing this disease

IMPORTANT: Use proper Markdown formatting:
- Use ## for main sections
- Use ### for subsections
- Use **bold** for emphasis
- Use bullet points with - for lists
- Keep it well-structured and easy to read
"""
    )
    
    # Create chain using LCEL (LangChain Expression Language)
    remedy_chain = remedy_prompt | llm
    print("✓ LangChain initialized successfully")
except Exception as e:
    print(f"✗ Error initializing LangChain: {e}")
    llm = None
    remedy_chain = None

# ============================================================================
# CORE FUNCTIONS
# ============================================================================

def predict_disease(image):
    """
    Predict plant disease from image using Hugging Face model
    
    Args:
        image: PIL Image or numpy array
        
    Returns:
        tuple: (predictions_list, top_disease, top_confidence)
    """
    if disease_classifier is None:
        return None, "Model not loaded", 0.0
    
    try:
        # Run prediction
        predictions = disease_classifier(image)
        
        # Extract top prediction
        top_prediction = predictions[0]
        disease_name = top_prediction['label']
        confidence = top_prediction['score'] * 100
        
        # Format all predictions for display
        predictions_text = "\n".join([
            f"{i+1}. {pred['label']}: {pred['score']*100:.2f}%"
            for i, pred in enumerate(predictions)
        ])
        
        return predictions_text, disease_name, confidence
    
    except Exception as e:
        return None, f"Error during prediction: {str(e)}", 0.0


def get_remedies(disease_name, confidence):
    """
    Get treatment remedies using Groq via LangChain
    
    Args:
        disease_name: Name of the detected disease
        confidence: Confidence score of the prediction
        
    Returns:
        str: Formatted remedies and treatment information
    """
    if remedy_chain is None:
        return "⚠️ LangChain not initialized. Please set your GROQ_API_KEY environment variable."
    
    try:
        # Generate remedies using LangChain with LCEL
        response = remedy_chain.invoke({
            "disease_name": disease_name,
            "confidence": f"{confidence:.2f}"
        })
        # Extract content from AIMessage
        return response.content
    
    except Exception as e:
        return f"⚠️ Error generating remedies: {str(e)}\n\nPlease check your Groq API key."


def process_image(image):
    """
    Main processing function: predict disease and get remedies
    
    Args:
        image: Input image from Gradio
        
    Returns:
        tuple: (predictions_text, remedies_text)
    """
    if image is None:
        return "⚠️ Please upload or capture an image first.", ""
    
    # Step 1: Predict disease
    predictions_text, disease_name, confidence = predict_disease(image)
    
    if predictions_text is None:
        return disease_name, ""  # disease_name contains error message
    
    # Format prediction results with enhanced Markdown
    prediction_output = f"""
# 🔍 Disease Detection Results

---

### 📊 Top Predictions:

{predictions_text}

---

### 🎯 Primary Diagnosis

**Disease:** {disease_name}  
**Confidence Level:** {confidence:.2f}%

---
"""
    
    # Step 2: Get remedies from LLM
    remedies_output = f"""
# 🌿 Treatment & Remedies

## 📋 Detected Disease: **{disease_name}**

---

"""
    remedies_output += get_remedies(disease_name, confidence)
    
    return prediction_output, remedies_output


# ============================================================================
# GRADIO INTERFACE
# ============================================================================

def create_interface():
    """Create and configure Gradio interface"""
    
    with gr.Blocks(title="Plant Disease Detection System") as demo:
        # Header with embedded CSS
        gr.HTML("""
        <style>
        .markdown-text h1 {
            color: #2c3e50;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
            margin-top: 20px;
        }
        .markdown-text h2 {
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 8px;
            margin-top: 18px;
        }
        .markdown-text h3 {
            color: #7f8c8d;
            margin-top: 15px;
        }
        .markdown-text ul {
            line-height: 1.8;
        }
        .markdown-text li {
            margin-bottom: 8px;
        }
        .markdown-text strong {
            color: #2c3e50;
        }
        .markdown-text hr {
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 20px 0;
        }
        </style>
        <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px; margin-bottom: 20px;">
            <h1>🌱 Plant Disease Detection & Treatment System</h1>
            <p>Upload or capture a plant image to detect diseases and get AI-powered treatment recommendations</p>
        </div>
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 📸 Upload or Capture Image")
                
                # Image input with camera and upload options
                image_input = gr.Image(
                    label="Plant Image",
                    type="pil",
                    sources=["upload", "webcam"],
                    height=400
                )
                
                # Process button
                process_btn = gr.Button(
                    "🔬 Analyze Disease",
                    variant="primary",
                    size="lg"
                )
                
                # Info box
                gr.Markdown("""
                **Instructions:**
                1. Upload an image or use your camera
                2. Click 'Analyze Disease' button
                3. View predictions and AI-generated remedies
                
                **Tips for best results:**
                - Ensure good lighting
                - Focus on affected areas
                - Use clear, high-quality images
                """)
            
            with gr.Column(scale=1):
                gr.Markdown("### 📊 Results")
                
                # Predictions output with Markdown for rich formatting
                predictions_output = gr.Markdown(
                    label="Disease Predictions",
                    value="*Upload an image to see predictions...*"
                )
                
                # Remedies output with Markdown for rich formatting
                remedies_output = gr.Markdown(
                    label="Treatment & Remedies (AI-Generated)",
                    value=""
                )
        
        # Footer
        gr.Markdown("""
        ---
        **Powered by:**
        - 🤗 Hugging Face (Disease Detection)
        - 🚀 Groq + Llama 3.3 70B (Treatment Recommendations via LangChain)
        
        *Note: This system provides suggestions only. Always consult with agricultural experts for serious plant health issues.*
        """)
        
        # Event handlers
        process_btn.click(
            fn=process_image,
            inputs=[image_input],
            outputs=[predictions_output, remedies_output]
        )
    
    return demo


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Check if API key is set
    if not GROQ_API_KEY:
        print("\n" + "="*70)
        print("⚠️  WARNING: GROQ_API_KEY not found!")
        print("="*70)
        print("\nTo use the LLM features, please set your Groq API key:")
        print("  - Windows: set GROQ_API_KEY=your_key_here")
        print("  - Linux/Mac: export GROQ_API_KEY=your_key_here")
        print("\nOr add it to a .env file in the project directory.")
        print("\nThe app will still run, but remedy generation will not work.")
        print("="*70 + "\n")
    
    # Create and launch interface
    print("\n🚀 Launching Plant Disease Detection System...")
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )
