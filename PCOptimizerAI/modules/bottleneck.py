class BottleNeck:
    def __init__(self, cpu_threshold=90, ram_threshold=90):
        """
        Initializes the ResourceMonitor with specified CPU and RAM thresholds.

        Parameters:
        cpu_threshold (float): The CPU usage percentage threshold for considering it overloaded. Default is 90%.
        ram_threshold (float): The RAM usage percentage threshold for considering it nearly full. Default is 90%.
        """
        self.cpu_threshold = cpu_threshold
        self.ram_threshold = ram_threshold

    def check_bottlenecks(self, cpu_usage, ram_usage):
        """
        Checks if CPU or RAM usage exceeds the specified thresholds and provides recommendations.

        Parameters:
        cpu_usage (float): The current CPU usage percentage.
        ram_usage (float): The current RAM usage percentage.

        Returns:
        str: A recommendation message based on the current CPU and RAM usage.
        """
        # Check if the CPU usage exceeds the threshold
        if cpu_usage > self.cpu_threshold:
            return "The CPU is overloaded. Consider postponing intensive tasks."
        
        # Check if the RAM usage exceeds the threshold
        if ram_usage > self.ram_threshold:
            return "RAM is nearing its limit. Close unused applications."
        
        # If neither usage exceeds the threshold, the system is in good condition
        return "The system is in good condition."

# Example usage
if __name__ == "__main__":
    monitor = BottleNeck()
    cpu_usage = 85  # Example CPU usage percentage
    ram_usage = 92  # Example RAM usage percentage
    print(monitor.check_bottlenecks(cpu_usage, ram_usage))





