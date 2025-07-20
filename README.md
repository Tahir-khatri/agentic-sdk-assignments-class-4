# Agentic SDK Assignments – Class 4

This repository contains three assignments completed using the **Agentic SDK** and **Gemini API**. These assignments demonstrate how to build AI agents, use handoffs between agents, and integrate tool-based logic.

## 📁 Files

### 1. `product_suggester.py` – Smart Store Agent
An AI agent that suggests a relevant product (like medicine) based on user symptoms or needs.

**Example:**
> Input: "I have a headache"  
> Output: "You can try Panadol. These are effective pain relievers and commonly used to treat headaches."

---

### 2. `mood_handoff.py` – Mood Analyzer with Handoff
Uses **two agents**:
- Agent 1: Detects the user's mood.
- Agent 2: If mood is "sad" or "stressed", it suggests an uplifting activity.

**Example:**
> Input: "I'm feeling low"  
> Output:  
> - Detected Mood: sad  
> - Suggested Activity: "Try going for a walk and listening to your favorite music."

---

### 3. `country_info_toolkit.py` – Country Info Bot (Tools)
An orchestrator agent uses **3 tool functions** to return a country’s:
- Capital  
- Language  
- Population

**Example:**
> Input: "Japan"  
> Output: "Japan: Capital is Tokyo, Language is Japanese, Population is 125 million."

---

## 🔧 Technologies Used
- Python
- [Agentic SDK](https://github.com/panaversity/learn-agentic-ai)
- Gemini 2.0 Flash Model (via Google Generative Language API)
- `asyncio`, `dotenv`

## 🧠 Purpose
This is a **Class 4 assignment** for learning how to:
- Build AI agents
- Use agent handoffs
- Integrate tools with orchestrators

## 📌 Instructions
Make sure to:
- Add your `GEMINI_API_KEY` to a `.env` file
- Run each file using Python 3.10+  
- Install dependencies using `pip install -r requirements.txt` (if needed)

---

### 📅 Instructor Notes
All 3 assignments are implemented with clean code and working logic.  
Feel free to test each script individually.

---

