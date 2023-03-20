### Spark Jobs
Apply the manifest found in each job's subdirectory
```
$ kubectl apply -f hello/hello.yml
```
This will spawn a `SparkApplication` in the `spark` namespace. 
Once the application has completed, it will need to be deleted manually.