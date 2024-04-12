import os

parser_dir = os.getcwd()
root_dir = os.path.abspath(os.path.join(parser_dir, os.pardir))
data_dir = os.path.join(root_dir, "data/")

parametric_study_data_dir = os.path.join(data_dir, "parametric_study/")