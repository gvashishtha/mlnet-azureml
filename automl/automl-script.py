import argparse
import os
import stat
import subprocess

from azureml.core import Run

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_file', type=str, default=None,
        help='path to data file')
    parser.add_argument('--task', type=str, default='regression',
        help='AutoML task')
    parser.add_argument('--label_column', type=str, default='SalePrice',
        help='labeled column')
    parser.add_argument('--max_time', type=int, default=60,
        help='max time to explore in seconds')
    parser.add_argument('--output_path', type=str, default='outputs',
        help='output path')

    args = parser.parse_args()
    FNULL = open(os.devnull, 'w')
    data_file = os.path.join(os.getcwd(), args.data_file)
    max_time = args.max_time
    output_path = args.output_path
    os.makedirs(output_path, exist_ok=True)
    task = args.task
    label_column = args.label_column

    args = ['mlnet', 'auto-train', 
            '--task', task,
            '--dataset', data_file,
            '--label-column-name', label_column, 
            '--max-exploration-time', str(max_time),
            '--output-path', output_path]

    subprocess.run(args, stdout=FNULL, stderr=FNULL, shell=False)

if (__name__=='__main__'):
    main()