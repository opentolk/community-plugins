<p align="center">
  <img src="https://github.com/opentolk/opentolk/raw/main/Resources/AppIcon.png" width="80" height="80" alt="OpenTolk">
</p>

<h1 align="center">OpenTolk Community Plugins</h1>

<p align="center">
  <strong>A growing collection of voice-powered plugins for <a href="https://github.com/opentolk/opentolk">OpenTolk</a>.</strong><br>
  Browse, install, and share plugins that extend what your voice can do.
</p>

<p align="center">
  <a href="#plugins">Browse Plugins</a> &bull;
  <a href="CONTRIBUTING.md">Submit Yours</a> &bull;
  <a href="https://github.com/opentolk/opentolk/blob/main/PLUGINS.md">Plugin Dev Docs</a> &bull;
  <a href="https://github.com/opentolk/opentolk">OpenTolk App</a>
</p>

---

## How to Install Plugins

### From the App (Easiest)

Open OpenTolk Settings > Plugins > **Browse** tab. Search, click Install. Done.

### Manual Install

Download any `.tolkplugin` file and drop it in:

```
~/.opentolk/plugins/
```

It hot-reloads instantly — no restart needed.

---

## Plugins

### AI & Language

| Plugin | Description | Trigger |
|--------|-------------|---------|
| [Translate](plugins/translate.tolkplugin) | Translate text to any language | "translate ..." |
| [Summarize](plugins/summarize.tolkplugin) | Condense text into key points | "summarize ..." |
| [Explain Like I'm 5](plugins/eli5.tolkplugin) | Simplify complex topics | "explain ..." / "eli5 ..." |
| [Rephrase](plugins/rephrase.tolkplugin) | Rewrite for clarity and tone | "rephrase ..." |
| [Grammar Fix](plugins/grammar-fix.tolkplugin) | Fix grammar and spelling | "fix ..." / "grammar ..." |

### Productivity

| Plugin | Description | Trigger |
|--------|-------------|---------|
| [Define](plugins/define.tolkplugin) | Dictionary definitions | "define ..." |
| [Proofread Pipeline](plugins/proofread-pipeline.tolkplugin) | Fix grammar then rephrase (chained) | "proofread ..." |

### Developer

| Plugin | Description | Trigger |
|--------|-------------|---------|
| [Explain Code](plugins/explain-code.tolkplugin) | Explain code from clipboard | "explain code" |

---

## Creating a Plugin

The simplest plugin is **9 lines of JSON**:

```json
{
  "id": "com.yourname.my-plugin",
  "name": "My Plugin",
  "version": "1.0.0",
  "description": "What it does",
  "trigger": { "type": "keyword", "keywords": ["my trigger"] },
  "execution": { "type": "ai", "system_prompt": "Your instruction to the AI." },
  "output": { "mode": "paste" }
}
```

Save it as `~/.opentolk/plugins/my-plugin.tolkplugin` and it works immediately.

For the full reference covering all trigger types, execution types, tool use, pipelines, streaming, and more — see the **[Plugin Development Guide](https://github.com/opentolk/opentolk/blob/main/PLUGINS.md)**.

---

## Submit Your Plugin

We welcome community contributions! See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the full guide.

Quick version:

1. Fork this repo
2. Add your `.tolkplugin` file to `plugins/`
3. Add it to `plugins.json`
4. Submit a PR

---

## License

All plugins in this repository are MIT licensed unless otherwise specified by the plugin author.
