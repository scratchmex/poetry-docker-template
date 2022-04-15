import tomli
import jinja2


# from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("."),
    autoescape=jinja2.select_autoescape(),
    trim_blocks=True,
)

with open("config.toml", "r") as f:
    render_vars = tomli.load(f)

out = env.get_template("dockerfile.jinja").render(render_vars)

print(out)
