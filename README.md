# carsguide_harvest


## Preparation
 
### Navigate to the folder

```cd ./stevejbickley/carsguide_harvest```

OR

```cd ./carsguide_harvest```

### Clone the project and run the following commands:

```poetry env use path_to_pyevn_python_version```

If you are not using pyenv, just replace the above command with:

```poetry env use path_to_python_interpreter```

Activate the virtual environment if needed:

```source ./carsguide_harvest/.venv/bin/activate```

If using windows - to activate environment, run the following:
```cd ./carsguide_harvest```
```poetry shell```
```cd ../ ```

### Next, run the following to update poetry and install ffmpeg (if required):

```poetry update```

Macos
```brew install ffmpeg```

Linux
```apt install ffmpeg```

Running Python and Scripts:

```poetry run python script.py```

Note: ffmpeg is open-source suite of libraries and programs for handling video, audio, and other multimedia files and streams

## Creating your own poetry environment

### To create new poetry project (if required):

```poetry new carsguide_harvest```


### Initialize the existing directory (if required):

```cd carsguide_harvest``` 

followed by:

```poetry init```


### To add a new package to your project, use:

```poetry add package-name```
