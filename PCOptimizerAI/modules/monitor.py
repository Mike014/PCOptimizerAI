import psutil
import time

class ResourceMonitor:
    def __init__(self, duration=60, interval=1):
        """
        Initializes the ResourceMonitor object with a duration and interval.
        
        Parameters:
        duration (int): The total time in seconds to monitor resources. Default is 60 seconds.
        interval (int): The time interval in seconds between each monitoring. Default is 1 second.
        """
        self.duration = duration
        self.interval = interval

    def monitor_resources(self):
        """
        Monitors CPU and RAM usage over the specified duration and interval.

        Returns:
        list of tuples: A list where each tuple contains CPU usage percentage and RAM usage percentage at a given time.
        """
        # Initialize an empty list to store the resource usage data
        data = []
        
        # Loop through the specified duration with the given interval
        for _ in range(int(self.duration / self.interval)):
            # Get the current CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=self.interval)
            # Get the current RAM usage percentage
            ram_usage = psutil.virtual_memory().percent
            # Append the current usage to the data list
            data.append((cpu_usage, ram_usage))
            # Print the current CPU and RAM usage
            print(f"CPU: {cpu_usage}%, RAM: {ram_usage}%")
        
        return data

# Example usage
if __name__ == "__main__":
    # Create an instance of ResourceMonitor
    monitor = ResourceMonitor(duration=10, interval=1)
    # Monitor CPU and RAM usage
    monitor.monitor_resources()


    



