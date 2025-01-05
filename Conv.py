import converter

# optional output_dir argument specifies the output location for the file
# optional romfs_path argument specifies the romfs location for zs compression/decompression
# optional compress_file argument specifies whether or not to compress the file with zstd

# optional baev_path argument loads the corresponding BAEV file with the ASB    
converter.asb_to_json("C:\\Users\\brend\\OneDrive\\Documents\\GitHub\\asb\\WeaponRollerNormal.root.asb")
converter.json_to_asb("C:\\Users\\brend\\OneDrive\\Documents\\GitHub\\asb\\WeaponRollerNormal.root.json")