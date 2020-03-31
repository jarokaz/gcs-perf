# GCS Read Performance

The tests were performed using `gsutil perfdiag` configured to test read throughput on parallel read of 50 1000MB files.

```
gsutil perfdiag -n 50 -c 50 -s 1000M -t rthru -o output.json gs://jk-perf-test-bucket 
```

|Machine type|Mean throughput|
|------------|---------------|
|n1-standard-16|~23GiBit/s|
