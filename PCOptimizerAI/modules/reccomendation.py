class Recommendation:
    def __init__(self, cluster_label):
        """
        Initializes the Recommendation object with a cluster label.
        
        Parameters:
        cluster_label (int): The label of the cluster which determines the type of recommendation.
        """
        self.cluster_label = cluster_label
    
    def make_recommendation(self):
        """
        Provides a recommendation based on the cluster label.

        The cluster label is used to determine the type of workload and suggest 
        appropriate actions to optimize performance. The labels represent different
        types of usage scenarios:

        - 0: Light work (e.g., basic tasks or energy-saving mode)
        - 1: Intensive work (e.g., high-performance tasks)
        - 2: Gaming (e.g., high-demand applications)

        Returns:
        str: A recommendation message based on the cluster label.
        """
        if self.cluster_label == 0:
            return "Light work: you can reduce processor power to save energy."
        elif self.cluster_label == 1:
            return "Intensive work: optimize system performance settings."
        elif self.cluster_label == 2:
            return "Gaming: close non-essential applications to improve performance."
        else:
            return "Unknown cluster label: please check the input."

# Example usage:
# Create an instance of Recommendation with a cluster label
rec = Recommendation(cluster_label=1)
# Get the recommendation based on the cluster label
print(rec.make_recommendation())  # Output: Intensive work: optimize system performance settings.







