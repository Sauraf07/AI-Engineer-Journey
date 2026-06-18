# Phase 4: Deep Learning with PyTorch (Day 61 - Day 90)

<div align="center">

# 🧠 Deep Learning Roadmap
### From Neural Networks to Computer Vision & NLP

**Duration:** 30 Days  
**Study Time:** 4–6 Hours Daily  
**Goal:** Become Job-Ready in Deep Learning Fundamentals using PyTorch

</div>

---

# 🎯 Phase Goal

By the end of this phase, you will be able to:

✅ Understand Neural Networks

✅ Understand Forward & Backpropagation

✅ Build Deep Learning Models using PyTorch

✅ Train and Evaluate Models

✅ Work with CNNs

✅ Build Image Classification Projects

✅ Understand RNNs & LSTMs

✅ Build NLP Models

✅ Create Production-Ready Deep Learning Projects

---

# 📅 Week 1: Deep Learning Foundations

---

# Day 61: Introduction to Deep Learning

## Topics

- What is Deep Learning?
- AI vs ML vs Deep Learning
- Applications of Deep Learning
- Why Deep Learning Works
- Neural Networks Overview

## Why It Matters

Deep Learning powers:

- ChatGPT
- Gemini
- Claude
- Self Driving Cars
- Face Recognition
- Recommendation Systems

## Learning Objectives

- Understand Deep Learning Ecosystem
- Learn Neural Network Basics
- Understand Training Process

## Practical

Create Notes:

```text
AI
 └── Machine Learning
      └── Deep Learning
```

## Resources

### Free

- Deep Learning Specialization (Audit)
- PyTorch Documentation

### YouTube

- Krish Naik Deep Learning Playlist
- CampusX Deep Learning Playlist

---

# Day 62: Mathematics for Deep Learning

## Topics

- Scalars
- Vectors
- Matrices
- Tensors

## Learn

```python
import torch

x = torch.tensor([1,2,3])
print(x)
```

## Practical

Create:

- Vector Addition
- Matrix Multiplication

## Interview Questions

### Q1 What is a Tensor?

Answer:

A Tensor is a multidimensional array used in Deep Learning.

---

# Day 63: Introduction to PyTorch

## Topics

- Installation
- Tensor Operations
- GPU Support

## Learn

```python
import torch

x = torch.tensor([1,2,3])
y = torch.tensor([4,5,6])

print(x+y)
```

## Practical

Perform:

- Addition
- Multiplication
- Matrix Operations

---

# Day 64: Autograd in PyTorch

## Topics

- Computational Graph
- Automatic Differentiation

## Learn

```python
x = torch.tensor(2.0, requires_grad=True)

y = x**2

y.backward()

print(x.grad)
```

## Interview Questions

### What is Autograd?

Autograd automatically computes gradients.

---

# Day 65: Neural Network Basics

## Topics

- Neuron
- Activation Function
- Hidden Layers
- Output Layer

## Learn

Structure

```text
Input → Hidden Layer → Output
```

## Practical

Draw:

- Single Layer Network
- Multi Layer Network

---

# Day 66: Activation Functions

## Topics

- Sigmoid
- Tanh
- ReLU
- Leaky ReLU
- Softmax

## Learn

Why ReLU is widely used.

## Interview Questions

### Why ReLU?

- Faster
- Solves Vanishing Gradient Problem

---

# Day 67: Build First Neural Network

## Topics

- PyTorch nn.Module

## Learn

```python
import torch.nn as nn

class NeuralNet(nn.Module):

    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(10,5)

    def forward(self,x):
        return self.fc1(x)
```

## Practical

Build:

- House Price Prediction Model

---

# Week 1 Assignment

Build:

### Student Marks Predictor

Input:

- Hours Studied

Output:

- Predicted Marks

---

# 📅 Week 2: Training Deep Learning Models

---

# Day 68: Loss Functions

## Topics

- MSE Loss
- Cross Entropy Loss

## Learn

```python
loss = criterion(outputs, labels)
```

## Interview Questions

### What is Loss Function?

Measures prediction error.

---

# Day 69: Optimizers

## Topics

- Gradient Descent
- SGD
- Adam

## Learn

```python
optimizer = torch.optim.Adam(model.parameters())
```

---

# Day 70: Forward Propagation

## Topics

- Prediction Flow

```text
Input → Hidden → Output
```

---

# Day 71: Backpropagation

## Topics

- Chain Rule
- Weight Updates

## Why Important

Neural Networks learn using Backpropagation.

---

# Day 72: Training Loop

## Learn

```python
for epoch in range(100):

    optimizer.zero_grad()

    outputs = model(inputs)

    loss = criterion(outputs, labels)

    loss.backward()

    optimizer.step()
```

---

# Day 73: Model Evaluation

## Metrics

- Accuracy
- Precision
- Recall
- F1 Score

---

# Day 74: Save & Load Models

## Learn

```python
torch.save(model.state_dict(),"model.pth")
```

