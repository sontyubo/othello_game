from plantuml import PlantUML

server = PlantUML(url="http://www.plantuml.com/plantuml/svg/")

source = """
@startuml
entity 曲 {
    + 曲ID [PK]
    --
    タイトル
    # アーティストID [FK]
    # アルバムID [FK]
}
entity アーティスト {
    + アーティストID [PK]
    アーティスト名
}
entity アルバム {
    + アルバムID [PK]
    アルバム名
}
曲 }o--|| アーティスト
曲 }|--o| アルバム
@enduml
"""


def save_img(data, output_dir: str) -> None:
    with open(f"{output_dir}/uml.svg", "wb") as f:
        f.write(data)


def main():
    data = server.processes(source)
    save_img(data, "info/")


if __name__ == "__main__":
    main()
