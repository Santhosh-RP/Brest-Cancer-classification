class DataProcessingError(Exception):
    """Exception raised for errors during data preprocessing."""
    def __init__(self, message="Error occurred during data processing"):
        self.message = message
        super().__init__(self.message)


class ModelTrainingError(Exception):
    """Exception raised for errors during model training."""
    def __init__(self, message="Error occurred during model training"):
        self.message = message
        super().__init__(self.message)


class ModelEvaluationError(Exception):
    """Exception raised for errors during model evaluation."""
    def __init__(self, message="Error occurred during model evaluation"):
        self.message = message
        super().__init__(self.message)


class DeploymentError(Exception):
    """Exception raised for errors during model deployment."""
    def __init__(self, message="Error occurred during model deployment"):
        self.message = message
        super().__init__(self.message)


class DataLoadingError(Exception):
    """Exception raised when there is an issue loading the dataset."""
    def __init__(self, message="Error occurred while loading the dataset"):
        self.message = message
        super().__init__(self.message)


class FileNotFoundCustomError(Exception):
    """Exception raised when a specified file is not found."""
    def __init__(self, message="File not found"):
        self.message = message
        super().__init__(self.message)
