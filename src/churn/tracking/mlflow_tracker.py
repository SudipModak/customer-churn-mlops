import mlflow

class MLflowTracker:
    @staticmethod
    def start_run(run_name):
        return mlflow.start_run(
            run_name=run_name
        )