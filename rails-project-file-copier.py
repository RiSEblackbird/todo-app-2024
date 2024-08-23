'''
LLMに状況を把握させるためにファイルのツリー構造の作成と、
相談に必要なファイル一式をまとめてコピーして準備するためのスクリプト
'''

import os
import shutil

def run_custom_tree_command(project_root, output_file):
    """
    カスタマイズされたツリーコマンドを実行し、結果をファイルに保存します。
    バックエンドとフロントエンドの構造を分けて表示します。
    """
    important_paths = [
        "backend", "frontend", "frontend/src", "frontend/src/store", ".gitattributes", ".gitignore",
        "docker-compose.yml", "README.md", ".github/workflows"
    ]

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"プロジェクトルート: {project_root}\n")
        f.write("プロジェクト構造:\n")
        for path in important_paths:
            full_path = os.path.join(project_root, path)
            if os.path.exists(full_path):
                if os.path.isdir(full_path):
                    f.write(f"  {path}/\n")
                    for item in os.listdir(full_path):
                        f.write(f"    - {item}\n")
                else:
                    f.write(f"  {path}\n")
    
    print(f"カスタマイズされたツリー構造が {output_file} に保存されました")

def copy_files(project_root, dest_folder, files_to_copy, tree_output_file):
    """
    指定されたファイルをプロジェクトルートから目的のフォルダにコピーします。
    """
    copied_files = []
    for file in files_to_copy:
        src_path = os.path.join(project_root, file)
        if os.path.exists(src_path):
            # Dockerfileはファイル名で区別してコピー保存する
            if "Dockerfile" in src_path:
                if "backend" in src_path:
                    file = file.replace("Dockerfile", "(backend)Dockerfile")
                    dest_path = os.path.join(dest_folder, os.path.basename(file))
                elif "frontend" in src_path:
                    file = file.replace("Dockerfile", "(frontend)Dockerfile")
                    dest_path = os.path.join(dest_folder, os.path.basename(file))
                else:
                    file = file.replace("Dockerfile", "(root)Dockerfile")
                    dest_path = os.path.join(dest_folder, os.path.basename(file))
            else:
                dest_path = os.path.join(dest_folder, os.path.basename(file))

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(src_path, dest_path)
            copied_files.append(file)
            print(f"{file} を {dest_folder} にコピーしました")
        else:
            print(f"ファイルが見つかりません: {src_path}")
    
    dest_path = os.path.join(dest_folder, os.path.basename(tree_output_file))
    shutil.copy2(tree_output_file, dest_path)
    
    if not copied_files:
        print("コピーされたファイルはありません。")
    else:
        print(f"コピーされたファイル: {', '.join(copied_files)}")

def main():
    project_root = os.getcwd()
    base_dest_folder = os.path.expanduser("~/Desktop/share_files")
    
    os.makedirs(base_dest_folder, exist_ok=True)
    
    tree_output_file = os.path.join(base_dest_folder, "project_structure.txt")
    run_custom_tree_command(project_root, tree_output_file)
    
    # 通常のファイル
    normal_files = [
        "docker-compose.yml",
        "README.md",
        "backend/Gemfile",
        "backend/Dockerfile",
        "frontend/Dockerfile",
        "backend/config/routes.rb",
        "backend/config/database.yml",
        "frontend/package.json",
        "backend/erd.pdf",
        "backend/db/schema.rb"
    ]
    normal_dest = os.path.join(base_dest_folder, "normal")
    copy_files(project_root, normal_dest, normal_files, tree_output_file)

    # フロントエンドのファイル
    frontend_files = [
        "frontend/package.json",
        "frontend/src/App.js",
        "frontend/src/index.js",
        "frontend/src/styles/App.css",
        "frontend/src/styles/index.css",
        "frontend/src/services/api.js",
        "frontend/src/store/store.js",
        "frontend/src/store/tasksSlice.js",
        "frontend/public/index.html",
        "frontend/Dockerfile",
    ]
    frontend_dest = os.path.join(base_dest_folder, "frontend")
    copy_files(project_root, frontend_dest, frontend_files, tree_output_file)
    
    # バックエンドのファイル
    backend_files = [
        "backend/Gemfile",
        "backend/Dockerfile",
        "backend/config/routes.rb",
        "backend/config/database.yml",
        "backend/erd.pdf",
        "backend/db/schema.rb"
    ]
    backend_dest = os.path.join(base_dest_folder, "backend")
    copy_files(project_root, backend_dest, backend_files, tree_output_file)
    
if __name__ == "__main__":
    main()