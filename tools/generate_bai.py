#!/usr/bin/env python

import os
import sys
import json
import time
from random import randint
from utils import get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])
cwd = os.getcwd()

"""
    input:
      bam_file:
        type: string
        is_file: true
      ega_file_id:
        type: string
      file_name:
        type: string
      file_size:
        type: integer
      file_md5sum:
        type: string
      bundle_id:
        type: string
"""
bam_file = task_dict.get('input').get('bam_file')
ega_file_id = task_dict.get('input').get('ega_file_id')
file_name = task_dict.get('input').get('file_name')
file_size = task_dict.get('input').get('file_size')
file_md5sum = task_dict.get('input').get('file_md5sum')
bundle_id = task_dict.get('input').get('bundle_id')

task_start = int(time.time())

# do the real work here
time.sleep(randint(1,10))


# complete the task

task_stop = int(time.time())
idx_file_name = '%s.bai' % file_name

# TODO generate object_id by calling ICGC ID service
idx_object_id = None
idx_file_size = None
idx_file_md5sum = None
"""
    output:
      # this is the object_id obtained from ICGC service using bundle_id and ega_metadata_file_name as input
      idx_object_id:
        type: string
      idx_file:
        type: string
        is_file: true
      idx_file_name:
        type: string
      idx_file_size:
        type: string
      idx_file_md5sum:
        type: string
"""


output_json = {
    'idx_file': os.path.join(cwd, idx_file_name),
    'idx_file_name': idx_file_name,
    'idx_object_id': idx_object_id,
    'idx_file_size': idx_file_size,
    'idx_file_md5sum': idx_file_md5sum,

    'runtime': {
        'task_start': task_start,
        'task_stop': task_stop
    }
}

save_output_json(output_json)