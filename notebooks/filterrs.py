import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to visualize the matrix
def visualize_convolution(input_size, padding, kernel_size, stride):
    # Compute padded dimensions and output size
    padded_size = input_size + 2 * padding
    output_size = (padded_size - kernel_size) // stride + 1

    # Create input matrix with padding
    input_matrix = np.zeros((padded_size, padded_size))
    if padding > 0:
        input_matrix[padding:padding + input_size, padding:padding + input_size] = 1
    else:
        input_matrix[:input_size, :input_size] = 1

    # Create output matrix for visualization
    output_matrix = np.zeros((output_size, output_size))

    # Plot input and output matrices
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Plot input matrix
    axs[0].imshow(input_matrix, cmap="Greys", interpolation="none")
    axs[0].set_title(f"Input ({padded_size}x{padded_size}) After Padding")
    axs[0].set_xticks(np.arange(-0.5, padded_size, 1))
    axs[0].set_yticks(np.arange(-0.5, padded_size, 1))
    axs[0].grid(which="major", color="black", linestyle="-", linewidth=0.5)
    axs[0].set_xticklabels([])
    axs[0].set_yticklabels([])

    # Plot output matrix
    axs[1].imshow(output_matrix, cmap="Greys", interpolation="none")
    axs[1].set_title(f"Output ({output_size}x{output_size})")
    axs[1].set_xticks(np.arange(-0.5, output_size, 1))
    axs[1].set_yticks(np.arange(-0.5, output_size, 1))
    axs[1].grid(which="major", color="black", linestyle="-", linewidth=0.5)
    axs[1].set_xticklabels([])
    axs[1].set_yticklabels([])

    # Display the plot
    st.pyplot(fig)

# Streamlit app layout
st.title("Interactive Convolution Visualization")
st.sidebar.title("Adjust Parameters")

# Sidebar sliders for user inputs
input_size = st.sidebar.slider("Input Size", min_value=4, max_value=10, value=4, step=1)
padding = st.sidebar.slider("Padding", min_value=0, max_value=5, value=1, step=1)
kernel_size = st.sidebar.slider("Kernel Size", min_value=1, max_value=5, value=2, step=1)
stride = st.sidebar.slider("Stride", min_value=1, max_value=3, value=1, step=1)

# Visualize convolution with current parameters
visualize_convolution(input_size, padding, kernel_size, stride)
