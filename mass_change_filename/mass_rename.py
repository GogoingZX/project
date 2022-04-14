import sys
import os
import re
import tqdm

def get_all_files(
    folder_path,
    file_type="all",
    show_info=True
):
    filepath_list = []
    
    if file_type == "all":
        for filename in os.listdir(folder_path):
            if filename.startswith(".") is False:
                filepath_list.append(os.path.join(folder_path, filename))
    else:
        for filename in os.listdir(folder_path):
            if filename.startswith(".") is False and filename.split(".")[-1] == file_type:
                filepath_list.append(os.path.join(folder_path, filename))

    filepath_list = list(set(filepath_list))

    if show_info == True:
        first_line = "{divider} Files Info {divider}".format(divider="="*35)
        msg = """
        \r{first_line}
        \r* Folder Path: {folder_path}
        \r* File Type: {file_type}
        \r* Total Files: {file_cnt}
        \r{divider_end}
        """.format(
            first_line = first_line,
            folder_path = folder_path,
            file_type = file_type,
            file_cnt = len(filepath_list),
            divider_end = "="*len(first_line)
        )
        print(msg)
    else:
        pass
    
    return filepath_list


# mass rename
def main():
    target_folder = input("Please Enter The Folder Path: ")
    file_type = input("Please Enter The File Type: ")
    filepaths = get_all_files(
        folder_path=target_folder,
        file_type=file_type
    )
    
    filepaths_failed = []
    for filepath in tqdm.tqdm(filepaths):
        try:
            filename_old = os.path.basename(filepath)
            keyword = re.search("E\d+", filename_old).group()
            filename_new = "{0}.{1}".format(keyword, file_type)
            os.rename(filepath, os.path.join(target_folder, filename_new))
        except:
            filepaths_failed.append(filepath)
    
    # print(len(filepaths_failed))
    # print(filepaths_failed)

if __name__ == "__main__":
    main()