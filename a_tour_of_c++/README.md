A space to experiment while reading "A Tour of C++" 3rd ed, by the creator of C++, Bjarne Stroustrup

https://www.stroustrup.com/tour3.html

Run the service with interactive shell with:
```docker
docker compose run gcc
```

Using `docker compose up` will cause it to run the background and you will not get the interactive shell.

To add a new project, just follow the existing struture. The `CMakeLists.txt` will will automatically find all subprojects and build the executables.

All executables are runnable from anywhere since the `build.sh` installs then as symlinks in `/usr/local/bin`.