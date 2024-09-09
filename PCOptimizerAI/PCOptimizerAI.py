# -*- coding: utf-8 -*-

from modules.monitor import ResourceMonitor
from modules.bottleneck import BottleNeck
from modules.optimizer import ResourceOptimizer
from modules.nlp_interface import NLPQuestionAnswering
from modules.reccomendation import Recommendation

import tkinter as tk
from tkinter import ttk
import threading

class PCOptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PC Optimizer AI")
        
        # Monitor
        self.monitor = ResourceMonitor(duration=10, interval=1)
        
        # Bottleneck
        self.bottleneck = BottleNeck()
        
        # Optimizer
        self.optimizer = ResourceOptimizer()
        
        # NLP Interface
        self.nlp_qa = NLPQuestionAnswering(model_path="modules/models/distilbert-base-cased-distilled-squad")
        
        # UI Elements
        self.create_widgets()
        
        # Start monitoring in a separate thread
        self.monitor_thread = threading.Thread(target=self.monitor_resources)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
    
    def create_widgets(self):
        # CPU and RAM usage labels
        self.cpu_label = ttk.Label(self.root, text="CPU Usage: ")
        self.cpu_label.grid(column=0, row=0, padx=10, pady=10)
        
        self.ram_label = ttk.Label(self.root, text="RAM Usage: ")
        self.ram_label.grid(column=0, row=1, padx=10, pady=10)
        
        # Recommendation label
        self.recommendation_label = ttk.Label(self.root, text="Recommendation: ")
        self.recommendation_label.grid(column=0, row=2, padx=10, pady=10)
        
        # NLP Question Entry
        self.question_entry = ttk.Entry(self.root, width=50)
        self.question_entry.grid(column=0, row=3, padx=10, pady=10)
        
        # NLP Answer Label
        self.answer_label = ttk.Label(self.root, text="Answer: ")
        self.answer_label.grid(column=0, row=4, padx=10, pady=10)
        
        # Buttons
        self.ask_button = ttk.Button(self.root, text="Ask", command=self.ask_question)
        self.ask_button.grid(column=1, row=3, padx=10, pady=10)
        
        self.optimize_button = ttk.Button(self.root, text="Optimize", command=self.optimize_resources)
        self.optimize_button.grid(column=1, row=2, padx=10, pady=10)
    
    def monitor_resources(self):
        while True:
            data = self.monitor.monitor_resources()
            if data:
                cpu_usage, ram_usage = data[-1]
                self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
                self.ram_label.config(text=f"RAM Usage: {ram_usage}%")
                
                # Check for bottlenecks
                bottleneck_message = self.bottleneck.check_bottlenecks(cpu_usage, ram_usage)
                self.recommendation_label.config(text=f"Recommendation: {bottleneck_message}")
    
    def ask_question(self):
        question = self.question_entry.get()
        if not question.strip():
            self.answer_label.config(text="Answer: Please enter a question.")
            return
        
        # Build a more detailed context
        cpu_usage = self.cpu_label.cget("text").split(": ")[1][:-1]
        ram_usage = self.ram_label.cget("text").split(": ")[1][:-1]
        recommendation = self.recommendation_label.cget("text").split(": ")[1]

        context = f"CPU Usage: {cpu_usage}% | RAM Usage: {ram_usage}% | Recommendation: {recommendation}"

        # Debug print to verify context
        print(f"Context: {context}")

        # Predefined answers for specific questions
        if "improve my system's performance" in question.lower():
            answer = "You can improve your system's performance by closing unnecessary applications, optimizing startup programs, and ensuring your system is free of malware."
        elif "high cpu usage" in question.lower():
            answer = "If your CPU usage is high, consider closing intensive applications, reducing process priority, or upgrading your hardware."
        elif "free up ram" in question.lower():
            answer = "To free up RAM, close unused applications, disable startup programs, and consider adding more physical RAM."
        elif "current cpu usage" in question.lower() or "cpu usage" in question.lower():
            answer = f"The current CPU usage is {cpu_usage}%."
        elif "current ram usage" in question.lower() or "ram usage" in question.lower():
            answer = f"The current RAM usage is {ram_usage}%."
        elif "reduce cpu usage" in question.lower():
            answer = "You can reduce CPU usage by closing unnecessary applications, reducing process priority, or upgrading your CPU."
        elif "tips for optimizing my computer" in question.lower():
            answer = "Some tips for optimizing your computer include: keeping your software updated, running regular malware scans, and cleaning up your disk space."
        elif "make my computer run faster" in question.lower():
            answer = "To make your computer run faster, consider upgrading your hardware, optimizing your startup programs, and keeping your system free of malware."
        elif "common causes of high cpu usage" in question.lower():
            answer = "Common causes of high CPU usage include running too many applications simultaneously, malware infections, and insufficient hardware resources."
        elif "current recommendation" in question.lower():
            answer = f"The current recommendation for your system is: {recommendation}."
        elif "follow the recommendation" in question.lower():
            answer = "To follow the recommendation, take the suggested actions such as closing unused applications or optimizing system settings."

        # Use NLP model for other questions
        else:
            answer = self.nlp_qa.get_response(question, context)
            if "Recommendation: Recommendation:" in answer:
                answer = answer.replace("Recommendation: Recommendation:", "Recommendation:")
            if "CPU Usage:" in answer or "RAM Usage:" in answer:
                answer = "I'm sorry, I couldn't find a relevant answer. Please try asking in a different way."

        self.answer_label.config(text=f"Answer: {answer}")
    
    def optimize_resources(self):
        try:
            cpu_usage_text = self.cpu_label.cget("text").split(": ")[1][:-1]
            ram_usage_text = self.ram_label.cget("text").split(": ")[1][:-1]
            if cpu_usage_text and ram_usage_text:
                cpu_usage = float(cpu_usage_text)
                ram_usage = float(ram_usage_text)
                result = self.optimizer.optimize(cpu_usage, ram_usage)
                self.recommendation_label.config(text=f"Recommendation: {result}")
            else:
                print("CPU or RAM usage text is empty.")
        except ValueError as e:
            print(f"Error converting usage to float: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PCOptimizerApp(root)
    root.mainloop()
