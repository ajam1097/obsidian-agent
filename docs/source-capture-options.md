# Source Capture Options

`source` pages are captured material waiting to be processed into durable knowledge. The capture tool matters less than the contract: preserve the original, add enough metadata to route it, and process it later with review.

## Options

| Option | Good For | Notes |
| --- | --- | --- |
| Readwise Reader + Readwise Official Obsidian plugin | Highlights, reading queues, recurring sync | Readwise can sync new highlights to Obsidian, append new highlights to existing pages, customize export templates, and export Reader full text for Library documents. |
| Obsidian Web Clipper | One-off web pages, selected highlights, browser capture | Obsidian Web Clipper saves web content locally to a vault and supports templates, variables, filters, highlighting, and a reader view. |
| Manual source note | Conversations, offline notes, unusual media | Use the `source` template/shape and paste enough context to process later. |
| Read-it-later export | Tools such as Pocket/Instapaper-style queues | Keep these as ingestion inputs; normalize into `source` pages before synthesis. |
| Email/newsletter forwarding | Receipts, newsletters, recurring inbound material | Useful when the source arrives outside the browser; make sure private headers and addresses are not published. |

## Capture Contract

Every source capture should answer:

- What is it?
- Where did it come from?
- Has it been processed?
- What should remain immutable?

The sample schema keeps this small:

```yaml
type: source
source_type: article
source_url: "https://example.com/article"
processing_status: unprocessed
created: 2026-01-11
```

## Processing Pattern

1. Capture the source without overthinking it.
2. Keep source bodies stable.
3. Extract durable takeaways into concept pages.
4. Link concepts back to the source.
5. Mark the source `processed` or `skipped`.

## References

- [Readwise to Obsidian export integration](https://docs.readwise.io/readwise/docs/exporting-highlights/obsidian)
- [Obsidian Web Clipper](https://obsidian.md/help/web-clipper)

