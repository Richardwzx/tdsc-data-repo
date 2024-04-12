# Import necessary libraries
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import MaxNLocator
import ini

# Define a class to parse and plot data from a parametric study
class parametricStudyParser:
    def __init__(self, rpm : int, metric : str):
        # Initialize with the directory paths and load data files based on RPM
        data_dir = ini.parametric_study_data_dir
        self.metric = metric                    # Selected metric to display
        self.rpm = rpm                          
        
        # Load datasets from CSV files into numpy arrays
        amp_grid_file = os.path.join(data_dir, "amp_" + str(rpm) + ".csv")
        lamda_grid_file = os.path.join(data_dir, "lamda_" + str(rpm) + ".csv")
        oaspl_grid_file = os.path.join(data_dir, "oaspl_" + str(rpm) + ".csv")
        thrust_grid_file = os.path.join(data_dir, "thrust_" + str(rpm) + ".csv")
        
        self.amp = pd.read_csv(amp_grid_file).values
        self.lamda = pd.read_csv(lamda_grid_file).values
        self.oaspl = pd.read_csv(oaspl_grid_file).values
        self.thrust = pd.read_csv(thrust_grid_file).values
        

    # Function to generate surface plots based on the selected metric
    def surf_plot(self):
        # Set plot font size and family
        plt.rcParams['font.size'] = 24
        plt.rcParams['font.family'] = 'Arial'
        
        # Create figure and set ticks
        plt.figure(figsize=(10, 7))
        plt.yticks(np.arange(0.1, 0.5, 0.1))
        plt.xticks(np.arange(0.01, 0.05, 0.01))
        
        # Generate contour plot based on the selected metric
        if self.metric == "thrust":
            contour = plt.contourf(self.amp, self.lamda, self.thrust, levels=200, cmap='magma')
        elif self.metric == "oaspl":
            contour = plt.contourf(self.amp, self.lamda, self.oaspl, levels=200, cmap='magma')
        else:
            # Handle invalid metric selection
            raise ValueError("Metric should be one of the followings:\n1. thrust\n2. oaspl")
        
        # Customize colorbar format and ticks
        cbar = plt.colorbar(contour)
        cbar.formatter = FormatStrFormatter('%.1f')
        cbar.locator = MaxNLocator(nbins=8)  
        cbar.update_ticks()

        # Set axis labels
        plt.xlabel("A (inch)", fontsize=28)
        plt.ylabel(r"$\lambda$ (inch)", fontsize=28)

            
    # Function to display the generated figure
    def show_fig(self):
        plt.show()
        
# Main execution block
if __name__ == "__main__":
    # Clear the console screen (specific to the system's command line interface)
    os.system("clear")
    # Create an instance of the class and generate a plot
    ps_parser = parametricStudyParser(rpm=5000, metric = "oaspl")
    ps_parser.surf_plot()
    ps_parser.show_fig()
