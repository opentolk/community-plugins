# Contributing to OpenTolk Community Plugins

Thanks for building a plugin! Here's how to get it listed in the official directory.

## Submitting a Plugin

### 1. Create Your Plugin

Follow the [Plugin Development Guide](https://github.com/opentolk/opentolk/blob/main/PLUGINS.md) to build your plugin. Test it locally by dropping it in `~/.opentolk/plugins/`.

### 2. Fork & Add

1. Fork this repository
2. Add your `.tolkplugin` file (or directory) to the `plugins/` folder
3. Add an entry to `plugins.json` (see format below)

### 3. Update `plugins.json`

Add your plugin to the `plugins` array:

```json
{
  "id": "com.yourname.your-plugin",
  "name": "Your Plugin Name",
  "version": "1.0.0",
  "description": "A clear, one-line description of what it does",
  "author": "Your Name",
  "categories": ["ai"],
  "url": "https://raw.githubusercontent.com/opentolk/community-plugins/main/plugins/your-plugin.tolkplugin",
  "homepage": "https://github.com/yourname/your-plugin"
}
```

**Fields:**

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Unique reverse-DNS ID (e.g., `com.yourname.plugin-name`) |
| `name` | Yes | Display name |
| `version` | Yes | Semver version |
| `description` | Yes | One-line description |
| `author` | Yes | Your name or handle |
| `categories` | No | Array of: `ai`, `translation`, `productivity`, `developer`, `writing` |
| `url` | Yes | Raw GitHub URL to the plugin file |
| `homepage` | No | Link to docs, repo, or website |
| `featured` | No | Set by maintainers only |

### 4. Submit a PR

Open a pull request with:
- A brief description of what the plugin does
- Confirmation that you've tested it locally
- The trigger words/patterns so reviewers can test it

## Plugin Guidelines

### Do

- Use a unique, descriptive `id` (reverse-DNS: `com.yourname.plugin-name`)
- Write a clear `description` — this shows in the Browse tab
- Test your plugin locally before submitting
- Keep AI system prompts focused and concise
- Include `categories` so users can discover your plugin

### Don't

- Don't include API keys, tokens, or secrets in the plugin file
- Don't use `catch_all` triggers (too broad for a community plugin)
- Don't make HTTP calls to untrusted or personal servers
- Don't include scripts that modify system files or require elevated permissions

### Plugin ID Conventions

```
com.yourname.plugin-name     # Personal plugins
org.orgname.plugin-name      # Organization plugins
```

Don't use `com.opentolk.*` — that's reserved for official plugins.

## Review Process

1. You submit a PR
2. A maintainer reviews the plugin manifest and any scripts
3. We test the plugin locally
4. If approved, we merge and it appears in the Browse tab

Reviews typically take 1-3 days. We may request changes if:
- The plugin has overly broad triggers that conflict with others
- Scripts make unexpected system calls
- The description is unclear

## Updating Your Plugin

To update an existing plugin:

1. Update the `.tolkplugin` file in `plugins/`
2. Bump the `version` in both the plugin file and `plugins.json`
3. Submit a PR

Users with the plugin installed will see the update in the Updates tab.

## Need Help?

- [Plugin Development Guide](https://github.com/opentolk/opentolk/blob/main/PLUGINS.md) — full reference
- [OpenTolk Issues](https://github.com/opentolk/opentolk/issues) — bug reports and feature requests
- [Discussions](https://github.com/opentolk/opentolk/discussions) — questions and ideas
