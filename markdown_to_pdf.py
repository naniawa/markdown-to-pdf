import os
import re
import subprocess
#node.js plantuml(javaで代用可) md-to-pdfが必要。

def extract_plantuml_code_from_markdown(input_markdown_path):
    # Markdownファイル読み込み
    with open(input_markdown_path, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    # 正規表現を使用してPlantUMLコードを抽出
    plantuml_matches = re.findall(r"```plantuml(.*?)```", markdown_content, re.DOTALL)

    return plantuml_matches

def generate_diagram_images(plantuml_matches):
    image_paths = []

    for i, plantuml_code in enumerate(plantuml_matches, start=1):
        # PlantUMLを画像に変換
        os.makedirs("images", exist_ok=True)
        with open(f"images/diagram_{i}.puml", "w", encoding="utf-8") as file:
            file.write(plantuml_code)

        #subprocess.run(["plantuml", f"-tpng", f"diagram_{i}.puml"]) #macOS
        subprocess.run(["plantuml", f"-tsvg", f"images/diagram_{i}.puml"]) #macOS
        #subprocess.run(["java","-Dfile.encoding=UTF-8", "-jar", "plantuml.jar","-tsvg", f"images/diagram_{i}.puml"]) #windowsOS

        #image_paths.append(f"diagram_{i}.png")
        image_paths.append(f"images/diagram_{i}.svg")

        # 不要なファイルの削除
        #os.remove(f"diagram_{i}.puml")

    return image_paths

def insert_diagrams_into_markdown(input_markdown_path, image_paths):
    # Markdownファイル読み込み
    with open(input_markdown_path, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    # 画像の挿入
    for i, image_path in enumerate(image_paths):
        markdown_content = re.sub(r'```plantuml(.*?)```', f"![UML Diagram {i + 1}]({image_path})  ", markdown_content, count=1, flags=re.DOTALL)

    return markdown_content

def save_markdown_to_file(markdown_content, output_md_path):
    with open(output_md_path, "w", encoding="utf-8") as file:
        file.write(markdown_content)

def convert_md_to_pdf(input_md_path,):
    try:
        subprocess.run(["md-to-pdf", input_md_path], check=True)
        print("Conversion successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

# 外部で指定されたMarkdownファイルと出力PDFファイルのパス
print("input file(.md)")
input_markdown_path = input()  # ユーザーからの入力を受け取る
#print("output file(.md)")
#output_md_path = input()
output_md_path = "output.md"
#/Users/nishikawashota/Downloads/Markdown/out.md


plantuml_matches = extract_plantuml_code_from_markdown(input_markdown_path)
image_paths = generate_diagram_images(plantuml_matches)
markdown_content = insert_diagrams_into_markdown(input_markdown_path, image_paths)

# 生成されたMarkdownをファイルに保存
save_markdown_to_file(markdown_content, output_md_path)

# 保存したMarkdownをPDFに変換
convert_md_to_pdf(output_md_path)
