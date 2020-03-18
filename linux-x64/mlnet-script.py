import argparse
import os
import stat
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
    data_file = os.path.join(os.getcwd(), args.data_file)
    output_dir = os.path.join(os.getcwd(), args.output_dir)
    model_file = args.model_file
    exe = os.path.join(os.getcwd(), args.exe)

    # Need to give correct permissions to executable
    st=os.stat(exe)
    os.chmod(exe, st.st_mode | stat.S_IEXEC)

    print('cur dir is {}, containing {}'.format(os.getcwd(), os.listdir(os.getcwd())))
    os.makedirs(name=output_dir, exist_ok=True)

    args = [exe, data_file, os.path.join(output_dir, model_file)]
    
    subprocess.run(args, stdout=FNULL, stderr=FNULL, shell=False)

if (__name__=='__main__'):
    main()