```

gcloud beta compute instances create instance-name \
   --custom-cpu 96 \
   --custom-memory 624 \
   --image-project=gvnic-vm-image-prod \
   --image-family=debian-9-gvnic \
   --accelerator type=nvidia-tesla-t4,count=4 \
   --maintenance-policy TERMINATE \
   --metadata="install-nvidia-driver=True"  \
   --boot-disk-size 200GB \
   --scopes=cloud-platform,userinfo-email \
   --zone=us-central1-f
   
```
