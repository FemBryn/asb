import converter

# optional output_dir argument specifies the output location for the file
# optional romfs_path argument specifies the romfs location for zs compression/decompression
# optional compress_file argument specifies whether or not to compress the file with zstd

# optional baev_path argument loads the corresponding BAEV file with the ASB    
Path = "C:\\Users\\brend\\OneDrive\\Documents\\GitHub\\asb\\"
converter.json_to_asb(Path + "SplPlayer.root.json")
converter.json_to_asb(Path + "WeaponBrushHeavy.root.json")
converter.json_to_asb(Path + "WeaponRollerNormal.root.json")