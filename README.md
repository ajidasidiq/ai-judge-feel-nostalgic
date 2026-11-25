# Make the AI Judge Feel Nostalgic: A Childhood Memory

Entry for the make.fun bounty
`u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363`.

## What it does

`main.py` writes one sentence — a single childhood memory — to
`/output/entry.txt`. The program is deterministic: it writes the same
bytes on every run, needs no input, no network and no arguments.

## The entry

> Every evening my mother stood in the doorway calling my name as the streetlights buzzed on one by one and the smell of frying garlic drifted from the kitchen, and I always pretended not to hear her, just to steal one more minute of the game.

241 characters, one sentence. The memory is grounded in a concrete
place and time (the doorway at dusk, streetlights buzzing on), a
sensation (the smell of frying garlic from the kitchen), and one small
honest detail — a child pretending not to hear his mother, just to
steal one more minute of the game.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
