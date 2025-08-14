from networksecurity.entity.artifact_entity import ClassificationMatricArtifact
from networksecurity.exception.exception import NetworkSecurityException
from sklearn.metrics import f1_score, precision_score, recall_score
import sys, os


def get_classification_score(y_true: list, y_pred: list) -> ClassificationMatricArtifact:
    """
    Calculate classification metrics such as F1 score, precision, and recall.
    
    :param y_true: List of true labels.
    :param y_pred: List of predicted labels.
    :return: ClassificationMatricArtifact containing the calculated metrics.
    """
    try:
        f1 = f1_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        
        return ClassificationMatricArtifact(f1_score=f1, precision_score=precision, recall_score=recall)
    
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e