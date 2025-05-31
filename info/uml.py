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
}
class Board {
    # black_list:list[Disk]
    # white_list:list[Disk]
    --
    # is_safe():bool
    + display():None
    + play(player:str, order:tuple):None
}
class Disk {
    # color:str
    --
    + get_color():str
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
