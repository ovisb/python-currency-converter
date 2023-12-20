# EDU project

## Project

This is _Currency converter_ project that is part of Hyperskill platform from Jetbrains Academy.

'Python Core' track

## Technologies and tools used

- Python 3.12
- pytest
- mypy
- isort
- black
- flake8
- make

## Project description

This is a simple currency calculator which uses https://www.floatrates.com/ for the currency information.

Program also uses simple caching, where it remembers the currency information after it's been fetched at least once.

The initial caching has the information pre-set for USD and EUR.

How to use:
 - first: input your current currency
 - second: input the currency which you want to convert amount to
 - third: input enter amount of money

The first input will be remembered until the program exits.

You can check your initial currency across many other currencies

To exit program input empty space

### Examples:
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

```sh
> USD
> EUR
> 20
Checking the cache...
Oh! It is in the cache!
You received 18.24 EUR.
> NOK
> 45
Checking the cache...
Sorry, but it is not in the cache!
You received 463.84 NOK.
> SEK
> 75
Checking the cache...
Sorry, but it is not in the cache!
You received 763.16 SEK.
> NOK
> 55
Checking the cache...
Oh! It is in the cache!
You received 566.91 NOK.
> ISK
> 91
Checking the cache...
Sorry, but it is not in the cache!
You received 11708.38 ISK.
```
 
#### Install steps

Install everything (main + dev packages except optional groups)

```sh
peotry install
```

Install main packages only

```sh
peotry install --only main

```

If you need pre-commit

```sh
poetry install --with commit
```

If you decided to install pre-commit you can install .pre-commit files in your repo

```sh
peotry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

If the files are git staged, you can trigger pre-commit manually

```sh
poetry run pre-commit run --all-files
poetry run pre-commit run --hook-stage push -v
```

#### Makefile

Added 'Makefile' to make it easy to validate files

Check bellow command on usage

```sh
make help
```
