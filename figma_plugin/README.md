# Figma to PyX (Zen Mode) Plugin

This Figma plugin allows you to convert Figma designs directly into `PyX` framework code, adhering to the Zen Mode philosophy.

## Installation

1. Open Figma Desktop App or Browser.
2. Go to **Main Menu** > **Plugins** > **Development** > **Import plugin from manifest...**.
3. Navigate to this folder (`/Users/aaa/Documents/Developer/Framework/PyX/figma_plugin`).
4. Select `manifest.json`.

## Usage

1. Select a Frame, Group, or Component in your Figma file.
2. Right-click > **Plugins** > **Development** > **Figma to PyX**.
3. The plugin window will open. Click **Generate PyX Code**.
4. The generated Python code will appear in the text area.
5. Copy and paste it into your PyX application.

## Project Structure

- `manifest.json`: Configuration file for the Figma plugin.
- `code.js`: Compiled backend logic.
- `src/code.ts`: Source code for the plugin backend (accesses Figma document).
- `src/ui.html`: The user interface of the plugin (contains the Code Generation logic).

## Customization & AI

Currently, the plugin uses a heuristic rule-based generator in `src/ui.html`. 
To use an **AI MCP** or external LLM:
1. Edit `src/ui.html`.
2. Modify the `generatePyX` function to send the JSON data to your AI endpoint.
3. Parse the response and display the code.

## Build

If you modify `src/code.ts`, run:
```bash
npx tsc
```
to regenerate `code.js`.
