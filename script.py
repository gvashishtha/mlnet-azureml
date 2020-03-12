import argparse
import os
import subprocess

from azureml.core import Run

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--exe', type=str, default=None,
        help='path to exe')
    parser.add_argument('--data_file', type=str, default=None,
        help='path to data file')
    parser.add_argument('--output_dir', type=str, default=None,
        help='path to store your model')
    parser.add_argument('--model_file', type=str, default=None,
        help='path to model file')

    args = parser.parse_args()
    FNULL = open(os.devnull, 'w')
    exe = args.exe
    data_file = args.data_file
    output_dir = args.output_dir
    model_file = args.model_file

    print('cur dir is {}, containing {}'.format(os.getcwd(), os.listdir(os.getcwd())))
    os.makedirs(name=output_dir, exist_ok=True)

    args = [exe, data_file, os.path.join(output_dir, model_file)]
    
    subprocess.run(args, stdout=FNULL, stderr=FNULL, shell=False)

if (__name__=='__main__'):
    main()