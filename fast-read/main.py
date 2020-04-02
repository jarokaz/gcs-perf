# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import fire
import logging

from multiprocessing import cpu_count

from download import download_command

def start_download(
    object_path,
    output_file,
    processes=cpu_count(), 
    threads=4,
    io_buffer=128 * 2**10,
    min_slice=64 * 2**20,
    max_slice=2**30,
    slice_size=None,
    transfer_chunk=262144 * 4 * 16):

    download_command(processes, threads,
        io_buffer, min_slice, max_slice,
        slice_size, transfer_chunk,
        object_path, output_file)
    

if __name__ == "__main__":
    
    logging.basicConfig(level=logging.INFO)
    program_root_logger = logging.getLogger(__name__)
    program_root_logger.setLevel(logging.DEBUG)
    fire.Fire(start_download)