# Stalin

## Code by Ethan Cohen

Annoyed at your code? Send problematic lines to the Gulag with this nifty little package.

## Usage

Start by running `pip install stalin`. Once installed, you can threaten your code by running `python -m stalin <file>`. Lines that throw an exception will be sent straight to the Gulag. However, unlike the real purges, you can always recover any line of code by running `python -m stalin release` to clear out the gulag.

## The Gulag

The gulag is a file called `gulag.ussr`. If you delete this file, you cannot recover any lines currently in there, so meddle with caution!

## The Idea

This is not an original idea. I first heard about the legendary `fuckit.js` several years ago, and then would eventually joke with a coworker that I could probably implement it in Python. Et voila, here it is!
