from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


def show_database(self, name):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(name)
    db.open()

    view = self.bd_preview
    model = QSqlTableModel(self, db)
    model.setTable('record')
    model.select()
    view.setModel(model)
    for i in range(3):
        view.setColumnWidth(i, 280)