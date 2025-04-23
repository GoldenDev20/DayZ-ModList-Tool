import os
from utils.file_handler import (
    get_mod_names,
    load_previous_mods_xlsx,
    write_mod_list_to_excel,
    write_mod_list_to_html,
    write_mod_list_to_markdown,
    load_config
)

def main():
    # Load config from JSON file
    config = load_config("config.json")

    # Load mods from folder
    mod_names = get_mod_names(config["mods_folder"])

    # Load previous mod list (optional)
    previous_mods = load_previous_mods_xlsx(config["output_folder"])

    # Export to Excel if enabled
    if config["export_formats"].get("excel", False):
        write_mod_list_to_excel(
            mod_names,
            previous_mods,
            os.path.join(config["output_folder"], "mod_list.xlsx"),
            config["columns"],  # Pass the columns dictionary
            config.get("use_color", False)
        )

    # Export to HTML if enabled
    if config["export_formats"].get("html", False):
        write_mod_list_to_html(
            mod_names,
            previous_mods,
            os.path.join(config["output_folder"], "mod_list.html"),
            config["columns"]
        )

    # Export to Markdown if enabled
    if config["export_formats"].get("markdown", False):
        write_mod_list_to_markdown(
            mod_names,
            previous_mods,
            os.path.join(config["output_folder"], "mod_list.md"),
            config["columns"]
        )

if __name__ == "__main__":
    main()
