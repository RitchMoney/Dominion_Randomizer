# Ingest Tool
This module is the ingest tool for Dominion Data. It pulls data from publically-available APIs related to Dominion Sets (i.e expansions) and serializes the information for local storage. A separate pickle is created for each relevant set, including metadata and all available cards.

NOTE: only use the relevant APIs with permission.

## Using the Ingest Tool
run the following from the root of the project: ```python3 -m ingest.ingest_tool```
