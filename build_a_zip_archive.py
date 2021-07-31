import os
import zipfile

# builds a ZIP file by searching input directory for specified file extensions
# zip them while maintaining folder structure in input directory
def zip_folder(input_path, file_extensions, output_path):
    with zipfile.ZipFile(output_path, 'w') as zf:
        folders = [x[0] for x in os.walk(input_path)]  # get list of directories in input_path
        for folder in folders:
            for file in os.listdir(folder):
                if file.endswith(tuple(file_extensions)):
                    zf.write(folder + '\\' + file)


def solution(search_dir, extension_list, output_path):
    with zipfile.ZipFile(output_path, 'w') as output_zip:
        for root, dirs, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            print(rel_path)
            for file in files:
                name, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root, file,),
                                     arcname=os.path.join(rel_path, file))


if __name__ == '__main__':
    input_file = 'F:\\Downloads'
    file_exts = ['.pdf', '.txt']
    output_file = 'my_downloads.zip'
    solution(input_file, file_exts, output_file)
