#!/bin/bash
#SBATCH --partition=free_gpu,kamiak        ### Partition (like a queue in PBS)
##SBATCH --partition=test        ### Partition (like a queue in PBS)
#SBATCH --job-name=extract_features      ### Job Name
#SBATCH --output=/data/vcea/n.kannappanjayakodi/run_results/extract_features.out         ### File in which to store job output
#SBATCH --error=/data/vcea/n.kannappanjayakodi/run_results/extract_features.err          ### File in which to store job error messages
#SBATCH --time=0-03:01:00       ### Wall clock time limit in Days-HH:MM:SS
#SBATCH --nodes=1               ### Node count required for the job
#SBATCH --ntasks-per-node=1     ### Nuber of tasks to be launched per Node
#SBATCH --gres=gpu:1          ### General REServation of gpu:number of GPUs

python extract_features.py