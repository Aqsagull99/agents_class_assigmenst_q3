# 🧭 AI Travel Designer Agent

This project is a smart, AI-powered travel planning system using OpenAI Agent SDK. It coordinates between specialized
agents to plan a complete travel experience for users—based on their mood, interests, and preferences.

---

## ✨ What It Does

The system interacts through the command-line and simulates a complete trip plan:

- Recommends **destinations** based on mood or interests  
- Suggests **flights and hotels** using mock data tools  
- Recommends **places to visit and food options**

---

## 🧠 Agents Involved

The core agent (`TravelMasterAgent`) delegates tasks to the following:

| Agent Name        | Responsibility                      |
|------------------|--------------------------------------|
| `DestinationAgent` | Finds suitable travel destinations   |
| `BookingAgent`     | Simulates flight/hotel booking       |
| `ExploreAgent`     | Suggests attractions and local food  |

All agents are coordinated using `handoffs`.

---

#run this with command 
uv run main.py
