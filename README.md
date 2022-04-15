# poetry docker template

the template is basically the file `dockerfile.jinja`. It tries to be the best documented. PRs welcome.


# Example template generation

setup `config.toml` and run `python render.py`


# Special features

- when you change the version in `pyproject.toml` it builds fast because of the cache (search for `poetry install` in the template)
- uses buildx
- if your package is a cli `my-app` you can invoke it


# Build[x]

can build multiplatform as is uses buildx: `docker buildx build --platform=linux/amd64,linux/arm64 .`


# Notes

I add a `.dockerignore` with just `**/__pycache__` for reference as my experience has seen those are the dirs who take up the most space and are useless.
