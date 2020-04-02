```
python main.py gs://jk-perf-test/testimage1 /dev/null \
--threads 1 \
--processes 1 \
--max_slice $((262144 * 4 * 1024)) \
--transfer_chunk  $((262144 * 4 * 16))
```
