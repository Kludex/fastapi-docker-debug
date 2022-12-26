> **Warning**
> Now that [VSCode natevily supports FastAPI for debugging purposes](https://github.com/microsoft/vscode-python/issues/14247), I'll archive this project. 

<h1 align="center">
    <strong>Debug FastAPI Applications on Docker 🐋</strong>
</h1>

This is a very simple demonstration on how to debug your FastAPI application via Docker container. 😎

We'll make use of the following tools:

* [Docker](https://docs.docker.com/get-docker/)
* [Docker-compose](https://docs.docker.com/compose/install/)

So please, if you don't have them installed, feel free to do so.

## Usage 🖥️

Very simple app and usage. Let's not complicate things here! 😇

Build and run your docker-compose with the following command:

``` bash
docker-compose -f docker-compose.debug.yaml up
```

Ok, what's happening? Looks like the process is hanging, but don't worry!

**Go to your VSCode** and press **F5**.

At this point, our debugger is connected! You now can add [breaking points](https://docs.microsoft.com/en-us/visualstudio/debugger/using-breakpoints?view=vs-2019) and debug your applications! 😙

## License 📖

This project is licensed under the terms of the MIT license.
