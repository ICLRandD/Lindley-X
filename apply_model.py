"""
Apply the Lindley-X reportability model to plain-text version of judgments. 

The model returns a prediction of 'reportable' for significant cases and 'unreportable'
for less significant cases. The results are saved out to CSV. 

Usage:

python3 apply_model.py <path/to/text/files> <path/to/model> <path/to/output/csv/file> 

e.g. 

python3 apply_model.py /sample_data /model/lindley_x.pkl predictions.csv
"""

from pathlib import Path
from wasabi import Printer
import plac
import joblib
import pandas as pd

from extract_features import feature_extraction

EXPORT_LIST = []
PREDICTION = []
CONFIDENCE_R = []
CONFIDENCE_U = []

msg = Printer()

@plac.annotations(
    input_dir=("Path to text files", "positional", None, Path),
    model=("Path to model", "positional", None, Path),
    output_file=("Path to export file", "positional", None, Path),
)
def main(input_dir=None, model=None, output_file=None):
    features = feature_extraction(input_dir)
    # load_model
    lindley_x_model = joblib.load(model)

    for row in features:
        X = row[1:13]
        prediction = lindley_x_model.predict([X])
        prediction = str(prediction).replace("[", "")
        prediction = prediction.replace("]", "")
        confidence = lindley_x_model.predict_proba([X])
        print(row[0], prediction, confidence)
        EXPORT_LIST.append(row)
        PREDICTION.append(prediction)
        CONFIDENCE_R.append(confidence[0,0])
        CONFIDENCE_U.append(confidence[0,1])

    df = pd.DataFrame(EXPORT_LIST)
    df.columns = [
        "casename",
        "total_tokens",
        "total_entities",
        "ents_to_tokens",
        "total_cases_cited",
        "total_sentences",
        "axioms",
        "conclusions",
        "issues",
        "legal_test",
        "uncat",
        "total_special_sentences",
        "special_to_total_sents",
    ]
    df["prediction"] = PREDICTION
    df["confidence_rep"] = CONFIDENCE_R
    df["confidence_unrep"] = CONFIDENCE_U
    df.to_csv(output_file)

    msg.good(f"Done and Done! Predictions saved to {output_file}")


if __name__ == "__main__":

    plac.call(main)
