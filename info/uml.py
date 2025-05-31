from plantuml import PlantUML

server = PlantUML(url="http://www.plantuml.com/plantuml/svg/")

source = """
@startuml
abstract class GameObject {
    # height:int
    # width:int
    # coord_x:int
    # coord_y:int
    --
    # アーティストID [FK]
    # アルバムID [FK]
}
class Board {
    + アーティストID [PK]
    --
    + display():None
    + play(turn:str, order:list):None
}
class Disk {
    + color:str
    --
    + get_symbol():str
}
GameObject <|-- Board
GameObject <|-- Disk
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
