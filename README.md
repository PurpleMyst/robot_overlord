# robot_overlord

robot_overlord is a Python service to manage programs such as bots, scrapers,
etcetera...

## Installation

### Requirements

* Ubuntu (for now)
* Python 3 and up

## Usage

Create a file named `your_program_name.yaml`, and fill it out following this
template:

```yaml
---

# the name of your program. used for logging.
name: your_program_name

# required interpreters/compilers your program needs
requires:
    # the currently supported requirements are:
    - python2
    - python3

# where to find your porgram
location:
    # the type of location to find your program.
    # currently only local is supported
    type: local
    directory: directory_of_your_program

# any shell commands that need to be run prior to running your program.
setup:
    - "echo foobar"

# what shell command to run to start your program. make sure that this blocks
# until your program is finished running.
start: "interpreter foo.bar"
```

After that, run at your shell the command:

```shell
$ python3 -m robot_overlord your_program_name.yaml
```

And your program will start being controlled by robot_overlord.

## Development

Clone the project and hack away!

## Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
