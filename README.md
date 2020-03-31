# GCS Read Performance

The tests were performed using `gsutil perfdiag` configured to test read throughput on parallel read of 50 1000MB files.

```
gsutil perfdiag -n 50 -c 50 -s 1000M -t rthru -o output.json gs://jk-perf-test-bucket 
```

|Machine type|Mean throughput|
|------------|---------------|
|n1-standard-16|~23GiBit/s|


## High perf machine configuration
```
gcloud compute instances create jk-test-instance \
   --custom-cpu 96 \
   --custom-memory 624 \
   --image-project=deeplearning-platform-release \
   --image-family=tf-latest-gpu-gvnic \
   --accelerator type=nvidia-tesla-t4,count=4 \
   --maintenance-policy TERMINATE \
   --metadata="install-nvidia-driver=True"  \
   --boot-disk-size 200GB \
   --scopes=cloud-platform,userinfo-email \
   --zone=us-central1-f
```
