# ARCHWEET

## Description

An ugly script to archive tweet ("du ya archweet ?") responding to a specific query, over past (up to 1500 results) and present (one update every 60 seconds).

## Usage

If you want it to run a long time the most simple is to combine it with `nohup` and `&`:

	nohup python ./archweet.py "an awesome query" &

You'll find the results in a json file in the current working directory named by your query, updated every 60 seconds.

## Dependencies

It uses [urllib3](https://github.com/shazow/urllib3)

	sudo easy_install urllib3