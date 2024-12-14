import numpy as np

def compute_eigenvalues(matrix):
    """
    Compute the eigenvalues of a given matrix.

    Parameters:
    matrix (list of list of floats): The input matrix.

    Returns:
    list: Eigenvalues of the matrix.
    """
    try:
        eigenvalues = np.linalg.eigvals(matrix)
        return eigenvalues
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
if __name__ == "__main__":
    matrix = [[2, -1], [-1, 2]]
    print(f"Matrix: {matrix}")
    print(f"Eigenvalues: {compute_eigenvalues(matrix)}")
