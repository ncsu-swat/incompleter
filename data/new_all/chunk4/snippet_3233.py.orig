#Source: https://stackoverflow.com/questions/76945050/qml-and-pyside6-typeerror-cannot-read-property-x-of-null
import sys

from PySide6.QtWidgets import QApplication

from dialog_manager import DialogManager

import style_rc


def main() -> None:
    app = QApplication(sys.argv)
    dialogManager = DialogManager()
    dialogManager.loadDialog(
            name="DateRangeDialog",
            width=800, 
            height=180, 
            startDates=["14/08/23", "15/08/23"], 
            endDates=["15/08/23"]
    )

    sys.exit(app.exec())


if __name__ == "__main__":
    main()