---

# Week 2 Assignment

Build:

### Customer Churn Prediction

Dataset:

- Kaggle Telecom Churn Dataset

---

# 📅 Week 3: Computer Vision

---

# Day 75: Introduction to Computer Vision

## Topics

- Image Classification
- Object Detection
- Segmentation

---

# Day 76: Image Processing

## Libraries

- OpenCV
- Pillow

## Practical

Load Image

Resize Image

Convert Image

---

# Day 77: CNN Basics

## Topics

- Convolution
- Kernel
- Pooling

## Architecture

```text
Image
 ↓
Conv Layer
 ↓
Pooling
 ↓
Dense Layer
 ↓
Output
```

---

# Day 78: CNN in PyTorch

## Practical

Build CNN

```python
nn.Conv2d()
```

---

# Day 79: MNIST Digit Classification

## Project

Train CNN on MNIST Dataset

Goal:

Predict digits from images.

---

# Day 80: Fashion MNIST

## Project

Clothing Classifier

Classes:

- Shirt
- Shoe
- Bag

---

# Day 81: CIFAR-10 Dataset

## Project

Object Classification

Classes:

- Car
- Cat
- Dog
- Plane

---

# Week 3 Assignment

Build:

### Image Classification System

Features:

- Upload Image
- Predict Class
- Show Confidence Score

---

# 📅 Week 4: NLP with Deep Learning

---

# Day 82: Introduction to NLP

## Topics

- Text Processing
- Tokenization
- Stop Words

---

# Day 83: Word Embeddings

## Topics

- Word2Vec
- GloVe

## Why Important

Convert text into vectors.

---

# Day 84: RNN

## Topics

- Sequential Data
- Hidden States

---

# Day 85: LSTM

## Topics

- Long-Term Memory
- Forget Gate
- Input Gate

## Interview Questions

### Why LSTM over RNN?

Handles long-term dependencies better.

---

# Day 86: Text Classification

## Project

Spam Email Classifier

---

# Day 87: Sentiment Analysis

## Project

Movie Review Classifier

Positive

Negative

Neutral

---

# Day 88: Sequence Models

## Topics

- Language Modeling
- Next Word Prediction

---

# Day 89: Mini NLP Project

Build:

### AI Review Analyzer

Features:

- Input Review
- Predict Sentiment
- Confidence Score

---

# Day 90: Phase Revision + Portfolio Upload

## Upload All Projects

Create Repository Structure

```text
Deep-Learning/
│
├── Neural-Network-Basics
├── Student-Marks-Predictor
├── Customer-Churn-Prediction
├── CNN-MNIST
├── Fashion-MNIST
├── CIFAR10-Classifier
├── Spam-Classifier
├── Sentiment-Analysis
└── AI-Review-Analyzer
```

---

# 🚀 Phase 4 Portfolio Projects

## Beginner

### 1. Student Marks Predictor

### 2. House Price Predictor

### 3. Customer Churn Predictor

---

## Intermediate

### 4. MNIST Classifier

### 5. Fashion Classifier

### 6. CIFAR-10 Classifier

---

## Advanced

### 7. Spam Detection System

### 8. Sentiment Analysis System

### 9. AI Review Analyzer

---

# 📚 Best Resources

## Official Documentation

### PyTorch

https://pytorch.org/docs/stable/index.html

---

## Free Resources

### Deep Learning Specialization

https://www.coursera.org/specializations/deep-learning

### FastAI

https://course.fast.ai

---

## YouTube

### Krish Naik

https://www.youtube.com/@krishnaik06

### CampusX

https://www.youtube.com/@campusx-official

### freeCodeCamp

https://www.youtube.com/@freecodecamp

---

# 📖 Recommended Books

### Deep Learning with PyTorch

### Hands-On Machine Learning

### Deep Learning by Ian Goodfellow

---

# 🎯 Interview Preparation

## Deep Learning Questions

### What is Deep Learning?

### What is a Neural Network?

### What is Backpropagation?

### What is Gradient Descent?

### What is ReLU?

### What is CNN?

### What is Pooling?

### What is Overfitting?

### What is Dropout?

### What is Batch Normalization?

### What is RNN?

### What is LSTM?

### Difference Between CNN and RNN?

### What is Transfer Learning?

### Why PyTorch?

---

# 🏆 Phase 4 Completion Milestone

After completing this phase, you will:

✅ Understand Deep Learning Fundamentals

✅ Build Neural Networks from Scratch

✅ Use PyTorch Professionally

✅ Build Computer Vision Projects

✅ Build NLP Projects

✅ Create Deep Learning Portfolio Projects

✅ Be Ready for Phase 5: NLP & Transformers

---

# Next Phase

➡️ Phase 5: NLP & Transformers

Topics:

- NLP Fundamentals
- Tokenization
- Attention Mechanism
- Transformers
- BERT
- GPT
- Hugging Face
- Fine-Tuning
- Embeddings
- LLM Foundations