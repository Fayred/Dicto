#include "dicto.h"
#include "ui_dicto.h"
#include "dialog_about.h"

#include <iostream>

dicto::dicto(QWidget *parent): QMainWindow(parent), ui(new Ui::dicto)
{
    ui->setupUi(this);
    text_tab_vect.push_back(new text_tab);
    ui->tabWidget->addTab(text_tab_vect[number_of_textEdit], "untitled");
    number_of_textEdit++;
}

dicto::~dicto()
{
    delete ui;
}

void dicto::on_actionNew_file_triggered()
{
    text_tab_vect.push_back(new text_tab);
    ui->tabWidget->addTab(text_tab_vect[number_of_textEdit], "untitled");
    text_tab_vect[number_of_textEdit]->set_fontSize(font_size);
    ui->tabWidget->setCurrentIndex(++index_of_current_window);
    number_of_textEdit++;
}

void dicto::on_actionOpen_file_triggered()
{
    std::string file_path = (QFileDialog::getOpenFileName(this, tr("Open file"))).toStdString();
    std::string content;

    if(!file_path.empty()){
        std::ifstream file;
        file.open(file_path);
        if(file.is_open()){
            while(!file.eof()){
                std::string line;
                getline(file, line);
                content += line+"\n";
            }
        }
        file.close();

        on_actionNew_file_triggered();
        text_tab_vect[index_of_current_window]->set_text(QString::fromStdString(content));
        text_tab_vect[index_of_current_window]->set_path(file_path);
        std::string filename = file_path.substr(file_path.find_last_of("/") + 1, file_path.length() - file_path.find_last_of("/"));
        ui->tabWidget->setTabText(index_of_current_window, QString::fromStdString(filename));
        text_tab_vect[index_of_current_window]->set_fileSave(true);
    }
}

void dicto::on_actionSave_triggered()
{
    std::string filename;
    if(!text_tab_vect[index_of_current_window]->get_fileSave()){
        std::string file_path = (QFileDialog::getSaveFileName(this, tr("Save file"))).toStdString();
        if(!file_path.empty()){
            text_tab_vect[index_of_current_window]->set_path(file_path);
            text_tab_vect[index_of_current_window]->set_fileSave(true);
            filename = file_path.substr(file_path.find_last_of("/") + 1, file_path.length() - file_path.find_last_of("/"));
            ui->tabWidget->setTabText(index_of_current_window, QString::fromStdString(filename));
        }
    }
    save_content_to_file(text_tab_vect[index_of_current_window]->get_path(), text_tab_vect[index_of_current_window]->get_text().toStdString());
}

void dicto::on_actionSave_as_triggered()
{
    std::string file_path = (QFileDialog::getSaveFileName(this, tr("Save file as"))).toStdString();
    text_tab_vect[index_of_current_window]->set_path(file_path);
    save_content_to_file(text_tab_vect[index_of_current_window]->get_path(), text_tab_vect[index_of_current_window]->get_text().toStdString());
}

void dicto::on_actionAbout_triggered()
{
    dialog_about w;
    w.show();
    w.exec();
}

void dicto::save_content_to_file(std::string filename, std::string content)
{
    std::ofstream file;
    file.open(filename);
    file << content;
    file.close();
}

void dicto::on_actionZoomIn_triggered()
{
    font_size++;
    for(auto text_edit: text_tab_vect)
        text_edit->set_fontSize(font_size);
}

void dicto::on_actionZoomOut_triggered()
{
    if(font_size > 1){
        font_size--;
        for(auto text_edit: text_tab_vect)
            text_edit->set_fontSize(font_size);
    }
}

void dicto::on_tabWidget_tabCloseRequested(int index)
{
    if(number_of_textEdit > 1){
        ui->tabWidget->removeTab(index);
        text_tab_vect.erase(text_tab_vect.begin()+index);
        number_of_textEdit--;
    }
}


void dicto::on_tabWidget_currentChanged(int index)
{
    index_of_current_window = index;
}

