import os
import sys
import logging
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Define the logging string format
logging_str = "[%(asctime)s: %(lineno)d - %(name)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory to store the log files
log_dir = "logs"

# Define the log file path
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging
# Set the log level to INFO
# Set the log format
# Add a file handler to store logs in the log file
# Add a stream handler to display logs on the console
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Get the logger for the current module
# The logger is named "Bank Churn Project Logger"
logger = logging.getLogger("Bank Churn Project Logger")

# The logger is used throughout the project to log messages


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            RandomGrid = RandomizedSearchCV(model,
                                             para,
                                             cv=5,
                                             verbose=0,
                                             n_jobs=10,
                                             random_state=42)

            RandomGrid.fit(X_train, y_train)

            model.set_params(**RandomGrid.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_accuracy = accuracy_score(y_train, y_train_pred)
            train_model_precision = precision_score(y_train, y_train_pred)
            train_model_recall = recall_score(y_train, y_train_pred)
            train_model_f1_score = f1_score(y_train, y_train_pred)

            test_model_accuracy = accuracy_score(y_test, y_test_pred)
            test_model_precision = precision_score(y_test, y_test_pred)
            test_model_recall = recall_score(y_test, y_test_pred)
            test_model_f1_score = f1_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = {
                'train_model_accuracy': train_model_accuracy,
                'train_model_precision': train_model_precision,
                'train_model_recall': train_model_recall,
                'train_model_f1_score': train_model_f1_score,
                'test_model_accuracy': test_model_accuracy,
                'test_model_precision': test_model_precision,
                'test_model_recall': test_model_recall,
                'test_model_f1_score': test_model_f1_score
            }
            

        return report

    except Exception as e:
        raise e
