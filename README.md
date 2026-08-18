# s01p03-gh-actions-expressions-contexts-poc

GitHub Actions expressions (`${{ }}`), contexts (`github`, `env`, `runner`, `steps`, `needs`), and built-in functions (`contains()`, `startsWith()`, `format()`, `toJSON()`, `fromJSON()`).

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run tests

```bash
python3 -m pytest tests/ -v
```

## Run the workflow

Push to `main` or open a PR — `.github/workflows/expressions-contexts.yml` runs and prints each context/function's resolved value to the job logs.

See [BLOG.md](./BLOG.md) for a full walkthrough.
