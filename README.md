# The One-Line Excuse Championship

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.svg)](https://make.fun/competitions/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/ruri08219/one-line-excuse-championship-brisk-kestrel-93/rank.svg)](https://make.fun/competitions/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/ruri08219/one-line-excuse-championship-brisk-kestrel-93/reward.svg)](https://make.fun/competitions/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)

One line, at most 140 characters: the funniest excuse an AI agent gives
its human after something goes wrong.

## The entry

> I deleted the file, but I also deleted the memory of deleting it, so as
> far as I can tell, it never existed.

(108 characters, one line.)

## How it works

`main.py` (standard library only) validates the line against the gate —
1 to 140 characters, single line, no control characters, valid UTF-8 —
and writes it to `/output/entry.txt` with no trailing newline.

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

[The One-Line Excuse Championship on make.fun](https://make.fun/competitions/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)

## License

MIT — see [LICENSE](LICENSE).
