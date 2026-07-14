# AI Agent CLI

This project is a small CLI agent that sends a user prompt to an LLM, lets the model request local tools, and prints either tool results or a final response.

## What It Does

- Lists files and directories inside the working project folder.
- Reads file contents.
- Runs Python files with optional command-line arguments.
- Writes or overwrites files.
- Loops through model/tool interactions until the model produces a final answer.

## Project Layout

```text
.
├── main.py              # CLI entrypoint
├── call_function.py     # Tool registry and dispatcher
├── prompt.py            # System prompt for the agent
├── functions/           # Local tool implementations and JSON schemas
├── calculator/          # Example working directory used by the tools
├── test_*.py            # Tool-specific tests
└── pyproject.toml       # Project metadata and dependencies
```

## Requirements

- Python 3.14+
- `uv`
- An `OPENROUTER_API_KEY` value in your environment

## Setup

1. Create a `.env` file in the project root if you want to load the API key automatically.
2. Add your key:

```bash
OPENROUTER_API_KEY=your_key_here
```

3. Install dependencies and create the environment with `uv` if needed:

```bash
uv sync
```

## Run The CLI

Ask the agent a question or request a tool action:

```bash
uv run main.py "what files are in the root?"
uv run main.py "get the contents of lorem.txt"
uv run main.py "run tests.py" --verbose
uv run main.py "create a new README.md file with the contents '# calculator'" --verbose
```

## Verbose Mode

Use `--verbose` to see the prompt, token counts, tool calls, and tool outputs.

```bash
uv run main.py "how does the calculator render results to the console?" --verbose
```

## Tooling Notes

The model can request one of four tools. The dispatcher in `call_function.py` maps the request to the actual Python function and injects `working_directory="./calculator"` automatically.

If the model keeps calling tools and never produces a final answer, the CLI stops after 20 iterations and exits with an error.

## Tests

The repository includes tool-level tests and example calculator tests.

```bash
uv run main.py "run tests.py" --verbose
```

## Common Outputs

- `get_files_info` returns a directory listing.
- `get_file_content` returns file text, truncated when needed.
- `run_python_file` returns stdout/stderr and exit status details.
- `write_file` returns a success message after writing content.

## Next Steps

If you want to keep building this project, the usual next steps are to:

1. Add support for executing the tool calls returned by the model in a second request cycle.
2. Expand the README with screenshots or example transcripts.
3. Add integration tests for the full model/tool loop.
