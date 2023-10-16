# Using Docker to run zsdk
If you don't want to set up a Python environment and worry about installing all the required packages you can build 
a Docker container that will contain all of this for you.

You have the option of building and running a Docker container that contains the version of [zsdk that is hosted in this 
repo/branch](#Using-zsdk-hosted-in-this-git-repo), or using the [zsdk hosted on pypi](#Using-zsdk-posted-on-PyPi).

## Using zsdk posted on PyPi
The benefits of using the version of zsdk that is posted on pypi is that you are running the latest, but most stable,
version of zsdk.  **This is the recommended option if using in a production environment.**

This method uses a pre-built Docker image that is hosted on DockerHub.  Just reference **dmickels/zsdk:latest** to 
get the most recent version of the image.  We will do our best to maintain a version of this image for each 
version of zsdk released to PyPi.

Using this method in a Dockerfile will mean having a line something like **FROM dmickels/zsdk:latest** in your file.
Using this method in a docker-compose.yml file will mean having a line something like **image:dmickels/zsdk:latest** in your service for this container.

## Using zsdk hosted in this git repo
The benefits of using the version of zsdk that is hosted in this git repo is that you can run the bleeding edge 
version of zsdk.  Your options are to use the [docker](#Using-the-docker-command-method) or the [docker-compose](#Using-the-docker-compose-command-method) commands.

### Using the docker command method
Personally I don't like this method but many projects provide it.  So, here you go!

1. In the top level directory of where you cloned this repo run: `docker build -t zsdk .`
    - **-t zsdk** Gives this Docker image a name of zsdk.
    - **.** Is the build environment location.
2. Change directory to where your code is located.
3. To run the image: `docker run --rm -v $(pwd):/app zsdk filename.py` where **filename.py** is the filename of your Python script.
    - **--rm** Removes the container once completed.  (Optional, but this is desired/expected behaviour for this image.)
    - **--mount $(pwd):/app** Mounts the local directory as /app in the container.  This is required.
    - **zsdk** Is the name of the built image from the `docker build` command.
    - **filename.py** Replace this with whatever your code's filename is.
4. We've provided a test Python file, **docker-test-script.py** that will import zsdk but not do anything with it.  
   The script will then print **Hello World!** to the console.  The point is to run the Docker container and ensure 
   zsdk is importing correctly.

### Using the docker-compose command method
I much prefer using `docker-compose` (or `docker compose` in more recent releases).

1. In the top level directory of where you cloned this repo run: `docker-compose build`  This will build the 
   Docker image.
2. Different from using the `docker` command, `docker-compose` requires the container to be started in the same 
   directory as the docker-compos.yml file.  So, you may need to copy your code into this repo's directory structure,
   or copy the docker-compose.yml file to where your code resides.  (Alternatively, copy the contents of the 
   docker-compose.yml **service** section to your own docker-compose.yml file as you might be including this 
   container in a larger project.  Explaining this is beyond the scope of this document.) 
3. Run `docker-compose run --rm zsdk filename.py` to execute this container on your filename.py code.


## Notes for building Docker image and posting to DockerHub
Reminder notes for creating a docker image to be posted on DockerHub.

1. Build an image using the correct Dockerfile (probably Dockerfile-pypi): `docker build -t zsdk -f Dockerfile-dockerhub .`
2. Test this image: `docker run --rm -v $(pwd):/app zsdk docker-test-script.py`
3. Log into DockerHub prior to uploading working image(s): `docker login`
4. Update/Create a **latest** tagged image in DockerHub:
    1. `docker tag zsdk:latest dmickels/zsdk:latest`
    2. `docker push dmickels/zsdk:latest`
5. Update/Create an image linked to a different tag.  I suggest using the zsdk version number as the tag:
    1. `docker tag zsdk:latest dmickels/zsdk:<version>`
    2. `docker push dmickels/zsdk:<version>`
