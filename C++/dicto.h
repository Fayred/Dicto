#ifndef DICTO_H
#define DICTO_H

#include <QMainWindow>
#include <QFileDialog>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

#include "text_tab.h"

QT_BEGIN_NAMESPACE
namespace Ui { class dicto; }
QT_END_NAMESPACE

class dicto : public QMainWindow
{
    Q_OBJECT

public:
    dicto(QWidget *parent = nullptr);
    ~dicto();

private slots:
    void on_actionNew_file_triggered();
    void on_actionOpen_file_triggered();
    void on_actionSave_triggered();
    void on_actionSave_as_triggered();
    void on_actionAbout_triggered();
    void on_actionZoomIn_triggered();
    void on_actionZoomOut_triggered();
    void on_tabWidget_tabCloseRequested(int index);
    void on_tabWidget_currentChanged(int index);

private:
    Ui::dicto *ui;
    int index_of_current_window = 0;
    int number_of_textEdit = 0;
    std::vector<text_tab*> text_tab_vect;
    int font_size = 12;

    void new_file();
    void save_content_to_file(std::string, std::string);
};
#endif // DICTO_H
