#!/bin/sh

set -xe

#bm_dir="./CommonVoice/cv-corpus-5.1-2020-06-22/en/clips"
bm_dir="./data/bm_test"
test_csv="${bm_dir}/general-test.csv"
train_csv="${bm_dir}/general-train.csv"
dev_csv="${bm_dir}/general-dev.csv"
bm_csv="${bm_dir}/bm.csv"

if [ ! -f DeepSpeech.py ]; then
    echo "Please make sure you run this from DeepSpeech's top level directory."
    exit 1
fi;

# Force only one visible device because we have a single-sample dataset
# and when trying to run on multiple devices (like GPUs), this will break
export CUDA_VISIBLE_DEVICES=0

python -u DeepSpeech.py --noearly_stop \
  --train_files ${train_csv} --train_batch_size 4 \
  --dev_files ${dev_csv} --dev_batch_size 2 \
  --test_files ${test_csv} --test_batch_size 1 \
  --n_hidden 2048 --epochs 10 \
  --max_to_keep 1 --save_checkpoint_dir 'fine_tuning_checkpoints' \
  --load_checkpoint_dir 'load_checkpoints' \
  --load_cudnn \
  --export_dir 'exports' \
  --learning_rate 0.0005 --dropout_rate 0.38 \
  --scorer_path 'deepspeech-0.9.3-models.scorer' | tee /tmp/resume.log

if ! grep "Loading best validating checkpoint from" /tmp/resume.log; then
  echo "Did not resume training from checkpoint"
  exit 1
else
  exit 0
fi
