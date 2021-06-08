#!/bin/sh

set -xe

#bm_dir="./CommonVoice/cv-corpus-5.1-2020-06-22/en/clips"
#test_csv="${bm_dir}/test.csv"
#train_csv="${bm_dir}/train.csv"
#dev_csv="${bm_dir}/dev.csv"
bm_dir="./data/bm_test"
bm_csv="${bm_dir}/bm.csv"

if [ ! -f DeepSpeech.py ]; then
    echo "Please make sure you run this from DeepSpeech's top level directory."
    exit 1
fi;

# Force only one visible device because we have a single-sample dataset
# and when trying to run on multiple devices (like GPUs), this will break
export CUDA_VISIBLE_DEVICES=0

python3 -u DeepSpeech.py --noearly_stop \
  --train_files ${bm_csv} --train_batch_size 1 \
  --dev_files ${bm_csv} --dev_batch_size 1 \
  --test_files ${bm_csv} --test_batch_size 1 \
  --n_hidden 2048 --epochs 10 \
  --max_to_keep 1 --save_checkpoint_dir '/fine_tuning_checkpoints' \
  --load_checkpoint_dir '/load_checkpoints' \
  --load_cudnn \
  --export_dir '/exports' \
  --learning_rate 0.0005 --dropout_rate 0.05 \
  --scorer_path 'deepspeech-0.9.3-models.scorer' | tee /tmp/resume.log

if ! grep "Loading best validating checkpoint from" /tmp/resume.log; then
  echo "Did not resume training from checkpoint"
  exit 1
else
  exit 0
fi