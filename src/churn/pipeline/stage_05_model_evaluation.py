from churn.components.model_evaluation import ModelEvaluation


class ModelEvaluationTrainingPipeline:

    def main(self):

        evaluation = ModelEvaluation()

        evaluation.initiate_model_evaluation()