import os

def combine_md_files(directory_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        for filename in os.listdir(directory_path):
            if filename.endswith(".md"):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, 'r', encoding='utf-8') as input_file:
                    output.write(input_file.read())
                    output.write('\n\n')  # それぞれのファイルの終わりに空行を挿入

if __name__ == "__main__":
    print("write input directory")
    input_directory = input() # 対 象のディレクトリのパスを指定
    print("write output directory and file")
    output_file_path = input()  # 結合後のファイルのパスを指定
    combine_md_files(input_directory, output_file_path)
