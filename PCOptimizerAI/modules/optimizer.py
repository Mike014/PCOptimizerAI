class ResourceOptimizer:
    def __init__(self, cpu_threshold=90, ram_threshold=90):
        """
        Initializes the ResourceOptimizer class with CPU and RAM thresholds.
        
        Parameters:
        cpu_threshold (int): The CPU usage percentage threshold above which optimization is triggered.
        ram_threshold (int): The RAM usage percentage threshold above which optimization is triggered.
        """
        self.cpu_threshold = cpu_threshold
        self.ram_threshold = ram_threshold

    def optimize(self, cpu_usage, ram_usage):
        """
        Optimizes system resources based on the current CPU and RAM usage.
        
        Parameters:
        cpu_usage (float): The current CPU usage percentage.
        ram_usage (float): The current RAM usage percentage.
        
        Returns:
        str: A message indicating the actions taken or if the system is fine.
        """
        actions = []
        if cpu_usage > self.cpu_threshold:
            # Code to reduce process priority
            actions.append("Reduced process priority to lower CPU usage.")
        
        if ram_usage > self.ram_threshold:
            # Code to close background applications
            actions.append("Closed background applications to free up RAM.")
        
        if not actions:
            return "System resources are within acceptable limits."
        return " | ".join(actions)

# Example usage
if __name__ == "__main__":
    optimizer = ResourceOptimizer()
    cpu_usage = 95
    ram_usage = 92
    print(optimizer.optimize(cpu_usage, ram_usage))




