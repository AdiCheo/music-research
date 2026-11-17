# Publishing the vault

Use this folder directly in Obsidian. Standard relative Markdown links work there and are straightforward to move to a static publisher. [Obsidian links](https://help.obsidian.md/links)

| Route | Why try it | What to verify |
| --- | --- | --- |
| Quartz | Open-source static publisher designed for Obsidian-style content. Its docs cover full-text search, backlinks and hosting. Start with a separate Quartz checkout and direct it at a staging directory of Markdown. | Test internal links and paths in the rendered site, especially if deployed under a repository subpath. [Quartz](https://quartz.jzhao.xyz/) · [Hosting guide](https://quartz.jzhao.xyz/hosting) |
| Obsidian Publish | Managed option for publishing from Obsidian with explicit note selection. | Review which pages, backlinks and assets are selected. [Obsidian Publish](https://obsidian.md/publish) |

## First preview

1. Start from a clean commit and review the staged list of public notes and assets. Keep private practice notes and imported files outside the publish directory. Review the source and permission for any recording, stem, lyric, chart or lesson excerpt before including it.
2. For Quartz, copy the approved notes to its content directory with their paths intact. `index.md` is the home page. Use the build and preview steps for the Quartz version installed. [Quartz setup](https://quartz.jzhao.xyz/)
3. Open the home page, tool catalog, worked song, skill tree and app brief in the preview. Check navigation, table readability on a phone, and that search covers only the intended pages. Keep the [app integration](projects/vocal-training.md) as a link until its runtime and microphone use have been tested on an HTTPS deployment.
4. Choose the public host and visibility after checking the preview. [Quartz hosting](https://quartz.jzhao.xyz/hosting)

This repository contains the Markdown source. A static site build, deployment and remote Git repository are pending.
