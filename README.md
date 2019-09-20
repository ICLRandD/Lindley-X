# Lindley-X

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0d/LordLindley_cropp.jpg">

## Installation

**Note** it is strongly recommended that you follow these installation instructions from within a clean virtual environment.

1. Clone this repository
2. Navigate to the repository directory: 
`cd Lindley-X`
3. Install the dependencies: 
`pip install -r requirements.txt` (apologies are due here, the `requirements.txt` file is really bloated -- we will fix this)
4. Install the Blackstone model: 
`pip install https://blackstone-model.s3-eu-west-1.amazonaws.com/en_blackstone_proto-0.0.1.tar.gz`

## Usage

Lindley-X is executed from the command line and takes three positional arguments:

`input_dir` which is the path to a directory consisting of one or more judgments in plain-text format.
`model` which is the path to the Lindley-X model stored in this repo's `model` directory
`output_file` which is the path to a `.csv` file the model's predictions are written to

The Lindley-X model is applied from the command line, like so:

`python3 apply_model.py path/to/text/files path/to/the/model path/to/output/csv/file`

So, an example usage would be

`python3 apply_model.py /sample_data /model/lindley_x_model.pkl my_predictions.csv`

