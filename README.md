# Mod List Exporter 🎮

A simple tool for exporting a list of mods for DayZ or similar modded games. This project scans the "Mods" folder, compares it with a previous mod list (if available), and generates a summary of the current state of the mods (added, removed, unchanged). It can export this data to several formats, including **Excel**, **HTML**, **Markdown**, and more. 📊

---

## Features 🌟

- **Mod Folder Scanning:** 🗂️ Scans the folder containing your mod files and extracts their names.
- **Mod Comparison:** 🔍 Compares the current mod list with a previous version and shows the changes (added, removed, unchanged).
- **Export Options:** 🖥️ Exports the mod list to various formats (**Excel**, **HTML**, **Markdown**).
- **Configurable Output:** ⚙️ Customize the output by enabling/disabling columns like `mod_name`, `mod_version`, and `status`. Choose whether or not to color-code the results. 🎨
- **Simple Setup:** 🛠️ The tool works with just a few configuration changes and can be run from the command line using a batch file. 🏃‍♂️

---

## Installation 🛠️

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mod-list-exporter.git
cd mod-list-exporter
```

### 2. Install Dependencies 📦

Make sure you have **Python 3.x** installed. You can install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install the necessary libraries, including:

- `openpyxl` for **Excel** file handling 📑
- `jinja2` for **HTML** and **Markdown** templating 📝

### 3. Configuration ⚙️

Create or edit the `config.json` file to specify the mod folder location, output folder, and the export formats you want. Example:

```json
{
  "mods_folder": "./Mods",
  "output_folder": "./output",
  "export_formats": {
    "excel": true,
    "html": true,
    "markdown": true
  },
  "columns": {
    "mod_name": true,
    "mod_version": false,
    "status": true
  },
  "sort_order": "asc",
  "use_color": true
}
```

- `mods_folder`: 🗂️ Path to your mods folder (where your mods are stored).
- `output_folder`: 📂 Path where the exported files will be saved.
- `export_formats`: 📄 Choose the formats you want to export to (**Excel**, **HTML**, **Markdown**).
- `columns`: 🔢 Toggle the columns to be included in the export (`mod_name`, `mod_version`, `status`).
- `sort_order`: 🔀 Choose between `"asc"` or `"desc"` to sort the mod names.
- `use_color`: 🎨 Enable color-coding for the export results.

### 4. Run the Tool 🚀

Once the configuration is set up, you can run the tool via the command line.

#### Using the Batch File (Windows)

Simply double-click `run.bat` to execute the script. This will process the mods, compare with the previous list (if available), and generate the output files. 🖱️

#### Running Manually (Python)

If you prefer to run it manually, use this command:

```bash
python main.py
```

---

## Exported Files 📑

Depending on your configuration, the following files will be generated in the `output` folder:

- **Excel**: A `.xlsx` file containing the list of mods, their status, and other specified columns. 📊
- **HTML**: A well-formatted **HTML** file for easy viewing in the browser. 🌐
- **Markdown**: A **Markdown** file suitable for documentation or sharing. 📝

---

## License 🔑

This project is licensed under the [Apache 2.0 License](LICENSE) - see the LICENSE file for details. 📜

---

## Contributing 🤝

Contributions are welcome! If you want to contribute to this project, feel free to fork the repository and create a pull request. 🚀

### How to Contribute:

1. Fork the repository. 🍴
2. Create a new branch for your changes. 🌱
3. Commit your changes and push them to your fork. 🔄
4. Open a pull request to the main repository. 📨

---

## Contact 📬

If you have any questions or need help with the tool, feel free to open an issue or contact the project maintainer. 🛠️
