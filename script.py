import argparse
import subprocess

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--exe', type=str, default=None,
        help='path to exe')
    parser.add_argument('--data_file', type=str, default=None,
        help='path to data file')
    parser.add_argument('--output_path', type=str, default=None,
        help='path to store your model')

    args = parser.parse_args()
    FNULL = open(os.devnull, 'w')
    exe = args.exe
    filename = args.data_file
    output = args.output_path
    args = exe + " " + filename + " " + output

    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)