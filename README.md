## Run container
```shell script
cd /project/root/dir/
docker run -p 8080:8080 --mount type=bind,src=`pwd`/db_data,destination=/app/db_data forkcs/mycode:0.1
```
Now open [this link](http://127.0.0.1:8080/) in your browser.