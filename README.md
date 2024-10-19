# 📦 pixi-site-packages

A tool to extract PyPI requirements from a `pixi.lock` file.

## 🔧 Installation

To install this tool, use the following command:

```bash
pip install .
```

## 📝 Usage

This tool allows you to extract the PyPI requirements from a `pixi.lock` file and write them to a `requirements.txt` file or print them to stdout.

### 🚀 Command-Line Interface (CLI)

To use the tool from the command line, run the following:

```bash
pixi-requirements /path/to/pixi.lock
```

This will print the extracted PyPI requirements to the console. If you want to write the requirements to a file, use the `--output-path` option:

```bash
pixi-requirements /path/to/pixi.lock --output-path requirements.txt
```

### 🛠️ Example Usage with Bash Loop

You can use the `pixi-requirements` command in combination with a `for` loop in bash to install each requirement into a target `site-packages` directory. Here is an example:

```bash
for r in $(pixi run pixi-requirements /path/to/pixi.lock --platform linux-64) ; do
  echo "Installing $r..."
  pip install --upgrade --no-deps -t site-packages $r
done
```

In this example:

- The `pixi-requirements` command extracts the list of PyPI packages.
- Each requirement is installed into the `site-packages` directory using `pip install --upgrade --no-deps -t site-packages $r`.

### 💡 Optional Arguments

- `--platform`: Specify the platform (default: `linux-64`).
- `--environments`: Comma-separated list of environments to include (default: `default`).

### 📋 Example

To extract requirements for a specific platform and save them to `requirements.txt`:

```bash
pixi-requirements /path/to/pixi.lock --platform linux-64 --output-path requirements.txt
```

## ⚙️ Development

To format the code, use `black` and `isort`:

```bash
black src tests
isort src tests
```
